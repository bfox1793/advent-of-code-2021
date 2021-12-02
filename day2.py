## Parse file
my_file = open("input-files/day2.txt", "r")
content = my_file.read()
nav_list = content.split("\n")

depth = 0
horizontal_position = 0

## Puzzle 1
for instruction in nav_list:
  inst_array = instruction.split(" ")

  inst_type = inst_array[0]
  value = int(inst_array[1])

  if inst_type == "forward":
    horizontal_position += value
  elif inst_type == "up":
    depth -= value
  elif inst_type == "down":
    depth += value

print("depth: " + str(depth) + " horizontal_position: " + str(horizontal_position))
final_value = depth * horizontal_position
print("final value: " + str(final_value))

## Puzzle 2
depth = 0
horizontal_position = 0
aim = 0
for instruction in nav_list:
  inst_array = instruction.split(" ")

  inst_type = inst_array[0]
  value = int(inst_array[1])

  if inst_type == "down":
    aim += value
  elif inst_type == "up":
    aim -= value
  elif inst_type == "forward":
    horizontal_position += value
    depth += value * aim

print("depth: " + str(depth) + " horizontal_position: " + str(horizontal_position))
final_value = depth * horizontal_position
print("final value: " + str(final_value))