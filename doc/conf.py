# -*- coding: utf-8 -*-
#
# QUAC documentation build configuration file, created by
# sphinx-quickstart on Wed Feb 20 12:04:35 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.4.9'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.mathjax', 'sphinx.ext.todo']
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Charliecloud'
copyright = u'2014–2020, Triad National Security, LLC'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = open("../lib/version.txt", "r").read().rstrip()
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%Y-%m-%d %H:%M %Z'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["doctrees", "html", "man"]

# FIXME: Workaround for older Sphinx that barf with:
#
#   WARNING: document isn't included in any toctree
#
# on files included via ".. include::'. I believe this was fixed in 1.4.3 and
# the relevant issue is: https://github.com/sphinx-doc/sphinx/issues/2603
exclude_patterns += ["*_desc.rst", "_deps.rst", "bugs.rst", "see_also.rst"]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# FIXME: Workaround for older versions of Sphinx. This is not needed in 1.8.5,
# but it is needed in 1.2.3. I don't know where the boundary is. We embed it
# in try/except so that "docs-sane" can import the file too.
try:
   import sphinx_rtd_theme
   html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
except ImportError:
   pass  # error caught elsewhere

highlight_language = 'console'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {'bodyfont': 'serif',  # for agogo
#                      'pagewidth': '60em',
#                      'documentwidth': '43em',
#                      'sidebarwidth': '17em',
#                      'textalign':'left'}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "logo-sidebar.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True  # deprecated in 1.6.6
smartquotes = True
smartquotes_action = "qBD"   # quotes, en and em dashes, but not ellipses

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'charliedoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'charlie.tex', u'Charliecloud Documentation',
   u'Reid Priedhorsky, Tim Randles, and others', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
   ("charliecloud", "charliecloud",
    "Lightweight user-defined software stacks for high-performance computing",
    [], 1),
   ("ch-build", "ch-build",
    "Build an image and place it in the builder's back-end storage",
    [], 1),
   ("ch-build2dir", "ch-build2dir",
    "Build a Charliecloud image from Dockerfile and unpack it into a directory",
    [], 1),
   ("ch-builder2squash", "ch-builder2squash",
    "Flatten a builder image into a Charliecloud SquashFS file",
    [], 1),
   ("ch-builder2tar", "ch-builder2tar",
    "Flatten a builder image into a Charliecloud image tarball",
    [], 1),
    ("ch-checkns", "ch-checkns",
     'Check "ch-run" prerequisites, e.g., namespaces and "pivot_root(2)"',
    [], 1),
   ("ch-dir2squash", "ch-dir2squash",
    "Create a SquashFS file from an image directory",
    [], 1),
   ("ch-grow", "ch-grow",
    "Build an image from a Dockerfile; completely unprivileged",
    [], 1),
   ("ch-fromhost", "ch-fromhost",
    "Inject files from the host into an image directory",
    [], 1),
   ("ch-mount", "ch-mount",
    "Mount a SquashFS image file using FUSE",
    [], 1),
   ("ch-nudge", "ch-nudge",
    "Delete or push image by HTTPS from or to repository",
    [], 1),
   ("ch-pull2dir", "ch-pull2dir",
    "Pull image from a Docker Hub and unpack into directory",
    [], 1),
   ("ch-pull2tar", "ch-pull2tar",
    "Pull image from a Docker Hub and flatten into tarball",
    [], 1),
   ("ch-run", "ch-run",
    "Run a command in a Charliecloud container",
    [], 1),
   ("ch-run-oci", "ch-run-oci", 'OCI wrapper for "ch-run"',
    [], 1),
   ("ch-ssh", "ch-ssh",
    "Run a remote command in a Charliecloud container",
    [], 1),
   ("ch-tar2dir", "ch-tar2dir",
    "Unpack an image tarball into a directory",
    [], 1),
   ("ch-test", "ch-test",
    "Run some or all of the Charliecloud test suite",
    [], 1),
   ("ch-tug", "ch-tug",
    "Pull and flatten image from repository to local filesystem",
    [], 1),
   ("ch-umount", "ch-umount",
    "Unmount a FUSE mounted squash filesystem and remove the mount point",
    [], 1),
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Charliecloud', u'Charliecloud Documentation',
   u'Reid Priedhorsky, Tim Randles, and others', 'Charliecloud', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'
