# Contributing

# Local Setup for Development

To get started, install at least Python 3.8 and do the following:

## Linux / Mac OS

``` bash
git clone https://github.com/CSalih/dstack
python3 -m venv venv
venv/bin/pip install --editable ".[dev]"
source venv/bin/activate
dstack --version
```

This will install all required dependencies and create an "editable" virtual
environment ([virtualenv](https://docs.python.org/3/tutorial/venv.html)).
Editable means that any changes to the source code will be imminently reflected to the virtualenv.

## Code Style

`pre-commit` will help us to keep a consistent code style, for that you need to install the hooks.

``` bash
pre-commit install
```

That's it! Checks will run before a commit and issues will either be fixed
automatically or you will get an error message.