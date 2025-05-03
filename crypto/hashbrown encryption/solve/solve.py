import sys
from hashlib import blake2s

SALT = b">rb<"

def decrypt(filename):
    if not filename.endswith(".enc"):
        sys.exit(1)
    try:
        with open(filename, "r") as f:
            hashes = [line.strip() for line in f if line.strip()]
        lookup = {}
        for i in range(256):
            for j in range(256):
                b = bytes([i, j])
                lookup[blake2s(SALT + b).hexdigest()] = b
        chunks = [lookup[h] for h in hashes]
        if chunks and chunks[-1].endswith(b" "):
            chunks[-1] = chunks[-1][:-1]
        with open("hashbrown_flag.pbm.zip", "wb") as f:
            f.write(b"".join(chunks))
    except:
        sys.exit(1)

decrypt("../dist/hashbrown_flag.pbm.zip.enc")