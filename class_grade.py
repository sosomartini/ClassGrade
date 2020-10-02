



""" Plain English
start
create list to store 5 number (float)
each time we capture the user input, we append the number to the list 
once we have three highest number in the list, we sum them up and divide by 3
output a message to the user
end
"""

""" psuedocode
create list 

capture input 
appendnumber to list 

create input
append number to list

create input
append number to list 

create input
append number to list 

create input
append number to list 

sort the list, then splice out the two lowest number
print message to user
"""

grades =[]

grade = input("Enter the 1st grade")
grades.append(float(grade))

grade = input("Enter the 2nd grade")
grades.append(float(grade))

grade = input("Enter the 3rd grade")
grades.append(float(grade))

grade = input("Enter the 4th grade")
grades.append(float(grade))

grade = input("Enter the 5th grade")
grades.append(float(grade))

grades.sort()
grades = grades[2:]
grades = sum(grades)
result = grades / 3

print("Average Grade {0:.2f}%".format (result))