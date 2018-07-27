#program yang membantu translasi dari kalimat surgawi ke duniawi

#variable num_sur adalah variable untuk menyimpan number surgawi atau kalimat surgawi
num_sur = int(input("Masukkkan kalimat surgawi: "))

#variabele num_str adalah variable untuk menyimpan kalimat surgawi yang telah di translasi kan ke kalimat duniawi.
num_str = '' #string kosong untuk nanti di pergunakan untuk menambahkan string string yang terdiri dari B atau P

#jika ternyata yang diinputkan adalah 0 return saja 'P'
if num_sur == 0: 
    print("Makna duniawi: " + "P", end ='')
    
#jika ternyata inputtan lebih dari 0
else:
    while num_sur != 0 : #mengulang operasi dibawah while selama num_sur belum menjadi 0
        sisa = num_sur % 2 #mencari modulo antara kalimat surgawi dibagi dengan 2 dan memasukannya ke variable sisa(remainder)
        num_sur = num_sur // 2 #mencari modulo antara kalimat surgawi dibagi dengan 2 dan mengupdate variable num_sur
        if sisa == 1: 
            num_str = num_str + 'B' #pada saat ternyata sisa bagi nya 1, akan menambah string B pada num_str
            
        elif sisa == 0:
            num_str = num_str + 'P' #pada saat ternyata sisa bagi nya 0, akan menambah string P pada num_str

    num_dun = num_str[::-1] #reverse num_str untuk menjadi kalimat duniawi
    print("Makna duniawi: " + num_dun) #print kalimat duniawi
            

