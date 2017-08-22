def abbreviate(phrase):
  return ''.join(c for c in phrase.title() if c.isupper())
