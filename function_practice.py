def hello():
    print("Hellow welcome to your file!")

def pack(a, b, c):
    return [a, b, c]
    

def eat_lunch(my_list):
  if len(my_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_list)):
      if i == 0:
        print(f"First I eat {my_list[0]}")
      else:
        print(f"Next I eat {my_list[i]}")


hello()
print(pack(3, 4, 5))
eat_lunch(["banana", "sandwich", "pudding"])
eat_lunch([])
