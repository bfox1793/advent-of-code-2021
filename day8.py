
## Count unique digit in outputs
## Just need to count len of result section
## 1 = 2 seg
## 4 = 4 seg
## 7 = 3 seg
## 8 = 7 seg 
## Therefore, count results with 2,3,4,7 lengths
def part1(input):
  all_inputs = input.split("\n")

  unique_count = 0
  for val in all_inputs:
    val_arr = val.split("|")
    ## Only consider results
    outputs = val_arr[1].strip().split(" ")
    for output in outputs:
      output_len = len(output)
      if (output_len in (2,3,4,7)):
        unique_count += 1
  
  print("Part 1 - Total Unique Outputs: " + str(unique_count))

res_map = {
  "a" : "",
  "b" : "",
  "c" : "",
  "d" : "",
  "e" : "",
  "f" : "",
  "g" : "",
}

input_map = {
  0 : "",
  1 : "",
  2 : "",
  3 : "",
  4 : "",
  5 : "",
  6 : "",
  7 : "",
  8 : "",
  9 : ""
}
def get_result(input_arr):
  inputs = input_arr.split("|")[0].strip().split(" ")
  outputs = input_arr.split("|")[1].strip().split(" ")

  ## Populate maps
  generate_maps(inputs)


  curr_res = ""
  for num in outputs:
    num_len = len(num)
    if (num_len == 2):
      curr_res += "1"
    elif (num_len == 3):
      curr_res += "7"
    elif (num_len == 4):
      curr_res += "4"
    elif (num_len == 5):
      ## 2,3,5
      if is_value_2(input_map, num):
        curr_res += "2"
        input_map[2] = num
      elif is_value_3(res_map, num):
        curr_res += "3"
        input_map[3] = num
      else:
        ## Know it has to be 5
        curr_res += "5"
        input_map[5] = num
    elif (num_len == 6):
      if is_value_9(input_map, num):
        curr_res += "9"
        input_map[9] = num
      elif is_value_0(res_map, num):
        curr_res += "0"
        input_map[0] = num
      else:
        ## Know it has to be 6
        curr_res += "6"
        input_map[6] = num
    elif (num_len == 7):
      curr_res += "8"

  print("Input map: " + str(input_map))
  print("Result map: " + str(res_map))
  return curr_res

def generate_maps(inputs):

  for input in inputs:
    input_len = len(input)
    if (input_len == 2):
      input_map[1] = input
    elif (input_len == 3):
      input_map[7] = input
    elif (input_len == 4):
      input_map[4] = input
    elif (input_len == 7):
      input_map[8] = input

  ## Find 9
  for input in inputs:
    if is_value_9(input_map, input):
      input_map[9] = input
  
  print("Current input map: " + str(input_map))
  ## Map a and e segments
  ## a = what is in 7 but not 1
  for c in input_map[7]:
    if input_map[1].find(c) == -1:
      res_map["a"] = c

  ## e is what is missing from 9
  for c in input_map[8]:
    if input_map[9].find(c) == -1:
      res_map["e"] = c
      

  ## Can find 2 now that we know e
  for input in inputs:
    if len(input) == 5 and input.find(res_map["e"]) != -1:
      input_map[2] = input

  ## f is 7 but not in 2
  for c in input_map[7]:
    if input_map[2].find(c) == -1:
      res_map["f"] = c

  ## c is 7 but not a or f
  for c in input_map[7]:
    if res_map["a"] != c and res_map["f"] != c:
      res_map["c"] = c

def is_value_9(input_map, value):
  ## 9 - if all chars in 4 / 7 are in curr
  if len(value) != 6:
    return False
  char_counter = 0
  for c in input_map[4]:
    if value.find(c) != -1:
      char_counter += 1
  for c in input_map[7]:
    if value.find(c) != -1:
      char_counter += 1
  ## If 7 matches, all were found, therefore it's 9
  return char_counter == 7

def is_value_2(input_map, value):
  ## Assumes 2 is in the input map
  char_counter = 0
  for c in value:
    if input_map[2].find(c) != -1:
      char_counter += 1

  return char_counter == 5

def is_value_0(res_map, value):
  ## len = 6 and has c char
  ## Assumes we already  know it isn't 9
  return len(value) == 6 and value.find(res_map["c"]) != -1

def is_value_3(res_map, value):
  ## len = 5 and has c char
  return len(value) == 5 and value.find(res_map["c"]) != -1

def part2(input):
  all_inputs = input.split("\n")

  outputs = []
  for val in all_inputs:
    outputs.append(get_result(val))

  print("Output array: " + str(outputs))
  sum = 0
  for res in outputs:
    sum += int(res)
  
  print("Output sum: " + str(sum))
## Parse file
my_file = open("input-files/day8.txt", "r")
content = my_file.read()

part1(content)
part2(content)