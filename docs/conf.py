# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))

import f5_sphinx_theme
import recommonmark
import CommonMark
from recommonmark.parser import CommonMarkParser


# -- Project information -----------------------------------------------------

project = u'F5 IPAM Controller'
copyright = u'2018 F5 Networks'
author = u'F5 Networks'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
with open('../next-version.txt') as verfile:
    v = verfile.readline().strip().split('.')
    # The short X.Y version.
    version = u'v{}.{}'.format(v[0], v[1])
    # The full version, including alpha/beta/rc tags.
    release = u'v{}.{}.{}-dev'.format(v[0], v[1], v[2])

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinxjp.themes.basicstrap',
    'sphinx.ext.extlinks',
    'cloud_sptheme.ext.table_styling'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md']

source_parsers = {
    '.md': CommonMarkParser,
}

# The master toctree document.
master_doc = 'index'

# External links
extlinks = {'issues': ('https://github.com/F5Networks/f5-ipam-ctlr/issues/%s', 'issue ')}

# Substitutions
rst_epilog = '''
.. |url-version| replace:: %(url_version)s
.. |release-notes| raw:: html

    <a href="%(base_url)s/products/connectors/f5-ipam-ctlr/%(url_version)s/RELEASE-NOTES.html">Release Notes</a>
.. |attributions| raw:: html

    <a href="%(base_url)s/products/connectors/f5-ipam-ctlr/%(url_version)s/_static/ATTRIBUTIONS.html">Attributions</a>
.. |ctlr| replace:: :code:`f5-ipam-ctlr`
.. |ctlr-long| replace:: F5 IPAM Controller
.. _annotations: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/
.. _ConfigMap: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
.. _F5 Container Connector: %(base_url)s/containers/latest/
.. _F5 BIG-IP Controller for Kubernetes: http://clouddocs.f5.com/products/connectors/k8s-bigip-ctlr/latest/
.. _F5 Resource: %(base_url)s/containers/latest/kubernetes/#f5-resource-properties
.. _Infoblox: https://www.infoblox.com/
.. _Ingress: https://kubernetes.io/docs/concepts/services-networking/ingress/
.. _Kubernetes: https://kubernetes.io/
.. _Kubernetes Secrets: https://kubernetes.io/docs/concepts/configuration/secret/
.. _OpenShift: https://www.openshift.com/
.. _ServiceAccount: https://kubernetes.io/docs/admin/service-accounts-admin/
.. _ClusterRole: https://kubernetes.io/docs/admin/authorization/rbac/#role-and-clusterrole
.. _ClusterRole Binding: https://kubernetes.io/docs/admin/authorization/rbac/#rolebinding-and-clusterrolebinding
''' % {
    'url_version': version,
    'base_url': 'http://clouddocs.f5.com'
}

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'venv',
    '.github',
    'Dockerfile',
    'requirements.txt',
    '*.swp',
    '*.swx',
    '*~',
    'README.rst'
    ]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'f5_sphinx_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'next_prev_link': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['./_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
   '**': ['localtoc.html', 'globaltoc.html', 'searchbox.html']
}

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
html_title = project

# A shorter title for the navigation bar.  Default is the same as html_title.
#
#html_short_title = u'F5 IPAM Controller'

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
html_use_index = False

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'F5IPAMControllerdoc'


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

latex_toplevel_sectioning = 'section'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'F5IPAMController.tex', u'F5 IPAM Controller Documentation',
     u'F5 Networks', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'F5_IPAM_Controller', u'F5 IPAM Controller Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'F5_IPAM_Controller', u'F5 IPAM Controller Documentation',
     author, 'F5_IPAM_Controller', 'One line description of project.',
     'Miscellaneous'),
]

texinfo_show_urls = 'footnote'

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {'https://docs.python.org/': None}