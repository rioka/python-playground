# Introducing `uv`

This sample code is using the same code as [step-02](../step-02), but using [`uv`](https://docs.astral.sh/uv/) instead of `pip`.

## Installing `uv`

To install `uv`, run

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> `uv` is installed per-user.

## Create a project

To create a project with `uv`, run `uv init /path/to/project`.

Directory `/path/to/project` is created (if it does no exist), with this content:

```
├── .git
├── .gitignore
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

> To handle existing code, just go the the relevant folder and run `uv init` instead: existing files and folders are not modified, and all existing content is preserved.

## Running a project

Once you've created a project, you can run it with `uv run main.py https://...`; this automatically create a virtual environment and run the app

> In our case, it fails, because the existing code depends on `requests`: we have to restore dependencies first.

We can add dependencies with `uv add requests`.

> This updates `pyproject.toml`, adding `requests` to `dependencies`, and adds (or updates) `uv.lock`.

Direct dependencies are tracked in `pyproject.toml`; transitive ones are stored in `uv.lock` 

> **Note (for me)**: double check this.

If we have `requirements.txt` from existing code, we can import dependencies running `uv add -r requirements.txt`.

## Additional content

`.vscode` directory contains suggested extensions to run this projects in VS Code

## References

- [Managing Python Projects With uv: An All-in-One Solution](https://realpython.com/python-uv/)
