#!/usr/bin/env python3

from mido import Message, MidiFile, MidiTrack
import os

def save_midi(notes, filename="output.mid", folder="midi"):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    for note in notes:
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=480))

    if not os.path.exists(folder):
        os.makedirs(folder)

    path = os.path.join(folder, filename)
    mid.save(path)
    print(f"🎼 Saved: {path}")
    return path

def save_full_song(cids, filename="full_song.mid", folder="midi"):
    from composer import cid_to_midi

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    for cid in cids:
        notes, _ = cid_to_midi(cid)
        for note in notes:
            track.append(Message('note_on', note=note, velocity=64, time=0))
            track.append(Message('note_off', note=note, velocity=64, time=480))

    if not os.path.exists(folder):
        os.makedirs(folder)

    path = os.path.join(folder, filename)
    mid.save(path)
    print(f"🎼 Full song saved to {path}")
    return path
