class School(object):
  def __init__(self, school):
    self.roster = {}

  def grade(self, n):
    return self.roster.get(n, set())

  def add(self, name, grade):
    self.roster.setdefault(grade, set()).add(name)

  def sort(self):
    return [(k, tuple(sorted(v))) for k, v in sorted(self.roster.items())]
