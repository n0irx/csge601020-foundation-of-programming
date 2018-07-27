import string
#mendapatkan input dari user
myInput = input("Masukan Operasi: ") 

#myList mengandung key dan kalimat
myList =[]
myList = myInput.split(' ', 1)
 
#memasukan key ke variable
key = myList[0]
key = int(key)
#karena key sudah dimasukan, hapus list index 0
myList.pop(0)

print("Kalimat aslinya adalah: ", end='')

#convert list ke string
myString = str(myList[0])
myString = myString.lower() #agar uppercase jadi lower
for i in myString:
    if i == ' ':
        print(' ', end="") #skip transformasi dari space
    elif ord(i) - key < 97: 
        print(chr(ord(i)-key+26), end="") #saat index kurang dari a
    else:
        print(chr(ord(i) - key), end="") #saat normal


    
