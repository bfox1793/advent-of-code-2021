FILE_NAME = "input-files/day11.txt"

class octopus:
  def __init__(self, energy_level, x, y):
    self.energy_level = int(energy_level)
    self.has_flashed = False
    self.number_of_flashes = 0
    self.x = x
    self.y = y

  def ready_to_flash(self):
    if self.has_flashed:
      return False
    
    return self.energy_level > 9

  def increment(self):
    ## Skip if it already has flashed
    if self.has_flashed:
      return False
    self.energy_level += 1

    return self.energy_level > 9

  def reset_energy(self):
    self.has_flashed = False
    self.number_of_flashes += 1
    self.energy_level = 0
  def __str__(self):
    return str(self.energy_level) + " " + str(self.has_flashed)

def print_octo_array(octo_array):
  for arr in octo_array:
    print("Octopus Row: " + str(arr[0].y))
    for octo in arr:
      print(str(octo))

def init_octo_array(input_array):
  octopus_array = []
  curr_arr = []
  for i in range(0, len(input_array)):
    for j in range(0, len(input_array[i])):
      curr_arr.append(octopus(input_array[i][j], j, i))
    octopus_array.append(curr_arr)
    curr_arr = []
  
  return octopus_array

def increment_surrounding_octo(octopus_arr, x, y):

  possible_cases = [
    [y,x+1],
    [y,x-1],
    [y-1,x],
    [y+1,x],
    [y-1,x-1],
    [y-1,x+1],
    [y+1,x-1],
    [y+1,x+1]
  ]

  for case in possible_cases:
    curr_x = case[1]
    curr_y = case[0]
    # Skip bad cases
    if curr_x < 0 or curr_y < 0:
      continue
    if curr_y > len(octopus_arr) - 1 or curr_x > len(octopus_arr[0]) - 1:
      continue
    # Increment otherwise
    octopus_arr[curr_y][curr_x].increment()
  return octopus_arr

def flash_octos(octopus_arr):
  continue_flashing = True
  while(continue_flashing):
    for i in range(0, len(octopus_arr)):
      for j in range(0, len(octopus_arr[i])): 
        octo = octopus_arr[j][i]
        if octo.ready_to_flash():
          octopus_arr = increment_surrounding_octo(octopus_arr, octo.x, octo.y)
          octopus_arr[j][i].has_flashed = True
    ## Decide if we still need to keep flashing
    continue_flashing = False
    for octo_row in octopus_arr:
      for octo in octo_row:
        if octo.ready_to_flash():
          continue_flashing = True
  return octopus_arr
def part1(input):
  steps = 300
  octopus_array = init_octo_array(input)
  for i in range(0, steps):
    for octo_row in octopus_array:
      for octo in octo_row:
        if octo.increment():
          increment_surrounding_octo(octopus_array, octo.x, octo.y)
          octo.has_flashed = True
          flash_octos(octopus_array)
    ## Reset has_flashed and set energy levels to 0
    ## Part 2 - track # of flashed octopus
    ## If # flashed = num octopus, this is the row we want!
    octopus_flashed = 0
    for octo_row in octopus_array:
      for octo in octo_row:
        if octo.has_flashed:
          octo.reset_energy()
          octopus_flashed += 1
    
    total_octopus = len(octopus_array) * len(octopus_array[0])
    if total_octopus == octopus_flashed:
      print("Part 2: " + str(i+1))
  print_octo_array(octopus_array)
  sum_flashes = 0
  for octo_row in octopus_array:
    for octo in octo_row:
      sum_flashes += octo.number_of_flashes
  print("Part 1: " + str(sum_flashes))
    
## Parse file
my_file = open(FILE_NAME, "r")
content = my_file.read()
input = content.split("\n")
part1(input)