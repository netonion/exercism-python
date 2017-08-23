class Garden(object):
  STUDENTS = ['Alice', 'Bob', 'Charlie', 'David',
              'Eve', 'Fred', 'Ginny', 'Harriet',
              'Ileana', 'Joseph', 'Kincaid', 'Larry']

  CHAR_TO_PLANT = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}

  def __init__(self, text, students=STUDENTS):
    students.sort()
    l1, l2 = text.split()
    self.assignment = {students[i // 2]:[Garden.CHAR_TO_PLANT[c] for c in [l1[i], l1[i + 1], l2[i], l2[i + 1]]]
      for i in range(0, len(l1), 2)}

  def plants(self, name):
    return self.assignment[name]
