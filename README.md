# Python Library Template

Template for creating python libraries easily.

<br/>

## Why do I need this folders and files?

* python_lib_name: This folder will contain your library. It has to be renamed as your library's name.
* tests: Folder that will contain the tests for your library.
* venv: Not included in the repo because it has many files (check .gitignore). It is very recommended to have all the packages that need to be installed in the virtual environment, so that they don't interfere with the packages installed on your machine.
* requirements.txt: In this txt file I am leaving the basic packages that are needed to actually create a Python library. Install them before starting.
* setup.py: File that will help us build the library.

<br/>
<br/>

## What are the steps I need to follow in order to create a new library?

1) Create a virtual environment to store all the dependencies that will be needed. This is highly recommended to ensure that the dependencies you add don't collide or conflict another dependencies that already are on your machine.

```
python -m venv <name of your venv>
source <name of your venv>/bin/activate
```

2) Install the requirements.txt file.

```
pip install -r requirements.txt
```

3) You are ready to start coding! Remember to update the setup.py with the new dependencies you add.


<br/>
<br/>

## How do I run tests?

This is the command you are looking for:

```
python setup.py pytest
```

Run it after creating a new function in the test_my_functions.py file, importing the library you created.

<br/>
<br/>

## How do I build the library?

Run the following command:

```
python setup.py bdist_wheel
```

<br/>
<br/>

## After building the library, how can I try everything is working fine?

First install your own library using the following command.

```
pip install dist/<name of the wheelfile>.whl
```

You will be using the wheel you generated building the library to install your own library.

Once you have done this, you can import your library as any other in the world:

```
from python_lib_name import my_functions
```

<br/>
<br/>

## How do I upload my package?

After creating an account on [PyPi](https://pypi.org/), run the following command:

```
twine upload dist/*
```