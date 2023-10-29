MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""
from rich.console import Console
from rich.markdown import Markdown
from chessboard import chessboard
from dicts import piecesASCII
console = Console()
#md = Markdown(MARKDOWN)
#console.print(md)

print(piecesASCII['b']['bB'])
