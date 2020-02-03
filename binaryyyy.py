import os
import time
number = int (input("Enter the NUMERO: "))
# ASKING FOR NUMBER
binary = []
#Binary Variable
while number != 0 :
    if number % 2 == 0:
        number = number / 2
        binary.insert(0,0)
    else:
        number = (number - 1) / 2
#Checks if number is 0 or 1

print(binary)
#Prints the binary code

binary = input("ENTER BINARY STRINGOOO (needs to be over 8 digits, if you arent sure just keep adding them the script will only use the first 8): ")
bit1 = int(binary[1]) * 128
if bit1 == "":
    print("RETRY")
    time.sleep(3)
bit2 = int(binary[2]) * 64
if bit2 == "":
    print("RETRY")
    time.sleep(3)
bit3 = int(binary[3]) * 32
if bit3 == "":
    print("RETRY")
    time.sleep(3)
bit4 = int(binary[4]) * 16
if bit4 == "":
    print("RETRY")
    time.sleep(3)
bit5 = int(binary[5]) * 8
if bit5 == "":
    print("RETRY")
    time.sleep(3)
bit6 = int(binary[6]) * 4
if bit6 == "":
    print("RETRY")
    time.sleep(3)
bit7 = int(binary[7]) * 2
if bit7 == "":
    print("RETRY")
    time.sleep(3)
bit8 = int(binary[8]) * 1
if bit8 == "":
    print("RETRY")
    time.sleep(3)
bit9 = int(binary) * 1
bit10 = int(binary) * 1
bit11 = int(binary) * 1
bit12 = int(binary) * 1
bit13 = int(binary) * 1
bit14 = int(binary) * 1

#Registers each bit
total = bit1 + bit2 + bit3 + bit4 + bit5 + bit6 + bit7 + bit8
if total == total > bit1 + bit2 + bit3 + bit4 + bit5 + bit6 + bit7 + bit8:
    print("ERROR!")
else:
    print(total)
    print("THIS IS THE TOTAL YOU DID IT :D")
#Prints the total

