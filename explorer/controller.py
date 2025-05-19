# explorer/controller.py

import os
from rich.console import Console
from rich.tree import Tree

console = Console()

def list_folders(base_path):
    return [f.name for f in os.scandir(base_path) if f.is_dir()]

def list_files(base_path):
    return [f.name for f in os.scandir(base_path) if f.is_file()]

def build_tree(path, tree):
    for entry in os.scandir(path):
        if entry.is_dir():
            branch = tree.add(f"📁 {entry.name}")
            build_tree(entry.path, branch)
        else:
            tree.add(f"📄 {entry.name}")

def render_directory_tree(start_path="."):
    tree = Tree(f"[bold cyan]{start_path}[/bold cyan]")
    build_tree(start_path, tree)
    console.print(tree)
