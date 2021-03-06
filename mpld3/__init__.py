"""
mpld3: interactive D3 rendering of matplotlib images
====================================================

Functions: General Use
----------------------
- ``fig_to_d3`` : convert a figure to an html string

- ``show_d3`` : save a figure to HTML, and open in a web browser window


Functions: IPython Notebook
---------------------------
- ``display_d3`` : display a figure in an IPython notebook

- ``enable_notebook`` : enable automatic D3 display of figures
                        in the IPython notebook.

- ``disable_notebook`` : disable automatic D3 display of figures
                         in the IPython
"""

__version__ = '0.0.1'
__all__ = ["fig_to_d3", "display_d3", "show_d3",
           "enable_notebook", "disable_notebook"]

from .display import fig_to_d3, display_d3, show_d3
from .display import enable_notebook, disable_notebook
