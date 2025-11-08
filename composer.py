import hashlib

def cid_to_midi(cid):
    # Hash the CID to get entropy
    h = hashlib.sha256(cid.encode()).hexdigest()

    # Use first 6 hex digits to generate a triad (3 notes)
    notes = [int(h[i:i+2], 16) % 128 for i in range(0, 6, 2)]

    # Optional: log publishing power if hash starts with 'dead'
    publishing_power = h.startswith("dead")

    return notes, publishing_power
