import numpy
def get_delta(final_pos, curr_pos, is_fancy):
  delta = abs(final_pos - curr_pos)
  if is_fancy:
    count = 0
    for i in range(0,delta):
      count += i + 1
    return count

  return delta
def part1(positions, is_fancy):
  ## convert to int array
  positions_arr = []
  for p in positions:
    positions_arr.append(int(p))
  
  options = numpy.zeros(max(positions_arr))

  ## Loop
  for final_pos in range(0,max(positions_arr)):
    count = 0
    for curr_pos in positions_arr:
      delta = get_delta(final_pos, curr_pos, is_fancy)
      count += delta
    options[final_pos] = count

  print("Options array: " + str(options))
  min_fuel = min(options)
  min_pos = numpy.where(options == min_fuel)
  print("Min fuel: " + str(min_fuel))
  print("Min position: " + str(min_pos))


## Parse file
my_file = open("input-files/day7.txt", "r")
content = my_file.read()

horiz_positions = content.split(",")

part1(horiz_positions, False)
part1(horiz_positions, True)