import re
from collections import Counter

def word_count(text):
  words = re.findall('[^\W_]+', text.lower())
  return dict(Counter(words))
