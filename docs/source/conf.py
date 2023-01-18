# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../python'))


# -- Project information -----------------------------------------------------

project = 'DGL'
copyright = '2018, DGL Team'
author = 'DGL Team'

import dgl
version = dgl.__version__
release = dgl.__version__
dglbackend = os.environ.get("DGLBACKEND", "pytorch")


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.graphviz',
    'sphinx_gallery.gen_gallery',
    'sphinx_copybutton',
    'nbsphinx',
    'nbsphinx_link',
]

# TODO(#5199): 'auto' or 'always' should be used.
nbsphinx_execute = 'never'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
'''
if dglbackend == "mxnet":
    include_patterns = ['api/python/nn-mxnet*']
elif dglbackend == "tensorflow":
    include_patterns = ['api/python/nn-tensorflow*']
else:
    # pytorch
    exclude_patterns = ['api/python/nn-tensorflow*', 'api/python/nn-mxnet*']
'''

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/custom.css']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'dgldoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'dgl.tex', 'DGL Documentation',
     'DGL Team', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'dgl', 'DGL Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'dgl', 'DGL Documentation',
     author, 'dgl', 'Library for deep learning on graphs.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------
autosummary_generate = True
autodoc_member_order = 'alphabetical'

intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(sys.version_info), None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference', None),
    'matplotlib': ('http://matplotlib.org/', None),
    'networkx' : ('https://networkx.github.io/documentation/stable', None),
}

# sphinx gallery configurations
from sphinx_gallery.sorting import FileNameSortKey

examples_dirs = ['../../tutorials/blitz',
                 '../../tutorials/large',
                 '../../tutorials/dist',
                 '../../tutorials/models',
                 '../../tutorials/multi',
                 '../../tutorials/cpu']  # path to find sources
gallery_dirs = ['tutorials/blitz/',
                'tutorials/large/',
                'tutorials/dist/',
                'tutorials/models/',
                'tutorials/multi/',
                'tutorials/cpu']  # path to generate docs
if dglbackend != "pytorch":
    examples_dirs = []
    gallery_dirs = []

reference_url = {
    'dgl' : None,
    'numpy': 'http://docs.scipy.org/doc/numpy/',
    'scipy': 'http://docs.scipy.org/doc/scipy/reference',
    'matplotlib': 'http://matplotlib.org/',
    'networkx' : 'https://networkx.github.io/documentation/stable',
}

sphinx_gallery_conf = {
    'backreferences_dir' : 'generated/backreferences',
    'doc_module' : ('dgl', 'numpy'),
    'examples_dirs' : examples_dirs,
    'gallery_dirs' : gallery_dirs,
    'within_subsection_order' : FileNameSortKey,
    'filename_pattern' : '.py',
    'download_all_examples' : False,
}

# Compatibility for different backend when builds tutorials
if dglbackend == 'mxnet':
    sphinx_gallery_conf['filename_pattern'] = "/*(?<=mx)\.py"
if dglbackend == 'pytorch':
    sphinx_gallery_conf['filename_pattern'] = "/*(?<!mx)\.py"

# sphinx-copybutton tool
copybutton_prompt_text = r'>>> |\.\.\. '
copybutton_prompt_is_regexp = True
