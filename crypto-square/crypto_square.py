from math import sqrt, ceil
import re

def encode(text):
  normalized = re.sub(r'\W', '', text.lower())
  c = ceil(sqrt(len(normalized)))
  return ' '.join(normalized[i::c] for i in range(c))
