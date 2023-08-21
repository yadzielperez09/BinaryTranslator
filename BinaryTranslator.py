def menu(): #this function was created to print the menu
    print("\n####################################################")
    print("Welcome to the binary translator,select an option:")
    print("    1. Binary to text")
    print("    2. Text to binary")
    print("    3. Exit")
    print("####################################################\n")

dabc={'a': '01100001','b':'01100010','c':'01100011','d':'01100100','e':'01100101','f':'01100110','g':'01100111','h':'01101000','i':'01101001','j':'01101010','k':'01101011','l':'01101100','m':'01101101','n':'01101110','o':'01101111','p':'01110000','q':'01110001','r':'01110010','s':'01110011','t':'01110100','u':'01110101','v':'01110110','w':'01110111','x':'011110000','y':'01111001','z':'01111010'}
dABC={'A': '01000001','B':'01000010','C':'01000011','D':'01000100','E':'01000101','F':'01000110','G':'01000111','H':'01001000','I':'01001001','J':'01001010','K':'01001011','L':'01001100','M':'01001101','N':'01001110','O':'01001111','P':'01010000','Q':'01010001','R':'01010010','S':'01010011','T':'01010100','U':'01010101','V':'01010110','W':'01010111','X':'010110000','Y':'01011001','Z':'01011010'}
dsimb={' ':'00100000','!':'00100001','"':'001000010','#':'00100011','$':'00100100','%':'00100101','&':'00100110',"'":'00100111','(':'00101000',')':'00101001','*':'00101010','+':'00101011',',':'00101100','-':'00101101','.':'00101110','/':'00101111',':':'00111010',';':'00111011','<':'00111100','=':'00111101','>':'00111110','?':'00111111','@':'01000000','[':'01011011',']':'01011101','ˆ':'01011110','_':'01011111','{':'01111011','|':'01111100','}':'01111101','˜':'01111110'}
dnums={'0':'00110000','1':'00110001','2':'00110010','3':'00110011','4':'00110100','5':'00110101','6':'00110110','7':'00110111','8':'00111000','9':'00111001'}
done = False

while not done:
    menu() 
    uOp= int(input("Enter option: "))
    if uOp== 1:
        print('REMINDER!!!!!')
        print('You have to write 8 digits being 1 or 0, if you want the letter to be a lower letter start with 011')
        print('if you want it to be upper start with 010')
        print('Make sure to let an space between the 8 digits or /')
        b=input("Write your binary:")
        bt=b.split()
        print(bt)
        s=''
        for i in bt:
            x=0
            y=0
            if len(i)<7:
                print('Invalid binary')
                break
            if i in list(dnums.values()):
                v=list(dnums.values()).index(i)
                k=list(dnums.keys())[v]
                s+=k
            elif i in list(dsimb.values()):
                v=list(dsimb.values()).index(i)
                k=list(dsimb.keys())[v]
                s+=k
            elif i in list(dabc.values()):
                v=list(dabc.values()).index(i)
                k=list(dabc.keys())[v]
                s+=k
            else:
                v=list(dABC.values()).index(i)
                k=list(dABC.keys())[v]
                s+=k
        print("\n####################################################")
        print(f'Your binary in text: {s}')
        print("####################################################\n")
    elif uOp == 2:
        b=""
        t=input('Write your text ')
        print(t)
        for i in t:
            if(i.isalpha()==True and i.islower()==True):
                for k,v in dabc.items():
                    if k in i:
                        b+=v
                        b+=" "
            elif(i.isalpha()==True and i.islower()==False):
                for k,v in dABC.items():
                    if k in i:
                        b+=v
                        b+=" "
            elif(i.isdigit()==True):
                for k,v in dnums.items():
                    if k in i:
                        b+=v
                        b+=" "
            else:
                for k,v in dsimb.items():
                    if k in i:
                        b+=v
                        b+=" "
        print("\n####################################################")
        print(f'Your binary in text: {b}')
        print("####################################################\n")
        
    elif uOp ==  3:
        print('Thanks for using the binary translator')
        done = True
    else:
        print("Invalid option, try again.")
        
