# Class to represent a car park
class CarPark:

    # Runs automatically when a new CarPark object is created
    def __init__(self, capacity=20):
        self.capacity = capacity      # Maximum number of cars the car park can hold
        self.occupied = 0             # Current number of parked cars

    # Runs when print(object) is used
    def __str__(self):
        return "🚗" * self.occupied    # Show one car emoji for each parked car

    # Add n cars to the car park
    def park(self, n):
        self.occupied += n            # Increase the number of parked cars

    # Remove n cars from the car park
    def leave(self, n):
        self.occupied -= n            # Decrease the number of parked cars


cp = CarPark(3)       # Create a car park with a capacity of 3 cars

cp.park(2)            # Park 2 cars
print(cp)             # Display 🚗🚗

cp.leave(1)           # Remove 1 car
print(cp)             # Display 🚗

print(cp.capacity)    # Display the maximum capacity (3)
print(cp.occupied)    # Display the current number of parked cars (1)