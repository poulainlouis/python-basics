# python-basics Jupyter Notebooks on [GitHub](https://github.com/bernardocarvalho/python-basics)
## Python files for Python introductory Course

### Running Notebooks Online:
You can run the main Notebook in your Browser using the next icons. 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bernardocarvalho/python-basics/HEAD) 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bernardocarvalho/python-basics/blob/main/python_basics.ipynb)   
(You may need to login with an Google Account)

### Running Notebooks locally:

1. Install JupyterLab in your system. Options are:
    * (MAC/Windows/Linux). Install [Anaconda](https://anaconda.org/conda-forge/download)
    * Install with package Manager ([Homebrew](https://brew.sh) / [Scoop](https://scoop.sh)/[Chocolatey](https://chocolatey.org)/ yum / apt / etc.)
2. Install `Git` Software version control system
3. Open a terminal (in Windows use **PowerShell**) and do:
    * `git clone https://github.com/bernardocarvalho/python-basics`
    * `cd python-basics`
4. Open JupyterLab App 
5. Preferably, create an account in [GitHub](https://github.com), [Fork](https://github.com/bernardocarvalho/python-basics/fork)
this repository, modify the notebook, create new ones  add them to your account with:
    * `git add new_notebook.ipynb`
    * `git commit -m "some informative commit message"`
    * `git push origin main`


## Jupyter Notebooks contain "Code" and "Text" _Cells_

1. Text _Cells_ are writen in [Markdown](https://en.wikipedia.org/wiki/Markdown) language.
2. For a brief reference, see [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet)
3. Math Equations can be included. They are writen in [MathJax/LaTeX](https://jupyterbook.org/en/stable/content/math.html)
    * See for example the Notebook [Magnetics Fields](Athens-ExB/Nonuniform%20and%20constant%20magnetic%20field.ipynb) in this repository.


## ISTTOK Tokamak specific files
### Required step before running ISTTOK data examples

#### Install SDAS

1. Download and `unzip sdas-1.zip`
2. In a terminal go to folder with setup.py
3. do `python(2/3) setup install`

Enjoy!
