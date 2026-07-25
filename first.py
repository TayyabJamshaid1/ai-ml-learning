print("""Hello World!
kesq
eee
""")

b=3>5
print(b)

b= True or False
print(b)

b=False and False
print(b)

b=not(True)
print(b)

a = 31
check=type(a)
print(check)  #output: <class 'int'>

a = 31.4
check=type(a)
print(check)  #output: <class 'float'>

a = "Hello"
check=type(a)
print(check)  #output: <class 'str'>

d="31.4"
f=float(d)
print(f)  #output: 31.4

d="31"
f=int(d)
print(f)  #output: 31

d=78
j=str(d)
print(j)  #output: 78 as string


# b=input("Enter a number: ")
# v=input("Enter another number: ")
# sum=int(b)+int(v) #by default input() function takes input as string, so we need to convert it into integer using int() function
# print("The sum of the two numbers is: ",sum)


# q=input("Enter a number: ")
# w=input("Enter another number: ")
# e=int(q)%int(w)
# print("the remainder is ",e)



data={
    "kursi":"chair",
    "billi":"Cat",
    "larka":"boy"
}

friends=["apple","grapes",23,False,12.3]
user=input("Enter user name ")

if (user in friends):
    print("username exist in array")

else :
    print("username does not exist in array")    


