# plugins/blog.py

import os
from rich.console import Console

console = Console()

def generate_blog_from_path(folder_path):
    if not os.path.exists(folder_path):
        console.print(f"[red]Folder not found:[/red] {folder_path}")
        return

    blog_file = os.path.join(folder_path, "blog_post.md")
    try:
        with open(blog_file, 'w', encoding='utf-8') as f:
            f.write("# Blog Summary\n\n")
            f.write("This is a generated blog post based on the folder contents.\n")
        console.print(f"[green]Blog post created at:[/green] {blog_file}")
    except Exception as e:
        console.print(f"[red]Failed to generate blog:[/red] {e}")
