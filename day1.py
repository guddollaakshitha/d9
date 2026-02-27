print(25)

print("hello world")

x=25    #assigning     
x="hello"  #reassigning

print(x)

#variable name can start with A-Z,a-z,_ but not with digit and any other special character
#variable names are case sensitive
#should not contain any spaces
#should not use keywords as a variable names
#meaningful variable
#then normal names like x1,y1
#python will change the type of the variable as per the value we assigened
#so python can be considered as a dynamically typed language



student_name_1="vaishnavi"
student_name_2="amshika"            #string
student_name_3="prajwala"


student_1_roll_no=25
student_2_roll_no=26                  #integer 
student_3_roll_no=27
print(type(student_3_roll_no))    #if we want to know the type of variable  in pythonwe can use type() function


student_3_roll_no="five"          #the type will automatically as per assigined value.
print(type(student_3_roll_no))

student_aggregate_1=9.5
student_aggregate_2=9.2               #float
student_aggregate_3=9.6

# till now programmer was assignied the values
# now lets assign the by the user.


user_name=input("enter your name: ")   
print(user_name)
print(type(user_name))          #by default input function will consider the value as string



first_name=int(input("enter the first_name:"))
last_name=int(input("enter the last_name:"))
print(first_name)
print(last_name)

print(first_name+last_name)     #here "+" is used to add
print(first_name*last_name)     #here "*" is used to multiply
#print(first_name-last_name)     #here "-" is used to subtract


# if we use only "int" we get error 


value1=float(input("enter the first value:"))
value2=int(input("enter the second value:"))
print(value1)
print(value2)
print(value1+value2)        #here "+" is used to concatenate



a=5
b=10
c=a+b
print(type(c))


# string()--> float/int to string
# int()--> float/string to int
# float()--> float to string
#boolean()--> bool values(True/False)

#x=5-->T
#X=-5-->T
#x=0-->F
#x=""-->F
#x="hello"-->T
#X=" " -->T




                                          # DAY-1 VARIABLE END 