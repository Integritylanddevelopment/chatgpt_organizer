# explorer/preview_pane.py

import os
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def preview_readme_or_chat(file_path):
    if not os.path.exists(file_path):
        console.print(f"[red]File not found:[/red] {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if file_path.endswith(".md"):
                md = Markdown(content)
                console.print(md)
            else:
                console.print(content)
    except Exception as e:
        console.print(f"[red]Error reading file:[/red] {e}")
