def is_pangram(phrase):
  chars = filter(str.isalpha, phrase.lower())
  return len(set(chars)) == 26
