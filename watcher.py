import time
import os

SEEN_FILE = ".seen_cids.txt"

def load_seen():
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE, "r") as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_seen(seen):
    with open(SEEN_FILE, "w") as f:
        for cid in seen:
            f.write(cid + "\n")

def watch_cids(file_path):
    seen = load_seen()
    while True:
        if not os.path.exists(file_path):
            print(f"⚠️ File {file_path} not found.")
            time.sleep(2)
            continue

        updated = False
        with open(file_path, "r") as f:
            for line in f:
                cid = line.strip()
                if cid and cid not in seen:
                    seen.add(cid)
                    updated = True
                    yield cid

        if updated:
            save_seen(seen)

        time.sleep(2)

