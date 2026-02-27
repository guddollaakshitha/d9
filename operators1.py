"""

operators:

an operator is a symbol which tells python to perform the operator values.

1.ARITHMETIC OPERATOR:
+,-,*,/,//,%,**
2.ASSIGNMENT OPERATOR:
=,+=,-=,*=,|=,%=,**=
 3.COMPARISION (RELATIONAL) OPERATOR:
==,!=,>,<,>=,<=
4.logical operators:
when we want to compare /check multiple conditions .alwalys returns boolean values
and, or, not 
5.membership operator:
in,not in---->returns boolean values used to check presences of value in
starting,list,tuple,dictionary.
6.identify operator---> is is not ---> to compare two values based on the value and their memory adress
python uses same memory object for numbers within range of -5 to 256.

7.bitwise operator
"""

print(2+2)
print(2.5+3.6)
print((4+5j)+(3+8j))
print("hello"+"world")

#print(3+"hi") #unsupported operand


print([1,2,3]+[4,5,7])
print((1,4,7)+(2,5,8))
#print({1,4}+{2,6}) # not supported
#print({"name":"akshi"}+{"city":"hyd"})#not supported



#print(True+12)=13
#print(False+2)

#print(True+True)
#print(True+False)

#print(none+none)#not supported
#print(true+"hello")#not supported


#print("hello"-"world")#not supported
#print([1,5,7]-[2,6,8])#not supported


print((2+5j)*(3+2j))#not supported

print("hello"*"hello")#not supported


print("hello"*3)
print("hello**3.5")


print([1,2,4]*[3,5,6])#unsupported
print([1,2,3,]*4)
#print((1,3)*2)
#print({1,3}*2) #unsupported


print((4+5j)/2)
print((4+6j)/(4+8j))

#print([1,2,3]/[1,2,4])#unsuppotred
#print([1,2,3]/3) #unsupported.


#print(10//3)
#print(10%40)


print(3**3)
#print("hello"**3)
#print([1,2,,3]**2)


#x=5
#print(x)


#x/=2
#print(x)

#srri="hello"


#print(list1)
#set1=(4,5,6)
#set1={4,6}
#print(set1)


#print([1,2,3])==[1,4,6]

#if any value except zero treat as a truth Value
#zero,"'" ,[],none,{}can be treat as a falsy ValueError


print(True and True)
print(False and True)
print(True or True)
print(False and"")
print("" and True)
print(True and "")
print(True and 2)
print(True and -2)
print(False and 0)
print(False and [])

print([] or[1,2,3])
print([1,5,6] and [1,2,3])


#ip2
#list=[1,2,3,4,]
#print(ip in list1)
#students_name='akshitha'
#students=('rithish','bunny','manu','nithya','nidhi','kanna','julie','sunny')
#print(students_name not in students)


dict1={"name":"akshitha","city":"hyd","age":21,"gender":"male"}

print("akshitha" not in dict1)



#str="something"
#char='e'
#print(char not in str)


#optimization...??


# x=5
#y=6
#z=30
#a=4
#b=34
#c=4


x=12
y=12

print(x is y)
