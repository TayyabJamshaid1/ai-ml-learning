e={}
for i in range(1,5):
     while True:
            num1=input(f"Enter user name {i} : ")
            if num1 in e:
                  print(f"❌ '{num1}' already exists! Please enter a different name.")
            else:
                  break

     num2=input("Enter his language : ")
     e.update({num1:num2})

print(e)


