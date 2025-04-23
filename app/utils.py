import requests

def consultar_ensembl(chrom, pos, ref, alt):
    url = f'https://rest.ensembl.org/vep/human/region/{chrom}:{pos}:{ref}/{alt}'
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    if not r.ok:
        return {}
    data = r.json()[0] if r.json() else {}
    return {
        'gene': data.get('transcript_consequences', [{}])[0].get('gene_symbol', ''),
        'consequence': ','.join(data.get('most_severe_consequence', '').split(',')),
        'impact': data.get('transcript_consequences', [{}])[0].get('impact', ''),
        'sift': data.get('transcript_consequences', [{}])[0].get('sift_prediction', ''),
        'polyphen': data.get('transcript_consequences', [{}])[0].get('polyphen_prediction', ''),
        'af': data.get('colocated_variants', [{}])[0].get('frequencies', {}).get(alt.lower(), {}).get('gnomad', 0.0),
        'classification': 'benign' if data.get('transcript_consequences', [{}])[0].get('impact', '') == 'LOW' else 'pathogenic'
    }