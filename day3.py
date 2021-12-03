## Parse file
my_file = open("input-files/day3.txt", "r")
content = my_file.read()
binary_list = content.split("\n")

## Part 1
## Initialize final num array
final_num = []
for i in range(len(binary_list[0])):
  final_num.append(0)

## Calculate number of times each bit appears
for binary_num in binary_list:
  for i in range(0, len(binary_num)):
    curr_bit = binary_num[i]
    if curr_bit == "1":
      final_num[i] += 1
    elif curr_bit == "0":
      final_num[i] -= 1

## Convert to binary
## Negative = 0, positive = 1
gamma_rate = ""
for curr_bit in final_num:
  if (curr_bit > 0):
    gamma_rate += "1"
  else:
    gamma_rate += "0"

## Flip gamma rate to get epsilon rate
epsilon_rate = ""
for curr_bit in gamma_rate:
  if (curr_bit == "0"):
    epsilon_rate += "1"
  else:
    epsilon_rate += "0"
#print(gamma_rate)
#print(epsilon_rate)
gamma_rate_base10 = int(gamma_rate, 2)
epsilon_rate_base10 = int(epsilon_rate, 2)
#print("Final answer: " + str(gamma_rate_base10 * epsilon_rate_base10))


## Part 2

def recursion_time(remaining_options, bit_index, primary_bit):
  ## Base case
  if len(remaining_options) == 1:
    return remaining_options[0]
  
  final_list = calculate_final_num_list(remaining_options, primary_bit)

  print("Current final list: " + str(final_list))
  current_index_value = final_list[bit_index]

  ## If something, keep values with 1 in bit_index
  ## Else, keep values with 0 in bit_index
  next_values = []
  print("Current index value: " + str(current_index_value))
  if (current_index_value > 0 and primary_bit == "1") or (current_index_value < 0 and primary_bit == "0"):
    # Keep values with 1
    for i in range(0, len(remaining_options)):
      current_binary_value = remaining_options[i]
      print("Current value: " + current_binary_value)
      print("Current bit index: " + str(bit_index))
      print(current_binary_value[0])
      if current_binary_value[bit_index] == "1":
        next_values.append(current_binary_value)
  else:
    # Keep values with 0    
    for i in range(0, len(remaining_options)):
      current_binary_value = remaining_options[i]
      print("Current value: " + current_binary_value)
      print("Current bit index: " + str(bit_index))
      print(current_binary_value[0])
      if remaining_options[i][bit_index] == "0":
        next_values.append(current_binary_value)
  print(str(next_values))
  return recursion_time(next_values, bit_index + 1, primary_bit)
  #return next_values

def calculate_final_num_list(binary_list, primary_bit):
  ## Initialize final num array
  final_num = []
  for i in range(len(binary_list[0])):
    final_num.append(0)

  ## Calculate number of times each bit appears
  ## Final result - if positive, 1 more common. If negative, 0 more common
  for binary_num in binary_list:
    for i in range(0, len(binary_num)):
      curr_bit = binary_num[i]
      if curr_bit == "1":
        final_num[i] += 1
      elif curr_bit == "0":
        final_num[i] -= 1
  
  ## Convert final_result based on primary bit
  ## If primary bit = 1, flip 0s to 1
  ## If primary bit = 0, flip 1s to -1
  ## Will be used to determine if 0 or 1 route should be taken
  for i in range(0, len(final_num)):
    if final_num[i] == 0:
      if primary_bit == "1":
        final_num[i] = 1
      else:
        final_num[i] = 1
  
  return final_num

def multiple_binary_together(binary1,binary2):
  return int(binary1,2) * int(binary2,2)
def calculate_part_2(binary_list, primary_bit):
  
  final_value = recursion_time(binary_list, 0, primary_bit)

  print("Remaining: " + str(final_value))
  return final_value

oxygen_rating = calculate_part_2(binary_list, "1")
co2_scrubber_rating = calculate_part_2(binary_list, "0")

print("Oxygen rating: " + str(oxygen_rating))
print("Co2 scrubber rating: " + str(co2_scrubber_rating))

print(multiple_binary_together(str(oxygen_rating), str(co2_scrubber_rating)))