# Flask Web Form Template

Basic structure for starting a Flask web form project with Jinja templates

---

1. Clone this repository to local computer

2. Create a new repository in your GitHub and clone it to the local computer

3. Copy all files, EXCEPT the .git folder, from my repository folder into your repository folder

4. Delete my repository folder from your computer

5. Create a new virtual environment

   - Windows: `python -m venv ./venv`
   - Mac: `python3 -m venv ./venv`

6. Activate the new virtual environment

   - Windows: `.\venv\Scripts\activate`
   - Mac: `source ./venv/bin/activate`

7. Install the dependencies `pip install -r requirements.txt`

8. Run the program using either:

   - `flask run`
   - `python app.py`

9. Test the application by visiting it in your web browser

10. If everything is working, commit to your repository as an initial commit.

11. Create and change to a new local development branch `git checkout b development`

12. Continue working with the project as you normally would.

### TO-DO

- [x] Catch all selected activities in /add and put them into the python dictionary
- [ ] Create a confirmation page before submitting
- [ ] Submit records to database
- [ ] Delete a record
- [ ] Update a record
