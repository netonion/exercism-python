num_to_roman = {
  1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
   100: 'C',  90: 'XC',  50: 'L',  40: 'XL',
    10: 'X',   9: 'IX',   5: 'V',   4: 'IV',
     1: 'I'
}

def numeral(num):
  roman = ''
  for bound in num_to_roman:
    while num >= bound:
      roman += num_to_roman[bound]
      num -= bound

  return roman
