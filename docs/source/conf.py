# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.abspath('mymodule')))


# -- Project information -----------------------------------------------------

project = 'LinearAlgebra'
copyright = '2021, Ziniu Yu'
author = 'Ziniu Yu'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for LaTeX output ------------------------------------------------
rst_prolog = r'''
.. math::
    
    \newcommand{\bs}{\boldsymbol}
    \newcommand{\dp}{\displaystyle}
    
    \newcommand{\cd}{\cdot}
    \newcommand{\cds}{\cdots}
    \newcommand{\lv}{\lVert}
    \newcommand{\rv}{\rVert}
    
    \newcommand{\b}{\boldsymbol{b}}
    \newcommand{\e}{\boldsymbol{e}}
    \newcommand{\i}{\boldsymbol{i}}
    \newcommand{\j}{\boldsymbol{j}}
    \newcommand{\u}{\boldsymbol{u}}
    \newcommand{\v}{\boldsymbol{v}}
    \newcommand{\w}{\boldsymbol{w}}
    \newcommand{\x}{\boldsymbol{x}}
    \newcommand{\y}{\boldsymbol{y}}

    \newcommand{\bb}{\begin{bmatrix}}
    \newcommand{\eb}{\end{bmatrix}}

    \newcommand{\im}{^{-1}}
'''

# # -- Options for MathJax -----------------------------------------------------
# mathjax_config = {
#     'TeX': {
#         'equationNumbers': { 'autoNumber': "AMS" }
#     }
# }