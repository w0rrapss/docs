import datetime
from pathlib import Path

project = "w0rraps test docs"
author = "w0rraps"
copyright = f"{datetime.date.today().year}, {author}"
release = "1.0"
api_version = "1.0"

pygments_style = "sphinx"
htmlhelp_basename = project
html_theme_options = {}
highlight_language = "python3"

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx"
]

rst_prolog = f"""
.. |api_version| replace:: {api_version}

.. role:: pycode(code)
   :language: python3
"""


exclude_patterns = []
source_suffix = ".rst"
master_doc = "index"

man_pages = [(master_doc, project, f"{project} Documentation", [author], 1)]
texinfo_documents = [
    (
        master_doc,
        project,
        f"{project} Documentation",
        author,
        project,
        "w0rraps test docs"
    ),
]
