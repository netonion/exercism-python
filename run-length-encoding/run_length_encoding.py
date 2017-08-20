import re

def decode(msg):
  return re.sub(r'(\d+)(.)', lambda m: m.group(2) * int(m.group(1)), msg)

def encode(msg):
  return re.sub(r'(.)\1+', lambda m: '{}{}'.format(len(m.group(0)), m.group(1)), msg)
