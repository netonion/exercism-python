import re
def abbreviate(phrase):
  return ''.join(re.findall(r'\b\w', phrase)).upper()
