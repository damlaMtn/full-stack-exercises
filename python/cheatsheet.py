marks = 90
attendance_percentage = 87

if marks >= 80 and attendance_percentage >= 85:
    print("qualify for honors")
else:
    print("Not qualified for honors")

#----------------------------------

class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age

#----------------------------------

def greet(name): print("Hello,", name)

#----------------------------------

5 == 5 
age = 25 
age == 30 

#----------------------------------

for num in range(1, 10): 
    print(num)

fruits = ["apple", "banana", "orange", "grape", "kiwi"] 
for fruit in fruits:
    print(fruit)

#----------------------------------

greet("Alice")

#----------------------------------

5 >= 5 and 9 >= 5 
quantity = 105 
minimum = 100 
quantity >= minimum 

#----------------------------------

age = 20 
max_age = 25 
age > max_age 

#----------------------------------

temperature = 35
if temperature > 30: 
    print("It's a hot day!")

#----------------------------------

score = 85  # Example score
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B.")
else:
    print("You need to work harder.")

# Output = You got a B.

#----------------------------------

if age >= 18:
    print("You're an adult.")
else:
    print("You're not an adult yet.")

#----------------------------------

5 <= 5 and 3 <= 5 
size = 38 
max_size = 40 
size <= max_size 

#----------------------------------

4 < 6 
score = 60 
passing_score = 65 
score < passing_score 

#----------------------------------

for num in range(1, 6):
    if num == 3:
        break
    print(num)

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

#----------------------------------

#!isLocked

#----------------------------------

a = 10 
b = 20 
a != b 

count=0 
count != 0 

#----------------------------------

person1 = Person("Alice", 25)

#----------------------------------

"Farewell Party Invitation" 
Grade = 12 
Grade == 11 or Grade == 12 

#----------------------------------

range(5) #generates a sequence of integers from 0 to 4. 
range(2, 10) #generates a sequence of integers from 2 to 9. 
range(1, 11, 2) #generates odd integers from 1 to 9.

#----------------------------------

def add(a, b): return a + b 
result = add(3, 5)

#----------------------------------

try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("Invalid input. Please enter a valid number.")

#----------------------------------

try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("Invalid input. Please enter a valid number") 
else: 
    print("You entered:", num)

#----------------------------------

try: 
    file = open("data.txt", "r") 
    data = file.read() 
except FileNotFoundError: 
    print("File not found.") 
finally: 
    file.close()

#----------------------------------

count = 0 
while count < 5: 
    print(count) 
    count += 1