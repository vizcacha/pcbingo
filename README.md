# pcbingo

Requires: Python3, pycairo, a sane OS

Usage: python makebingo.py <text_file>

<text_file> should be a plain text file containing each category on a single line. The categories.text file in the repository is an example of such a file.

Output: A US letter sized pdf file (tentatively named 'test.pdf') that contains the bingo card as a vector graphic

TODO:

1. Word wrapping isn't the greatest
2. Color scheme
3. Specify output filename on CLI
4. Vertical spacing seems inconsistent
