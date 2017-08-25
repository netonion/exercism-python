class Luhn(object):
  def __init__(self, num):
    self.num = num.replace(' ', '')

  def is_valid(self):
    if len(self.num) < 2 or not self.num.isdigit(): return False
    luhn = 0
    for i, d in enumerate(reversed(self.num)):
      if i % 2:
        double = int(d) * 2
        luhn += double - 9 if double > 9 else double
      else:
        luhn += int(d)
    return not luhn % 10

