LARGE_HEIGHT = 10 # used to compare impossibly large height
FILE_NAME = "input-files/day9.txt"
def part1(lava_array):
  min_heights = []
  for i in range(0, len(lava_array)):
    print("Current row: " + str(lava_array[i]))
    for j in range(0,len(lava_array[i].strip())):
      curr_height = int(lava_array[i][j])
      top_height = LARGE_HEIGHT
      left_height = LARGE_HEIGHT
      bottom_height = LARGE_HEIGHT
      right_height = LARGE_HEIGHT
      if i != 0:
        top_height = int(lava_array[i-1][j])
      if i < len(lava_array) - 1:
        bottom_height = int(lava_array[i+1][j])
      if j != 0:
        left_height = int(lava_array[i][j-1])
      if j < len(lava_array[i]) - 1:
        right_height = int(lava_array[i][j+1])

      if curr_height < top_height and curr_height < bottom_height and curr_height < left_height and curr_height < right_height:
        min_heights.append(curr_height)
  
  risk_level = sum(min_heights) + len(min_heights)
  print("Min heights: " + str(min_heights))
  print("Risk level: " + str(risk_level))

my_file_2 = open(FILE_NAME, "r")
content_2 = my_file_2.read()
lava_array_permanent = content_2.split("\n")
def flood(curr_count, x, y):
  ## Past boundaries
  if x < 0 or y < 0:
    return 0
  if y > len(lava_array_permanent) - 1 or x > len(lava_array_permanent[y]) - 1:
    return 0
  ## If hit a 9, can't go any further
  if lava_array_permanent[y][x] == '9':
    return 0
  ## If hit an X, already been here. Don't count.
  if lava_array_permanent[y][x] == 'X':
    return 0

  ## Mark that we've been here
  lava_array_permanent[y] = lava_array_permanent[y][:x] + 'X' + lava_array_permanent[y][x + 1:]
  curr_count += 1
  ## Flood through each possible direction
  curr_count += flood(0, x+1, y)
  curr_count += flood(0, x-1, y)
  curr_count += flood(0, x, y+1)
  curr_count += flood(0, x, y-1)

  return curr_count
  
def part2(lava_array):
  flood_sizes = []
  for i in range(0, len(lava_array)):
    for j in range(0,len(lava_array[i].strip())):
      flood_size = flood(0, int(j), int(i))
      if flood_size > 0:
        flood_sizes.append(flood_size)
  
  flood_sizes.sort(reverse=True)
  print("Flood sizes: " + str(flood_sizes))
  mult_together = flood_sizes[0] * flood_sizes[1] * flood_sizes[2]
  print("Magic Number: " + str(mult_together))
## Parse file
my_file = open(FILE_NAME, "r")
content = my_file.read()
lava_array = content.split("\n")
# part1(lava_array)
part2(lava_array)
