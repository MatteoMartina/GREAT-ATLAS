#!/usr/bin/env python3
import json

files = ['smel_atlas_data.json', 'cic_atlas_data.json', 'cyn_atlas_data.json']

for fname in files:
    print(f"\n{'='*60}\n{fname}\n{'='*60}")
    try:
        with open(fname) as f:
            data = json.load(f)
        
        genes = data.get('genes', {})
        first_gene_id = list(genes.keys())[0]
        first_gene = genes[first_gene_id]
        
        print(f"Gene: {first_gene_id}")
        print(f"Tissues: {first_gene.get('tissues')}")
        print(f"\nBasemean keys:")
        
        basemean = first_gene.get('basemean', {})
        for key in sorted(basemean.keys()):
            print(f"  {key}")
        
        # Tissue patterns unici
        patterns = set()
        for gid in list(genes.keys())[:200]:
            bm = genes[gid].get('basemean', {})
            for key in bm.keys():
                patterns.add(key.split('__')[0])
        
        print(f"\nTissue patterns UNICI: {sorted(patterns)}")
        
    except Exception as e:
        print(f"ERRORE: {e}")
