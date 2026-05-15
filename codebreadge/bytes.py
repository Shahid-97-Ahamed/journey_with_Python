# bytes uses for img related its range(0,256) and its value not changable
numbers =[1,11,2,145,22,35,45,255]#256 is not acceptable because its index number is 257
convert_bytes =bytes(numbers)
# print(type(convert_bytes))

# bytearray is same as a bytes but little bit have a change bytes value is not changable and bytearray value is changable


number =[11,54,115,22,33,25,65,255]
convert_bytesarray=bytearray(number)
number[3]=333#its change  index 3 number 115 to 333
print(number)