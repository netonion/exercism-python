def is_isogram(phrase):
  chars = list(filter(str.isalnum, phrase.lower()))
  return len(set(chars)) == len(chars)
