FILE_NAME = "input-files/day10.txt"
import math
matching_pairs = {
  "(" : ")",
  "[" : "]",
  "{" : "}",
  "<" : ">"
}

closing_items = ")]}>"

def peek_stack(stack):
  if stack:
    return stack[-1]  
  else:
    return None

class chunk:
  def __init__(self, input):
    self.chunk = input
    self.is_corrupted = False
    self.corrupted_char = ""
    self.is_complete = False
    self.missing_chars = ""

  def is_chunk_corrupted(self):
    curr_stack = []
    for curr_char in self.chunk:
      ## Nothing in stack - add char to stack
      if len(curr_stack) == 0:
        curr_stack.append(curr_char)
      else:
        first_char = peek_stack(curr_stack)
        ## If this is matching pair, pop item off stack
        if matching_pairs[first_char] == curr_char:
          curr_stack.pop()
        ## If element is closing element, stack is corrupted
        elif closing_items.find(curr_char) != -1:
          self.is_corrupted = True
          self.corrupted_char = curr_char
          return True
        else:
          curr_stack.append(curr_char)
    self.is_complete = len(curr_stack) == 0

    ## If chunk isn't complete, add missing chars
    if not(self.is_complete):
      for i in range(len(curr_stack)):
        curr_char = curr_stack.pop()
        self.missing_chars += matching_pairs[curr_char]

    return False

  def missing_value(self):
    if self.corrupted_char == ")":
      return 3
    elif self.corrupted_char == "]":
      return 57
    elif self.corrupted_char == "}":
      return 1197
    elif self.corrupted_char == ">":
      return 25137
    return 0  
  
  def completion_score(self):
    total_score = 0
    for c in self.missing_chars:
      total_score = total_score * 5
      if c == ")":
        total_score += 1
      elif c == "]":
        total_score += 2
      elif c == "}":
        total_score += 3
      elif c == ">":
        total_score += 4
    
    return total_score
def part1(input):
  chunks = []
  for value in input:
    chunks.append(chunk(value))

  corrupted_chunks = []
  for c in chunks:
    if c.is_chunk_corrupted():
      corrupted_chunks.append(c)

  total_sum = 0
  for corrupt in corrupted_chunks:
    total_sum += corrupt.missing_value()

  print("Part 1: " + str(total_sum))

def part2(input):
  chunks = []
  for value in input:
    chunks.append(chunk(value))

  incomplete_chunks = []
  for c in chunks:
    if not(c.is_chunk_corrupted()):
      incomplete_chunks.append(c)
  
  scores = []
  for incomplete in incomplete_chunks:
    scores.append(incomplete.completion_score())

  scores.sort()  
  mid_index = int(math.floor(len(scores)/2))
  print("Part 2: " + str(scores[mid_index]))
## Parse file
my_file = open(FILE_NAME, "r")
content = my_file.read()
input = content.split("\n")

part1(input)
part2(input)