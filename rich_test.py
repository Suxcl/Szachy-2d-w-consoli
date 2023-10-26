from rich import print
from rich.layout import Layout
layout = Layout()
layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)
layout["upper"].size = None
layout["upper"].ratio = 2
layout["lower"].minimum_size = 10
print(layout)