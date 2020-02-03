import os
# Allows system commands (e.g. os.exit)
answer = input("What calculator would you want? Type 'one()' for 'Binary To Dinary!', 'Two()' for 'Denary To Binary!' or 'Three()' for 'Binary To Hex!": ")
#Asks for an input 

def One():
    binary = input("Input a number in binary: ")  
    denary = 0  
    for digit in binary:  
      denary = denary*2 + int(digit)
      if denary < 255:
          print("ERROR: MORE THAN 8 BITS!")
          os.exit()
      else:
          print("Your denary number is: " + str(denary))  


def Two():
    denary = int(input("Input a denary number: "))
    if denary > 255:
        print("ERROR! 8 BITS CANNOT BE ABOVE 255!")
        os.exit()
    else:
        binary=""  
        while denary>0:   
          binary = str(denary%2) + binary  
          denary = denary//2
        print("Your binary number is: " + binary)  


def Three():
    while True:
        binary = input("Enter an 8 bit binary string: ")
        bit1 = int(binary[0])*8
        bit2 = int(binary[1])*4
        bit3 = int(binary[2])*2
        bit4 = int(binary[3])*1
        bit5 = int(binary[4])*8
        bit6 = int(binary[5])*4
        bit7 = int(binary[6])*2
        bit8 = int(binary[7])*1
