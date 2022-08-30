"""1. Write a program in Python to find out the character in a string which is uppercase using list
comprehension."""
x="HELlo Python"
print(x)
res= list(filter(lambda c:c.isupper(),x))
print(res)


"""2.Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
HINT - Use Zip function also
Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}"""
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
y={i:j for i,j in zip (students,subjects)}
print (y)

#3. Learn More about Yield, next and Generators

"""4. Write a program in Python using generators to reverse the string.
Input String = “Consultadd Training”"""
def rev_str(my_str):
   length= len(my_str)
   for i in range (length -1,-1,-1):
      yield my_str[i]

for i in rev_str("hello python"):
    print(list(i))

"""5. Write an example on decorators."""
def add_value(x):
   def adder(y):
     return x+y
   return adder 
add_15 = add_value(15)
print(add_15(10))