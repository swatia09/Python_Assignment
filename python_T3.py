#1. Create a list of 10 elements of four different data types like int, string, complex and float.
l = [23, 2345,557,'hello world','abd','hello python',3.45,2.345,2+3j, 4+3k]
print(l)

#2. Create a list of size 5 and execute the slicing structure
l = [1,2,3,4,5,6,7,8,9]
print(l[3:6])

#3. Write a program to get the sum and multiply of all the items in a given list.
l = [1,2,3,4,5,6,7,8,9]
print(sum(l))
l1=[]

for i in l:
   l1.append(i*i)
print(l1)

#4. Find the largest and smallest number from a given list.
l = [1,2,3,4,5,6,7,8,9]
print(min(l))
print(max(l))

"""5. Create a new list which contains the specified numbers after removing the even numbers from a
predefined list."""
l = [1,2,3,4,5,6,7,8,9]
x=[i for i in l if i%2!=0]
print(x) 
#or
l = [1,2,3,4,5,6,7,8,9]
y=[]
for i in l:
   if i%2!=0:
     y.append(i)
print(y)

"""6. Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and30 (both included)."""
list=[]
for i in range(1,31):
   if i<=5 or i>=25:
     list.append(i*i)
print(list)

"""7. Write a program to replace the last element in a list with another list.
Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]"""
a= [1,3,5,7,9,10]
b= [2,4,6,8]
a.pop(-1)
c=a+b 
print(c)

"""8. Create a new dictionary by concatenating the following two dictionaries:
Sample input: a={1:10,2:20} b={3:30,4:40}
Expected output: {1:10,2:20,3:30,4:40}"""
a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)

"""9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).
Sample input: n=5
Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}"""
x={}
n=5
for i in range(1,n+1):
   x.update({i:i**2})
print(x)
#or
n=5
x={i:i**2 for i in range(1,n+1) if n==5}
print (x)

"""10. Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)"""
x=input("enter a comma separated values: ")
l1=x.split(',')
t1=tuple(l1)
print("list: ",l1)
print("tuple: ",t1)
