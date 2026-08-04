num=int(input("enter number : "))

try:
    with(open("tables.txt","a") as f1):

        table=[f"{num} X {i} = {num*i}\n" for i in range(1,11)]
        for i in table:
             f1.write(i)

except Exception as e:
      print(e)