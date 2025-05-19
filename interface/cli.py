# interface/cli.py

from prompt_toolkit import PromptSession
from rich.console import Console

console = Console()

def cli_loop():
    session = PromptSession()

    while True:
        try:
            user_input = session.prompt('> ')
            if user_input in [":exit", ":quit"]:
                console.print("[bold red]Exiting ChatGPT Organizer...[/bold red]")
                break
            elif user_input == ":tree":
                from explorer.tree_view import show_tree
                show_tree()
            elif user_input.startswith(":preview "):
                from explorer.preview_pane import preview_readme_or_chat
                preview_readme_or_chat(user_input.replace(":preview ", "").strip())
            elif user_input.startswith(":replay "):
                from explorer.chat_replay import replay_chat
                replay_chat(user_input.replace(":replay ", "").strip())
            elif user_input.startswith(":plugin blog "):
                from plugins.blog import generate_blog_from_path
                generate_blog_from_path(user_input.replace(":plugin blog ", "").strip())
            else:
                console.print(f"[yellow]Unknown command:[/yellow] {user_input}")
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
