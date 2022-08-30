"""1. Write a program in Python to allow the error of syntax to be handled using exception handling.
HINT: Use SyntaxError"""
try:
    x=true
    print(x)
except Exception as e:
    print("syntax error as occur") 

"""2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode."""
import sys
f=open("file1.txt",'r')

while True:
  try:
    f=open("xyz.txt" ,'r')
  except Exception as e:
        print('Access denied. Try again.',e)
        print("please enter file name again")
        break
f.close()



"""3. Write a program to handle an error if the user entered a number more than four digits it should
return “The length is too short/long !!! Please provide only four digits”"""
while True:
    n = int(input('4-digit number: '))
    if n in range(1000, 10000):
       break
    else:
           print("the length is too long/short!!! Please provide only four digits")

"""4. Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times."""

print('Enter correct username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Hytu76E' and username=='bank worker':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1

"""6. Read doc.txt file using Python File handling concept and return only the even length string from
the file. Consider the content of doc.txt as given below:
Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in The same link as it is present."""
f=open ("abc.txt",'x') 
f=open ("abc.txt",'w')
f.write("Hello I am a file"+ '\n')
f.write("Where you need to return the data string" +'\n')
f.write("Which is of even length\n")
f.write("Make sure you return the content in The same link as it is present" +'\n')
f=open ("abc.txt",'r')

for row in f:
   x=len(row)
   if x%2==0:
     print(row)
   else:
     pass
f.close()