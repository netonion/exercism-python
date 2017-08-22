translation = {
  0: 'zero',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety'
}

def say(num):
  if num < 0 or num >= 1e12:
    raise AttributeError
  if num < 21:
    return translation[num]
  if num < 100:
    return translation[num // 10 * 10] + (('-' + translation[num % 10]) if num % 10 else '')
  for limit, word in [(1e3, ' hundred'), (1e6, ' thousand'), (1e9, ' million'), (1e12, ' billion')]:
    if num < limit:
      div, mod = divmod(num, limit / 1e3 if limit > 1e3 else 100)
      return say(div) + word + ((' and ' if mod < 100 else ' ') + say(mod) if mod else '')
