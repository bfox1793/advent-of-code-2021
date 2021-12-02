
## Parse file
my_file = open("input-files/12-01-21-input-1.txt", "r")
content = my_file.read()
depth_list = content.split("\n")

## Convert list to ints
depth_list_ints = []
for depth in depth_list:
  depth_list_ints.append(int(depth))

## Basic check
last_depth = None
num_increases = 0

for depth in depth_list_ints:
  if last_depth is None:
    last_depth = depth
    continue

  if depth > last_depth:
    num_increases += 1

  last_depth = depth

print("Number of increases:", num_increases)

## Rolling average check
num_increases = 0
depth0 = None
depth1 = None
depth2 = None

for depth in depth_list_ints:
  if depth0 is None:
    depth0 = depth
    continue
  elif depth1 is None:
    depth1 = depth
    continue
  elif depth2 is None:
    depth2 = depth
    continue

  old_sum = depth0 + depth1 + depth2
  new_sum = depth1 + depth2 + depth

  if new_sum > old_sum:
    num_increases += 1

  depth0 = depth1
  depth1 = depth2
  depth2 = depth

print("Number of increases with rolling average:", num_increases)
