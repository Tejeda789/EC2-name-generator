import random 

#Get User Input
num_instances = int(input('How many EC2 department instance names do you need?:\n'))

# Make an empty list
departments = []

# Get each department name (simple way)
print("\nType your department names:")

dept1 = input("Department 1: ")
dept2 = input("Department 2: ")
dept3 = input("Department 3: ")

# Put them in a list
departments = [dept1, dept2, dept3]

# Show what they typed
print("\nYour departments:")
for dept in departments:
    print(f"  - {dept}")

# Make unique names for each department
print("========================================")
print("Unique Department Names:")

for dept in departments:
    # Pick 3 random letters one at a time
    letter1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    letter2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    letter3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    # Pick 4 random numbers one at a time
    number1 = random.choice("0123456789")
    number2 = random.choice("0123456789")
    number3 = random.choice("0123456789")

    
    # Put everything together
    unique_name = dept + "-" + letter1 + letter2 + letter3 + number1 + number2 + number3 + number4
    print(f"  {dept} → {unique_name}")

print("========================================")
print("\nThank you for using Haylin's EC2 Name Generator, have a good day!")
