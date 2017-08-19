def word_count(text):

  tally = {}
  word  = ''

  for c in text.lower():
    if c.isalnum():
      word += c
    elif word:
      tally[word] = tally.get(word, 0) + 1
      word = ''
    else:
      pass

  if word: tally[word] = tally.get(word, 0) + 1

  return tally
