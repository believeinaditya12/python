# print hello world
print('Hello World')
character_name = "John"
character_age = "35"
print("There once was a man named "+character_name+",")
name = input("What is your name?")
print(name)
old_age = input("enter your old age : ")

# # here it is considering old age as the string so it will considering the old age as the string so use int(old_age)
new_age = int(old_age)+2
print(new_age)
number = 18
print(float(18))

# print the sum of the two numbers
first = input("Enter the first number")
second = input("Enter the seccond number")
# here first and second are string so concatenation will be happened so to get sum use typecasting
sum = first + second 
sum2 = int(first)+int(second)
print(sum)
print(sum2)

# string operations
name = "Tony Stark"
print(name.find('Stark'))
print(name.replace("Stark", "Ironman"))
print(name)
# is T present in the name or not
print('T' in name)


# print according to the age
age = 19
# in python we use : not braces
if age>=18 :
    print("You are an adult")
    print("You can vote")
elif age<18 and age>3 :
    print("You are in school")
else:
    print("You are a child")
print("thank you")   
 
# print the numbers
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5%2)
print(5 ** 2)
i = 5
i = i+2
i += 2
i -= 2

# number operators
first = input("enter the first number :")
operator =input("enter the operator(+,-,*,/,%) :")
second = input("enter the second number :")
if operator == "+":
    print(first+second)
# print score 
marks = [95, 98, 97,"maths"]
print(marks[0])

for score in marks:
    print(score )
# print marks    
marks = (98,97,95,95,95)
print(marks.count(95))
print(marks.index(97))
person = "ram", "shyam", "abhi"
print(person)


