#!/usr/bin/env python3

from watcher import watch_cids
from composer import cid_to_midi
from player import save_midi

def main():
    print("🎧 Overhash Composer is listening for new CIDs...\n")
    for cid in watch_cids("cids.txt"):
        notes, power = cid_to_midi(cid)

        print(f"🎯 CID: {cid}")
        print(f"🎵 Notes: {notes}")
        print(f"⚡ Publishing Power: {'🔥' if power else '—'}\n")

        filename = f"{cid[:8]}.mid"
        save_midi(notes, filename)

if __name__ == "__main__":
    main()
