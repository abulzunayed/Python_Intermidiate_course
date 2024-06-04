print(1 + 3)
print('hello' + 'world')
print('hello', 'world')
print('hello "hi')
print('I\'m 5')
print(4 ** 2)
# for loop
x = [1, 3, 2, 4, 10, 5, 7, 6, 8, 9]
# for y in x:
#     print(y)
# rang for loop( from  start value to upto range value without last value) not index value
for y in range(3, 7):
    print(y)
# if statement:
x = 3
y = 4
z = 10
if x > y:
    print('y is less')
if x > z:
    print('z is big')
elif z > y:
    print('y is big')
else:
    print('x is less')


# function declaration
z=6
def sum(a, b):  # or  def sum():
    x = a  # x=4
    y = b  # 3
    print(x + y+z)
sum(2, 4)

# writing file
write= 'hello'
savefile= open('tse.txt', 'w')
savefile.write(write)
savefile.close()
# reading the file
readfile=open('tse.txt', 'r').read()
print(readfile)
# classse write

class cal:
    def add(x, y):
        ans=x+y
        print(ans)
    def sub(x, y):
        ans=x-y
        print(ans)
    def mul(x, y):
        ans=x*y
        print(ans)
cal.add(2,4)
cal.sub(7,2)
cal.mul(3,2)

# take imput from user
name= input("please enter your name?:")
print('hello', name)

#   import statastic module for use of mean function
import statistics
x=[1,3, 5, 6, 4, 5,]
y= statistics.mean(x)
y2= statistics.median(x)
y3= statistics.mode(x)
y4= statistics.stdev(x)
print(y)

# import Syntax as from module
import statistics as s
x=[1,3, 5, 6, 4, 5,]
y= s.mean(x)
print(y)
# another way: import Syntax as from module by directly call the function
# this technique is best for  less processing time

from statistics import mean, stdev
x=[1,3, 5, 6, 4, 5,6]
y= s.mean(x)
print(y)
# or
print(mean(x))
print(stdev(x))

from statistics import mean as m, stdev as s
x=[1,3, 5, 6, 4, 5,6]
print(m(x))
print(s(x))

# create module and call from different file
import moduletest
moduletest.module( ' show the moduel internal data') # this function calling from anther mouletset.py file

# exceptio nad try to accept
try:
    print('ist iam running')
    print('5'+ 5)
except Exception as e:
    print(str(e))
    print(' after exception runinng rest code')
print(' then exception runinng last rest code')

#  use of List vs Tuple and list manipulation

def example():
    return 15,19
a, b = example()   # this is Tuples
print(a)
print(b)
x=[1,2,3,4]    # this is list
print(x)
print(x[3])
x.append(12)  # do append
x.insert(2,0)   # in the insert function, 1st index indicates the position of list and 2nd index indicate the value of insert
print(x)
x.remove(4)
x.count(2)  #  count indicate how many time 2 is in the list
x.index(3)
x. sort()  # sort the list
x.reverse()  # reverse the list

# Dictionary use
garde= {'kely': 89, 'jack':99,  'math':97}
print(garde)      # print all value
print(garde['jack'])       # print only jack value
garde['jack']= 65       # the change jack value
del garde['kely']       # the delete kely value
garde= {'kely': 89, 'jack':[99,87], 'math':[78,65]}  # multiple value in single element