# chat_push_deploy.py

import os
from dotenv import load_dotenv
import subprocess
import hashlib
import time
import logging

load_dotenv()
logging.basicConfig(filename="push_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

username = os.getenv("GITHUB_USERNAME")
token = os.getenv("GITHUB_TOKEN")
repo = os.getenv("REPO_PATH")
branch = os.getenv("BRANCH", "main")

def is_duplicate(folder):
    hash_path = os.path.join(folder, ".__folder_hash__.md5")
    hasher = hashlib.md5()
    for root, _, files in os.walk(folder):
        for file in sorted(files):
            filepath = os.path.join(root, file)
            if os.path.isfile(filepath):
                with open(filepath, 'rb') as f:
                    while chunk := f.read(8192):
                        hasher.update(chunk)
    folder_hash = hasher.hexdigest()
    if os.path.exists(hash_path):
        with open(hash_path, 'r') as f:
            if f.read().strip() == folder_hash:
                return True
    with open(hash_path, 'w') as f:
        f.write(folder_hash)
    return False

def push_to_github(folder):
    if is_duplicate(folder):
        print("No changes to push.")
        return

    try:
        os.chdir(folder)
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
        subprocess.run(["git", "remote", "add", "origin", f"https://{username}:{token}@github.com/{username}/{repo}.git"], check=True)
        subprocess.run(["git", "checkout", "-B", branch], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Auto push at {time.strftime('%Y-%m-%d %H:%M:%S')}"], check=True)
        subprocess.run(["git", "push", "-u", "origin", branch, "--force"], check=True)
        print("Push complete.")
        logging.info("Push complete.")
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")
        logging.error(f"Git error: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", required=True, help="Path to folder to push")
    args = parser.parse_args()
    push_to_github(args.folder)
