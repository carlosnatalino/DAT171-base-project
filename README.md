# DAT171 template project

*Important:*
- You must not clone this repository. You must use it as a template.

This repository provides initial files for a base project of the course DAT171 Object-oriented programming in Python.

More info: https://www.chalmers.se/en/education/your-studies/find-course-and-programme-syllabi/course-syllabus/DAT171/

## Installation

This repository assumes the use of Python 3.12 or 3.13.
To install the necessary packages, we have three steps.

1. Install `pip-compile`:

```bash
pip install -U pip pip-compile
```

2. Compile the list of requirements:

```bash
pip-compile requirements.in
```

3. Install the requirements:

```bash
pip install -r requirements.txt
```

We also recommend installing this extension pack to VSCode: https://marketplace.visualstudio.com/items?itemName=CarlosNatalino.chalmers-applied-object-oriented-programming

You can also install the extension through the command line:

```bash
code  --install-extension CarlosNatalino.chalmers-applied-object-oriented-programming
```
