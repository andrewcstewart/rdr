import os
import sys
import pkgutil
from pathlib import Path
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.markdown import Markdown

import frontmatter
from mdutils.mdutils import MdUtils
from mdutils.fileutils import MarkDownFile

def init_project():
    pass

def load_config():
    pass

def list_resources(listing):   
    console = Console()     
    table = Table(title="List of records", min_width=400, style="blue")

    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Type", style="blue")
    table.add_column("Title", justify="right", style="green")

    for path in listing:
        with open(path) as f:
            post = frontmatter.load(f)
            table.add_row(post['id'], post['type'], post.get('title'))

    console.print(table, justify="center")   
    console.print(Panel("Hello, [red]World!", title="foobar"))
    cols = Columns([Panel("Hello, [red]World!", title="foobar"),Panel("Hello, [red]World!", title="foobar")])
    console.print(cols)


def make_rdr_md2(name, title = 'Markdown File Example'):
    mdFile = MdUtils(file_name=name,title=title)
    mdFile.new_header(level=1, title='Objective')
    mdFile.new_line('  - Inline link: ')
    mdFile.new_line('  - Inline link: ') 
    mdFile.new_header(level=1, title='Context')
    mdFile.new_line('  - Inline link: ' )
    mdFile.new_line('  - Inline link: ' )
    mdFile.new_header(level=1, title='Outcome')
    mdFile.new_list(['foo', 'bar'])
    mdFile.new_header(level=1, title='Next Steps')
    # mdFile.new_header(level=2, title='Atx Header 2')
    # mdFile.new_header(level=2, title='Atx Header 2')
    mdFile.new_paragraph("This is an example of text in which has been added color, bold and italics text.", bold_italics_code='bi', color='purple')
    mdFile.create_md_file()

def make_rdr_md(path, name, title = 'Markdown File Example'):
    data = pkgutil.get_data(__name__, "templates/rdr.md")
    post = frontmatter.loads(data)
    post['id'] = name
    post['title'] = title
    with open(f"{path}/{name}.md", 'w') as f:
        f.write(frontmatter.dumps(post))

def make_protocol_md():
    pass

def read_rdr_md(path):
    return MarkDownFile.read_file(path)

def view_md(path):
     with open(path) as f:
        post = frontmatter.load(f)
        console = Console()
        panels = []
        for k in post.keys():
            p = Panel(f"{post[k]}", title=f"[red]{k}")
            panels.append(p)
        console.print(Columns(panels,equal=False, expand=True))        
        md = Markdown(post.content)
        console.print(md)
