# Splitting code

This project replicates [step-01](../step-01), but using the page loading feature as a separate module, and importing it in the main *app*.

- Run `python -m venv venv` to create a virtual environment
- Run `source ./venv/bin/activate` to activate the virtual environment
- Run `python -m pip install requests` to install module `requests`

  Or, if you clone this repository, run `python -m pip install -r requirements.txt`

- Run `python -m pip freeze > requirements.txt` to register required modules
- Create a simple script that requests a page, and save it as `grabber/get_page.py`
- Create another script `app.py` that uses `grabber.get_page`
- Run the script: `python app.py https://...`

## Things to note

- `grabber` is a *package*

  Because it has no `__init__.py`, it is specifically a *namespace* package (PEP 420)

  > In this case, just importing the package does not do anything; if I add a `__init__.py`, I could add information about what is available and imported by default there.

There are two version of my "app", namely `app.py` and `app2.py`: they only differ in the way they import `grabber`:

- `app.py` uses an alias for `grabber.get_page`
- `app2.py` import `grabber.get_page` *as-is*
