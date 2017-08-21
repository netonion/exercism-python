NORTH, EAST, SOUTH, WEST = range(4)

class Robot(object):
  def __init__(self, bearing=NORTH, x=0, y=0):
    self.coordinates = (x, y)
    self.bearing = bearing

  def turn_right(self):
    self.bearing = (self.bearing + 1) % 4

  def turn_left(self):
    self.bearing = (self.bearing - 1) % 4

  def advance(self):
    x, y = self.coordinates
    if self.bearing == NORTH:
      self.coordinates = (x, y + 1)
    elif self.bearing == EAST:
      self.coordinates = (x + 1, y)
    elif self.bearing == SOUTH:
      self.coordinates = (x, y - 1)
    elif self.bearing == WEST:
      self.coordinates = (x - 1, y)

  def simulate(self, commands):
    for c in commands:
      if c == 'R':
        self.turn_right()
      elif c == 'L':
        self.turn_left()
      elif c == 'A':
        self.advance()
