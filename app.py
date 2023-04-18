from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)

app.config["SECRET_KEY"] = "XqsuG9QW8\das#\]i"


books_dict = [
    {"title": "Blue Ocean",
    "author": "W. Chan Kim & Renee Mauborgne",
    "pages": 256,
    "classification": "non-fiction",
    "details": ["own it", "read it", "liked it", "recommend it"],
    "acquisition": "purchased"}
]

###### Custom Error Pages ######
# Handling error 404 and displaying relevant web page


@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html", pageTitle=""), 404


# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


####### Routes #######
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", books=books_dict
    )

# For testing purposes.
@app.route('/trigger-500')
def trigger_500():
    raise Exception('This is a test 500 error')


@app.route("/about", methods=["GET"])
def about():
    return render_template(
        "about.html", pageTitle="About Page"
    )


@app.route("/add", methods=["POST"])
def add():

    if request.method == "POST":

        form = request.form

        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        classification = form["classification"]
        details = form.getlist("details")  # this is a python list
        acquisition = form["acquisition"]

        # make the Python list into a string
        activities_string = ", ".join(details)

        add_books_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "classification": classification,
            "details": details,
            "acquisition": acquisition
        }

        books_dict.append(
            add_books_dict
        )  # append this dictionary entry to the larger books dictionary

        flash(
            "The book ;" + title + " has been added to the database.",
            "success",)

        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=False)
