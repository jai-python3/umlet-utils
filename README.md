# umlet-utils

Software for generating Umlet class diagrams of a Python code base

Reference: https://www.umlet.com/



- [umlet-utils](#umlet-utils)
  - [Motivation](#motivation)
  - [Improvements](#improvements)
  - [Use Cases](#use-cases)
  - [Class Diagrams](#class-diagrams)
  - [Installation](#installation)
    - [Developers](#developers)
  - [Exported scripts](#exported-scripts)
  - [Contributing](#contributing)
  - [To-Do/Coming Next](#to-docoming-next)
  - [CHANGELOG](#changelog)
  - [License](#license)



## Motivation

Creating class diagrams can be a tedious process.<br>
This software can automatically read a Python codebase<br>
and then generate a UMLet .uxf file contain the class diagrams.


## Improvements

Please see the [TODO](TODO.md) for a list of upcoming improvements.


## Use Cases

![use case diagram](use_cases.png)


## Class Diagrams

![class diagrams](class_diagrams.png)

## Installation

Clone this project and then run the pip installer

```bash
git clone https://github.com/jai-python3/umlet-utils.git
cd umlet-utils
virtualenv -p python3 venv
source venv/bin/activate
python setup.py sdist
pip install .
```

You can uninstall like this:

```bash
pip uninstall umlet-utils
make clean
```

### Developers

If you modify the code in this package in your local virtual environment:

```shell
pip uninstall umlet-utils
make clean
python setup.py sdist
pip install .
```

If you want to export the code in this package to the PYPI repository:

Install `twine` and `setuptools`:

```shell
pip install twine setuptools
```


Build the Distribution Package

```shell
python setup.py sdist bdist_wheel
```

Configure your ~/.pypirc:

```bash
[pypi]
  username = __token__
  password = pypi-YOUR-TOKEN
```

Upload Your Package to PyPI

```shell
twine upload dist/*
```


Now you can install your package in your Python virtual environment

```shell
pip install umlet-utils
```


## Exported scripts

To use the exported scripts:
- umlet-utils-python-api-to-umlet-class-diagram
- umlet-utils-survey-python-codebase
- umlet-utils-yaml-to-use-case


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## To-Do/Coming Next

Please view the listing of planned improvements [here](TODO.md).

## CHANGELOG

Please view the CHANGELOG [here](CHANGELOG.md).

## License

[GNU AFFERO GENERAL PUBLIC LICENSE](LICENSE)
