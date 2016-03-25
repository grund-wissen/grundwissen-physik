# import sys, os
extensions = ['sphinx.ext.autodoc', 
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo', 
              'sphinx.ext.coverage', 
              'sphinx.ext.pngmath',
              'sphinx.ext.ifconfig', 
              'sphinx.ext.viewcode',
             ]

templates_path = ['_templates']
source_suffix  = '.rst'
master_doc     = 'index'

project   = "Grundwissen Physik"
copyright = "2011-2016, Bernhard Grotz"

version = '0.4.1e'
release = '0.4.1e'

language = 'de'
# spelling_lang = 'de_DE'

exclude_patterns = ["notes.rst", "*/notes.rst", "**/notes.rst","todos.rst", "README.rst"]

pygments_style = 'sphinx'

html_theme = 'sphinxdoc'
html_static_path = ['_static']
html_additional_pages = {'home': 'home.html'}
htmlhelp_basename = "Grundwissen Physik"
html_title        = "Grundwissen Physik"
html_short_title  = "Grundwissen Physik"
html_show_sourcelink = True
html_show_copyright  = False
html_show_sphinx     = False
html_last_updated_fmt = '%d.%m.%Y'
html_favicon = "favicon.ico"
html_logo    = "logo.png"
html_search_language = 'en'
html_search_options = {'type': 'default'}


trim_footnote_reference_space = True
todo_include_todos = False

latex_show_pagerefs = False
latex_preamble = r"""
\usepackage[version=3]{mhchem}
\usepackage{shadow}
\usepackage{amsmath, units, cancel}
\usepackage{amsfonts, amssymb,color}
\usepackage{pifont,mdframed,lscape}
\usepackage{nicefrac,marvosym,wasysym, textcomp, gensymb} 
\usepackage[left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}
% \usepackage{mathtools}
\setcounter{secnumdepth}{-1}
\setlength{\headheight}{15pt}
\setcounter{tocdepth}{2}
\clubpenalty  = 10000 % Disable single lines at the start of a page (Schusterjungen)
\widowpenalty = 10000 % Disable single lines at the end   of a page (Hurenkinder)
\displaywidowpenalty = 10000
\newenvironment{hinweis}
  {\par\begin{mdframed}[linewidth=1.5pt,linecolor=blue]%
    \begin{list}{}{\leftmargin=1cm
                   \labelwidth=\leftmargin}\item[\Large\ding{43}]}
  {\end{list}\end{mdframed}\par}
"""

pngmath_latex_preamble = latex_preamble
latex_elements = {
    "preamble": latex_preamble,
    "classoptions": "oneside,openany",
    "papersize": 'a4paper',
    "pointsize": '12pt',
    "fontpkg": '',
    "babel":    "\\usepackage[ngerman]{babel}",
    "fncychap": '',
}
# "fncychap": "\\usepackage[Conny]{fncychap}",
# Glenn ist auch schick


latex_documents = [
    ('index', 'grundwissen-physik.tex', "Grundwissen Physik",
        "Bernhard Grotz", 'manual'),
    ]

texinfo_documents = [
  ('index', 'Physik', "Grundwissen Physik",
   "Bernhard Grotz", "Physik", "Grundwissen Physik",
   ''),
]

intersphinx_mapping = {
    'gw':('http://grund-wissen.de/', None),
    'gwc':('http://grund-wissen.de/chemie/', None),
    'gwe':('http://grund-wissen.de/elektronik/', None),
    'gwm':('http://grund-wissen.de/mathematik/', None),
    'gwl': ('http://grund-wissen.de/linux/', None),
    'gwic': ('http://grund-wissen.de/informatik/c', None),
    'gwil': ('http://grund-wissen.de/informatik/latex', None),
    'gwip': ('http://grund-wissen.de/informatik/python', None),
}

