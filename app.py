from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

books_dict = [
    {"name": "Test", "flavor": "swirl", "read": "yes", "activities": "reading"}
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=books_dict
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
        details = form.getlist("details")  # this is a PYthon list
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
