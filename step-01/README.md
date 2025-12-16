# Using virtual environments

- Run `python -m venv venv` to create a virtual environment
- Run `source ./venv/bin/activate` to activate the virtual environment
- Run `python -m pip install requests` to install module `requests`

  Or, if you clone this repository, run `python -m pip install -r requirements.txt`

- Run `python -m pip freeze > requirements.txt` to register required modules
- Create a simple script that requests a page, and save it as `get_page.py`
- Run the script: `python get_page.py https://...`

> Depending on your setup, you may need to use `python3` instead of `python`.
