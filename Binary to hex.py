#Binary to Hex
import time
while True:
    print("Welcome to the Binary to Hex calculator!")
    binary = input("Enter an 8 bit binary string: ")
    time.sleep(2)
    bit1 = int(binary[0])*8
    bit2 = int(binary[1])*4
    bit3 = int(binary[2])*2
    bit4 = int(binary[3])*1
    bit5 = int(binary[4])*8
    bit6 = int(binary[5])*4
    bit7 = int(binary[6])*2
    bit8 = int(binary[7])*1
    total = bit1 + bit2 + bit3 + bit4 + bit5 + bit6 + bit7 + bit8
    if total > 15:
        hex2 = int(total / 16)
        hex1 = total % 16
    else:
        hex1 = total % 15
    if hex1 == 10:
        hex1 = ("A")
    elif hex1 == 11:
        hex1 = ("B")
    elif hex1 == 12:
        hex1 = ("C")
    elif hex1 == 13:
        hex1 = ("D")
    elif hex1 == 14:
        hex1 = ("E")
    elif hex1 == 15:
        hex1 = ("F")
    else:
        hex1 = hex1
    print("Your binary total is", total)
    time.sleep(2)
    print("Your hex total is", hex2, hex1)
    time.sleep(1)
    print("")
    print("")
