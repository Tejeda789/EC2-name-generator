import random 

#Get User Input
num_instances = int(input('How many EC2 department instance names do you need?:\n'))

# Make an empty list
departments = []

# Get each department name
print("\nType your department names:")
for i in range(num_instances):
    name = input(f"Department {i+1}: ")
    departments.append(name)

# Show what they typed
print("\nYour departments:")
for dept in departments:
    print(f"  - {dept}")

# Make unique names for each department
print("\n========================================")
print("Unique Department Names:")
print("========================================")


for dept in departments:
    # Make 3 random letters
    letters = ""
    for i in range(3):
        letters = letters + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    # Make 4 random numbers
    numbers = ""
    for i in range(4):
        numbers = numbers + random.choice("0123456789")
    
    # Put it all together
    unique_name = dept + "-" + letters + numbers
    print(f"  {dept} → {unique_name}")

print("========================================")

print("Thank you for using Haylin's EC2 Name Generator, have a good day!")