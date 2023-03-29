from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

books_dict = [
    {"title": "Blue Ocean",
            "author": "W. Chan Kim & Renee Mauborgne",
            "pages": 256,
            "classification": "non-fiction",
            "details": ["own it", "read it", "liked it", "recommend it"],
            "acquisition": "purchased"}
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", books=books_dict
    )

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

        activities_string = ", ".join(details)  # make the Python list into a string

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

        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
