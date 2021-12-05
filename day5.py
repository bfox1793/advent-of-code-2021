import numpy
## Find max X and Y
## Initialize matrix, all at 0
## Iterate through input, incrementing matrix at X,Y

def parse_line_string(self):
  arr = self.line_string.split("->")
  point1 = str(arr[0]).strip()
  point2 = str(arr[1]).strip()

  point1_arr = point1.split(",")
  point2_arr = point2.split(",")

  self.x1 = int(point1_arr[0])
  self.x2 = int(point2_arr[0])
  self.y1 = int(point1_arr[1])
  self.y2 = int(point2_arr[1])

def get_intersection_points(self):
    ## loop through either X or Y to get intersecting points
    points = []
    if self.x1 == self.x2:
      x_point = self.x1
      for i in range(min(self.y1,self.y2), max(self.y1,self.y2) + 1):
        points.append([x_point, i])
    elif self.y1 == self.y2:
      y_point = self.y1
      for i in range(min(self.x1,self.x2), max(self.x1,self.x2) + 1):
        points.append([i, y_point])
    else:
      ## Add part 2
      print("Neither X or Y Match!!!")
      print(self)
      min_x = min(self.x1, self.x2)
      max_x = max(self.x1, self.x2)

      subtracting_x = self.x2 < self.x1
      subtracting_y = self.y2 < self.y1
      ## If decreasing x, subtract i from x1
      ## If decreasing y, subtract i from y1
      for i in range(max_x - min_x + 1):
        if subtracting_x and subtracting_y:
          points.append([self.x1-i, self.y1-i])
        elif subtracting_x:
          points.append([self.x1-i, self.y1+i])
        elif subtracting_y:
          points.append([self.x1+i, self.y1-i])
        else:
          points.append([self.x1+i, self.y1+i])
      print(points)

    return points
class line:
  def __init__(self, line_string):
    self.line_string = line_string
    self.x1 = None
    self.x2 = None
    self.y1 = None
    self.y2 = None
    parse_line_string(self)
    self.is_diagonal = (self.x1 != self.x2) and (self.y1 != self.y2)
    self.intersection_points = get_intersection_points(self)

  def __str__(self):
    return self.line_string

class pipe_array:
  def __init__(self, input_text):
    self.input_text = input_text
    
    lines_raw = self.input_text.split("\n")
    self.lines = []
    for curr_line in lines_raw:
      self.lines.append(line(curr_line))
    


def part1(pipes):
  global_intersection_points = []
  x_points = []
  y_points = []

  lines = pipes.lines

  for l in lines:
    x_points.append(l.x1)
    x_points.append(l.x2)
    y_points.append(l.y1)
    y_points.append(l.y2)
  max_x = max(x_points)
  max_y = max(y_points)

  print("Max X: " + str(max_x))
  print("Max Y: " + str(max_y))

  global_intersection_points = numpy.zeros((max_x+1, max_y+1))

  for pipe in pipes.lines:
    for points in pipe.intersection_points:
      curr_x = points[0]
      curr_y = points[1]

      global_intersection_points[curr_x, curr_y] += 1
  
  print(global_intersection_points)

  count = 0
  for row in global_intersection_points:
    for val in row:
      if val > 1:
        count += 1

  print("Num int: " + str(count))

## Parse file
my_file = open("input-files/day5.txt", "r") # NOT 17565
content = my_file.read()

pipes = pipe_array(content)
part1(pipes)