def transform(data):
  return {letter.lower(): score for score in data for letter in data[score]}
