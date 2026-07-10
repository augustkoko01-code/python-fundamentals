# Best Runner

class Runner:
    def __init__(self, name, event, time):
        # Save the runner's name, event, and time
        self.name = name
        self.event = event
        self.time = time

    def summary(self):
        # Return the runner's details as a formatted string
        return f"{self.event:<5}{self.name:<15}Time: {self.time:.2f}s"


# Function to find the fastest runner for each event
def find_best(runners):

    # Store the fastest runner for each event
    best = {}

    # Go through each runner in the list
    for runner in runners:

        # Save the runner if:
        # 1. The event is not in the dictionary yet, or
        # 2. The runner has a faster time
        if runner.event not in best or runner.time < best[runner.event].time:
            best[runner.event] = runner

    # Return the dictionary of fastest runners
    return best


# Create a list of Runner objects
runners = [
    Runner("Aiden Tan", "100m", 10.92),
    Runner("Marcus Lee", "100m", 11.34),
    Runner("Joel Sim", "200m", 21.88),
    Runner("Faiz Rahman", "200m", 22.15),
    Runner("Kenji Mori", "400m", 48.75),
    Runner("Devan Raj", "400m", 49.60),
    Runner("Lucas Wong", "800m", 109.85),
    Runner("Sanjay Pillai", "800m", 112.40)
]

# Find the fastest runner for each event
best = find_best(runners)

# The dictionary returned:
# {
#     "100m": Runner("Aiden Tan", "100m", 10.92),
#     "200m": Runner("Joel Sim", "200m", 21.88),
#     "400m": Runner("Kenji Mori", "400m", 48.75),
#     "800m": Runner("Lucas Wong", "800m", 109.85)
# }

print("--- Fastest Runner Per Event ---")

# List of events to display
events = ["100m", "200m", "400m", "800m"]

# Go through each event
for event in events:
    # Print the fastest runner for the current event
    print(best[event].summary())

# OUTPUT:
# --- Fastest Runner Per Event ---
# 100m Aiden Tan      Time: 10.92s
# 200m Joel Sim       Time: 21.88s
# 400m Kenji Mori     Time: 48.75s
# 800m Lucas Wong     Time: 109.85s