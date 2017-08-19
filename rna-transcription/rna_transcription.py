mapping = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}

def to_rna(dna):
  rna = ''
  for n in dna:
    if mapping.get(n):
      rna += mapping.get(n)
    else:
      return ''
  return rna
