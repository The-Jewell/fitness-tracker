class User:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight  # Weight in pounds
        self.height = height  # Height in inches
        self.goals = []
        self.activities = []

    def calculate_bmi(self):
        # Calculate BMI using imperial units
        self.bmi = (self.weight / (self.height ** 2)) * 703
        return self.bmi

    def update_weight(self, new_weight):
        if new_weight != self.weight:  # Check if there's an actual change in weight
            weight_change = self.weight - new_weight
            self.weight = new_weight
            print(f"Weight updated to {new_weight} lbs.")
            self.update_goal_progress(weight_change)  # Update goal progress based on the weight change
        else:
            print("Weight remains the same. No update needed.")

    def update_goal_progress(self, weight_change):
        for goal in self.goals:
          if "lose weight" in goal.description.lower():  # Check if the goal is about losing weight
              goal.update_progress(weight_change)  # Update the progress with the weight change  

    def add_goal(self, goal):
        self.goals.append(goal)
        print(f"Added new goal: {goal}")

    def add_activity(self, activity):  # Ensuring this method is defined correctly
        self.activities.append(activity)
        print(f"Added activity: {activity.type} for {activity.duration} minutes.")

    def display_info(self):
        bmi = self.calculate_bmi()  # Calculate BMI
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years")
        print(f"Weight: {self.weight} lbs")
        print(f"Height: {self.height} inches")
        print(f"BMI: {bmi:.2f}")
        if self.activities:
            print("\nActivities:")
            for activity in self.activities:
                print(f"  - {activity.type} for {activity.duration} minutes, Calories burned: {activity.calculate_calories_burned():.2f}")
        else:
            print("\nNo activities logged.")
        if self.goals:
            print("\nGoals:")
            for goal in self.goals:
                print(f"  - {goal.description}, Target: {goal.target} lbs, Progress: {goal.progress} lbs")
        else:
            print("\nNo goals set.")

class Activity:
  def __init__(self, type, duration, user_weight):
    self.type = type
    self.duration = duration # in minutes
    self.user_weight = user_weight #in pounds

  def calculate_calories_burned(self):
    # Basic metabolic rates per minute by activity type (calories per minute per pound of body weight)
    rates = {
      'walking': 0.04,
      'jogging': 0.1,
      'lifting': 0.08
    }
    rate = rates.get(self.type, 0.05)  # default rate if activity type isn't recognized
    calories_burned = rate * self.duration * self.user_weight
    return calories_burned

class Goal:
    def __init__(self, description, target):
        self.description = description
        self.target = target
        self.progress = 0  # Initially, no progress has been made

    def update_progress(self, amount):
        self.progress += amount
        if self.progress >= self.target:
            print(f"Congratulations! You've met your goal to {self.description}!")
        else:
            print(f"Updated progress for {self.description}: {self.progress}/{self.target}")



print("Welcome to the Fitness Tracker!")
name = input("Please enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in lbs: "))
height = float(input("Enter your height in inches: "))

user = User(name, age, weight, height)  # User setup with initial input

while True:
    print("\n1. Add Activity")
    print("2. Update Weight")
    print("3. Add Goal")
    print("4. Display User Info")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        act_type = input("Enter activity type (walking, jogging, lifting): ")
        duration = int(input("Enter duration in minutes: "))
        activity = Activity(act_type, duration, user.weight)
        user.add_activity(activity)
        print(f"Calories burned: {activity.calculate_calories_burned():.2f}")
    
    elif choice == '2':
        new_weight = float(input("Enter new weight in lbs: "))
        user.update_weight(new_weight)
    
    elif choice == '3':
        description = input("Enter goal description (e.g., Lose weight): ")
        target = float(input("Enter goal target: "))
        goal = Goal(description, target)
        user.add_goal(goal)

    elif choice == '4':
        user.display_info()
    
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid option. Please try again.")


