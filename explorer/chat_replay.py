# explorer/chat_replay.py

import json
import time
from rich.console import Console

console = Console()

def replay_chat(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for line in data:
            role = line.get("role", "unknown")
            content = line.get("content", "")
            console.print(f"[bold cyan]{role}:[/bold cyan] {content}")
            time.sleep(1)
    except Exception as e:
        console.print(f"[red]Failed to replay chat:[/red] {e}")
