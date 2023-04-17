import pytest
from flask import Flask, url_for
from app import app, books_dict

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Unit test to check if the homepage is rendering the template
def test_index():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Web form template" in response.data


# Unit test to check if the about page is rendering the template
def test_about():
    with app.test_client() as client:
        response = client.get('/about')
        assert response.status_code == 200
        assert b"About Page" in response.data


# Functional test to check if a book can be added to the database
def test_add_book():
    with app.test_client() as client:
        response = client.post('/add', data={
            'title': 'New Book',
            'author': 'New Author',
            'pages': '100',
            'classification': 'fiction',
            'details': ['own it', 'read it'],
            'acquisition': 'gift'
        }, follow_redirects=True)
        assert response.status_code == 200
        assert b"The book ;New Book has been added to the database." in response.data


# Integration test to check if the added book is present in the database
def test_added_book_in_database():
    assert len(books_dict) == 2
    assert books_dict[1]['title'] == 'New Book'
    assert books_dict[1]['author'] == 'New Author'
    assert books_dict[1]['pages'] == '100'
    assert books_dict[1]['classification'] == 'fiction'
    assert books_dict[1]['details'] == ['own it', 'read it']
    assert books_dict[1]['acquisition'] == 'gift'


# Test the not_found_error function by making a GET request to a non-existent page
# and expecting a 404 error response with the "404 Page Not Found" message in the response data    
def test_not_found_error(client):
    response = client.get("/non-existent-page")
    assert response.status_code == 404
    assert b"404 Page Not Found" in response.data

# Test the internal_error function by creating a new route that will raise an exception
# when accessed. We make a GET request to that route and expect a 500 error response
# with the "500 Internal Server Error" message in the response data
def test_internal_error(client):
    @app.route("/error")
    def error():
        raise Exception("test error")

    response = client.get("/error")
    assert response.status_code == 500
    assert b"500 Internal Server Error" in response.data
