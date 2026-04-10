arquivo=open("even  or odd.py","w")
par=False
num=0
arquivo.write("number=int(input('Enter a number: '))\n")
while num<=10000000:
    if par==False:
        arquivo.write(f"if {num}==number:\n")
        arquivo.write("    print('even is True')\n")
        par=True
    else:
        arquivo.write(f"if {num}==number:\n")
        arquivo.write("    print('even is False')\n")
        par=False
    num+=1
arquivo.close()
