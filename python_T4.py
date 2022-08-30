"""1. Write a program to reverse a string.
Sample input: “1234abcd”
Expected output: “dcba4321”"""
a="1234abcd"
print(a[::-1])

"""2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters.
Sample input: “abcSdefPghijQkl”
Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12"""
def case(x):
    lower_count=0
    upper_count=0
    for i in x:
        if i.lower()==i:
            lower_count=lower_count+1
        else:
            upper_count=upper_count+1
    print("No of Uppercase characters: ",upper_count)
    print("No of lowercase characters: ",lower_count)


case("abcSdefPghijQkl")

#3.Create a function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 

"""4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically."""


items=[i for i in input("enter your hyphen separated sequence of words: ").split('-')]
items.sort()
print('-'.join(items))

5. Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.
Sample input: Hello world Practice makes man perfect
Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

x="hello world Practice makes man perfect"

def upper_case(x):
    y=x.upper()
    print(y)
upper_case(x)

"""6. Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console."""
def sumfunction(x,y):
    sum=int(x)+int(y)
    print(sum)
sumfunction('4','5')

"""7. Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line."""

def func1(x,y):
    if len(x)>len(y):
        print(x)
    elif len(x)==len(y):
        print(x)
        print(y)
    else:
        print(y)

func3(input("enter first string: "),input("enter a second string: "))


"""8. Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included)."""
x=map(lambda x:x**2,range(1,21))
print(tuple(x))

"""9. Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers.
Sample input: show Numbers(3) (where limit=3)
Expected output:
0 EVEN
1 ODD
2 EVEN
3 ODD"""

def shownumbers(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print(i, " EVEN")
        else:
            print(i," ODD")
shownumbers(int(input("enter a limit value: ")))

"""10. Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)"""
y=filter(lambda x:x%2==0,range(1,21))
print(list(y))

"""11. Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions."""
x=filter(lambda x:x%2==0,map(lambda x:x**2,[1,2,3,4,5,6,7,8,9,10]))
print(list(x))

#12. Write a function to compute 5/0 and use try/except to catch the exceptions
def catcherror():
   x=[5,3,2]
   for i in x:
    try:
     y=i/0
    except ZeroDivisionError:
     print("there was zero divition error")     
catcherror()

#13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce
from operator import concat
x=reduce(lambda x,y:concat(str(x),str(y)),[1,2,3,4,5])
print(x)

"""14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions."""

x=filter(lambda x:x%3!=0 and x%7==0,range(1,71))
print(list(x))

"""15. Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation."""
def multi_list(x):
    x=x*x
    return x
    #return l1


y=map(multi_list,[1,2,3,4,5])
print(list(y))

16. What is the output of the following codes:
def foo():
   try:
    return 1
finally:
    return 2
 k = foo()
print(k)
#output=2

def a():
  try:
   f(x, 4)
  finally:
   print('after f')
   print('after f?')
a()
#output=name error 'f' is not defined