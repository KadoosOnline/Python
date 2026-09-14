# __init__.py runs when the package is imported. Re-exporting the names here
# gives the user of the package a single, simple entry point:
#     from math_package import add, sub
#
# The dot in '.my_math' means "the module my_math of THIS package"
# (a relative import).
from .my_math import add, mul
from .your_math import sub, div
