import math

REPLICATION_RESET_NUMBER = 6
NEW_FISH_START_NUMBER = 8

class fish:
  def __init__(self, initial_timer, created_day):
    self.current_timer = int(initial_timer)
    self.created_day = created_day
    self.total_replications = 0

  def count_replications(self, days):
    total_remaining_days = days - self.created_day
    initial_rep_rem_days = total_remaining_days - self.current_timer - 1

    ## If neg, then no replications will happen in remaining time
    if initial_rep_rem_days >= 0:
      self.total_replications = math.floor(initial_rep_rem_days / (REPLICATION_RESET_NUMBER + 1)) + 1

    return self.total_replications

  ## Return true if new fish spawned
  ## False otherwise
  def count_day(self):
    if self.current_timer == 0:
      self.current_timer = REPLICATION_RESET_NUMBER
      return True
    
    self.current_timer -= 1
    return False

  def __str__(self):
    return "Fish: " + str(self.current_timer)

def part1(initial_fishes, days):

  fishes = initial_fishes
  for i in range(0,days):
    ## Call count_day method on each fish in fishes
    ## If true, add fish to fishes array

    for j in range(0,len(fishes)):
      if fishes[j].count_day():
        fishes.append(fish(8,0))

    ## Print all fishies
    print("Day number: " + str(i))
    # for f in fishes:
    #   print(str(f))

  print("Total fishes: " + str(len(fishes)))

def calculate_total_reps_recursion(curr_fishes, total_days, total_reps, levels):
  # print("_____LEVEL " + str(levels) + "_____")
  # print("Total reps: " + str(total_reps))
  # print("Total new fishes: " + str(len(curr_fishes)))
  if len(curr_fishes) == 0:
    return total_reps

  curr_reps = 0
  for f in curr_fishes:
    curr_reps = f.count_replications(total_days)
    if (curr_reps > 0):
      new_fishes = []
      new_fishes.append(fish(NEW_FISH_START_NUMBER, f.current_timer + 1 + f.created_day))
      for i in range(1,int(curr_reps)):
        new_fishes.append(fish(NEW_FISH_START_NUMBER, new_fishes[0].created_day + i * (REPLICATION_RESET_NUMBER+1)))

      total_reps += calculate_total_reps_recursion(new_fishes, total_days, curr_reps, levels+1)

  return total_reps

def part2(initial_fishes, days):
  total_reps = calculate_total_reps_recursion(initial_fishes, days, 0, 0)

  total_fish = total_reps + len(initial_fishes)
  print("Total reps: " + str(total_reps))
  print("Total fish: " + str(total_fish))

def part2_faster(init_fish_array, days):
  fish_days = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0
  }

  for f in init_fish_array:
    fish_days[int(f)] += 1

  for day in range(0, days):
    print("___ DAY " + str(day) + "____")
    new_fishes = fish_days[0]

    print("New fishes: " + str(new_fishes))

    ## decrement fish_days values down
    for i in range(1,9):
      print("Increment: " + str(i))
      fish_days[i-1] = fish_days.get(i)
    ## None should be at 8 day yet
    fish_days[8] = 0

    ## Add new fishes / repeated fish
    fish_days[6] += new_fishes
    fish_days[8] = new_fishes

  print(fish_days)

  print("Total fishes: " + str(get_total_number(fish_days)))

def get_total_number(fishes):
  total = 0
  for i in range(0,9):
    total += fishes.get(i)

  return total
## Parse file
my_file = open("input-files/day6.txt", "r")
content = my_file.read()

initial_fish_timers = content.split(",")
initial_fishes = []
for initial_fish in initial_fish_timers:
  initial_fishes.append(fish(initial_fish,0))

# part1(initial_fishes, 80)
part2_faster(initial_fish_timers, 256)