# compiler/summarizer.py

import os

def summarize_folder(folder_path):
    summary = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    summary[file] = f.readline().strip()
    return summary
