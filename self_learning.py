# # # # # # First Program
# # # # # # print("Hello, World!")
# # # # # # print("I am a Python programmer now 🎉")

# # # # # # Comments

# # # # # name       = "Alice"    # string
# # # # # age        = 25         # integer
# # # # # height     = 5.6        # float
# # # # # is_student = True      # boolean
# # # # # nothing    = None      # null value


# # # # # # Multiple assignment
# # # # # x, y, z = 1, 2, 3

# # # # # # Same value to multiple vars
# # # # # a = b = c = 0

# # # # # # print(name,age,height)

# # # # # x = 42
# # # # # # print(type(x))  
# # # # # # print(isinstance(x, int))  

# # # # # # b2  = bool(21245) 
# # # # # # print(b2)

# # # # # # lis =list("abc")
# # # # # # print(lis)

# # # # # x =10
# # # # # x = x/4
# # # # # # print(x)

# # # # # # print("Ha" * 3)             # HaHaHa
# # # # # # print("Hello" + " World")   # Hello World

# # # # # # String Indexing & Slicing
# # # # # # s = "Python"
# # # # # #    P  y  t  h  o  n
# # # # # #    0  1  2  3  4  5   forward
# # # # # #   -6 -5 -4 -3 -2 -1   backward
# # # # # # print(s[0])      # P      first char
# # # # # # print(s[-1])     # n      last char
# # # # # # print(s[1:4])    # yth    index 1,2,3
# # # # # # print(s[:3])     # Pyt    start to 2
# # # # # # print(s[3:])     # hon    3 to end
# # # # # # print(s[::-1])   # nohtyP reversed!


# # # # s = "   Hello World"
# # # # print(s.endswith(" "))

# # # name, age = "Ravi", 21

# # # # # % formatting (old)
# # # # print("Name: %s, Age: %d" % (name, age))

# # # # .format()
# # # print("Name: {}, Age: {}".format(name, age))

# # price = float(input("Enter price: ₹"))
# # print(f"With 18% GST: ₹{price*1.18:.2f}")

# print("Hello",end="")
# print("hshjkhfjsdjfjsjdjfsd,mvndbvhksdhfkvsdhjfvjsdjjfgvlisej")
# print("gfdhfhb",end="")
# print("3636936")

# print("Line1\nLine2")
# print("Tab:\there") 
# print("She said \"hi\"")  

# Project Calculator

a =float(input("first number: "))
op =input("Operation(+,-,*,/): ")
b =float(input("second number: "))


if op =="+":
    print(f"Result:{a+b}")
elif op =="-":
    print(f"Result:{a-b}")
elif op == "*":
    print(f"Result:{a*b}")
elif op =="/":
    if b !=0:
        print(f"Result:{a/b:.2f}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid Oparator")