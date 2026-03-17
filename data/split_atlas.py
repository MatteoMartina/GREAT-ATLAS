#!/usr/bin/env python3
"""
Splitta i 3 atlas JSON grandi in 3 chunk ciascuno.
Uso: python3 split_atlas.py
Eseguire nella cartella data/ oppure aggiornare i path sotto.

Output:
  smel_atlas_data_1.json, smel_atlas_data_2.json, smel_atlas_data_3.json
  cic_atlas_data_1.json,  cic_atlas_data_2.json,  cic_atlas_data_3.json
  cyn_atlas_data_1.json,  cyn_atlas_data_2.json,  cyn_atlas_data_3.json
"""

import json, os, math

FILES = [
    "smel_atlas_data.json",
    "cic_atlas_data.json",
    "cyn_atlas_data.json",
]

N_CHUNKS = 3

for fname in FILES:
    if not os.path.exists(fname):
        print(f"SKIP (not found): {fname}")
        continue

    print(f"Loading {fname} ...")
    with open(fname) as f:
        data = json.load(f)

    # Normalize to dict if needed
    if isinstance(data, list):
        data = {g['id']: g for g in data if 'id' in g}
    elif isinstance(data, dict) and 'genes' in data:
        data = data['genes']

    keys = list(data.keys())
    total = len(keys)
    chunk_size = math.ceil(total / N_CHUNKS)

    base = fname.replace(".json", "")
    for i in range(N_CHUNKS):
        chunk_keys = keys[i*chunk_size:(i+1)*chunk_size]
        chunk = {k: data[k] for k in chunk_keys}
        out_name = f"{base}_{i+1}.json"
        with open(out_name, 'w') as f:
            json.dump(chunk, f)
        size_mb = os.path.getsize(out_name) / 1024 / 1024
        print(f"  -> {out_name}: {len(chunk)} genes, {size_mb:.1f} MB")

    print(f"  Done: {total} genes split into {N_CHUNKS} chunks\n")

print("All done. Copy the *_1.json *_2.json *_3.json files to data/")
print("You can keep or delete the original large files.")
