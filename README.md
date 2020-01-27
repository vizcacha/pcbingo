# pcbingo

Requires: Python3, pycairo, a sane OS

Usage: ./makebingo.py <text_file> <output_filename>

<text_file> should be a plain text file containing each category on a single line. The categories.text file in the repository is an example of such a file. 

Output: A US letter sized pdf file (with filename as specified on command line) that contains the bingo card as a vector graphic

TODO:

1. Word wrapping isn't the greatest
2. Color scheme
3. Vertical spacing seems inconsistent
