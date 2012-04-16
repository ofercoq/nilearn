# -*- coding: utf-8 -*-
#
# sphinx-quickstart on Fri Nov 28 22:10:09 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.append(os.path.abspath('sphinxext'))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 
        ##'matplotlib.sphinxext.plot_directive', 
        #'plot_directive',
        #'only_directives',
        #'ipython_console_highlighting',
        ##'matplotlib.sphinxext.only_directives',
         #'sphinx.ext.pngmath',
        #]#'sphinx.ext.intersphinx']

doctest_test_doctest_blocks = 'true'

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u"NISL"
copyright = u'INRIA Parietal 2010'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = '2010'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en' 

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'


# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Options for HTML output
# -----------------------
html_theme_path = ['themes']

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
#html_style = 'default.css'
html_theme = "scikit-learn"
#html_theme_options = {"stickysidebar":"True"}


# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "NeuroImaging with the scikit-learn"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Nisl"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "scikitlearn.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.static']

# If false, no index is generated.
html_use_index = False 

# Output file base name for HTML help builder.
htmlhelp_basename = 'PythonScientic'


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Latex references with page numbers (only Sphinx 1.0)
#latex_show_pagerefs = True
 
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
#latex_documents = [
  #('index', 'PythonScientific.tex', ur'Python Scientific lecture notes',
   #ur"""EuroScipy tutorial team \\\relax
   #\normalfont Editors: Emmanuelle Gouillart, Gaël Varoquaux""", 
   #'manual'),
#]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'scikitlearn.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# Additional stuff for the LaTeX preamble.
latex_preamble = """
\definecolor{VerbatimColor}{rgb}{0.95,1,0.833}
\definecolor{VerbatimBorderColor}{rgb}{0.6,0.6,0.6}
"""

latex_elements = {
    'classoptions': ',oneside,openany',
    'babel': '\usepackage[english]{babel}',
    #'tableofcontents': '\\pagestyle{normal}\\pagenumbering{arabic} %\\tableofcontents',
} 

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'http://docs.python.org/dev': None,
    'http://docs.scipy.org/doc/numpy': None,
}

# Increase pngmath font size
pngmath_dvipng_args = ['-gamma 1.5', '-D 180']
pngmath_use_preview = True
