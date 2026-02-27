#by default function will return none values.

def sample():
    print('hello')
    return'something'
print('welcome')  #ignored

print(sample())


def sample1():#assigned function call to x
  #  print(x)

    def sample2():
        return 'i am sample2'
    
    x=sample2 #assigned function name/defination to x.
    print(x()) 

    def sample3():
        print('hello samples3')
        return 'byee'
        print('hhhhhhhhh')
    y=sample3

    print(y)
    y()
    print(y()) 

    #we can assign a function to a variable
    # #a function defination canbe taken as values inside the data structure like list/tuples.
    # a function which can pass as argument into another function,then that can be called as callback function.
    #a function which will take another function as arrgumrnt or return another function then it can be called as  higher order function.
    # because of above 4 points ---> function in python can be considerd as a first class function.


def fun1():
    print('iam function 1 ')
def fun2():
    print('i am function 2')

list1=[fun1,fun2]
list[0] ()
list[1] ()

def fun3():
    print('i am a function 3')
    return fun2()
fun3()
def fun4():
    return 'i am function 4'

def fun5(cdf):
    print(cdf())
    return 'i am function 5'
print(fun5(fun4))
 


 #where fun 4 is going as arugument into the func 5
 #fun5 is taking fun4 as an arugument

 #we can also define a function without name
 # a fun without name can be called as anonymous function
 #to define anonoymous func in python we have to use limited key words
 #for short logical problms line of codes ,we can use lamda function.
 #by default it will return values without using return keyword



#syntax  # functions1 = lamda param:logic


def sample():
    return"hello"
print(sample())


#lamda function without params
fun2=lambda:'hello'
print(fun2())


#lamdba function with single param
fun3=lambda x:x
print(fun3(10))


#lamdba function with multiple params
fun4=lambda x,y:x+y
print(fun4(4,5))
fun6=lambda *x:x[0]*x[1]+x[2]
print(fun6(1,2,3))

fun7=lambda  **x:x
print(fun7(first=4,second=5,third=6))

"""
recursive function
function being called by itself on a particular condition is called recursive process.
and that function can be called recursive function
1.default params
2.posoitional argms
3.arbitary argms
4.keyword aribitary
5.keyword argms
6.higer order
7.callback
8.anonymous using lambda
9.recursive function
"""




num=345

def reserve():
    rev=0
    if num<0:
        num=num*-1
        num1=num
        while num!=0:
            id=num%10
            rev=rev*10+id
            num=num//10
        print(rev) 
        reserve(234)
        reserve(345)


      # write a function to add 3 numbers 



def addition(a,b,c):
    return a+b+c
print(addition(1,2,3))
print(addition(4,5,6)) 



# write a function to print multiple table of given input

def m_table(num):
    for x in range(1,11):
        print(f"{num}*{x}={num*x}")
    return f'{num}table printed'
print(m_table(4)) 


# write a function to print numbers for given range 
def numbers(x1,x2):
    for i in range(x1,x2):
        print(i)
numbers(20,31) 
numbers(23,34)
numbers(34.56)       