class Allergies(object):

  ALLERGIES = [
    'eggs',
    'peanuts',
    'shellfish',
    'strawberries',
    'tomatoes',
    'chocolate',
    'pollen',
    'cats'
  ]

  def __init__(self, score):
    self.lst = [allergy for i, allergy in enumerate(self.ALLERGIES) if score & (1 << i)]

  def is_allergic_to(self, allergy):
    return allergy in self.lst
