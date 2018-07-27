from __future__ import print_function

#lab01_D_YE_MuhammadFachryNataprawira_1706039704_pertarungan2
#

def main():
    #input biaya pernikahan dengan nama variable uang
    
    uang = input("Masukkan biaya pernikahan: Rp ")
    uang = int(uang)
    gaji = 500000 #gaji per hari
    thn = 336 #jumlah hari dalam satu tahun
    bln = 28 #jumlah hari dalam satu bulan
    mg = 7 #jumlah hari dalam satu minggu
    hr = 1 #jumlah hari dalam satu hari

    #membagi uang yang didapatkan dengan gaji per hari nya
    bagian = uang//gaji

    #mendapatkan jumlah tahun dan mendapatkan sisa hari nya
    tahun = bagian//thn
    sisa = bagian%thn

    #mendapatkan jumlah bulan dan mendapatkan sisa hari nya
    bulan = sisa//bln
    sisa = sisa%bln

    #mendapatkan jumlah minggu dan mendapatkan sisa hari nya
    minggu = sisa//mg
    sisa = sisa%mg

    #mendapatkan jumlah hari dan mendapatkan sisa hari nya
    hari = sisa//hr
    sisa = sisa%hr   
    
    print("Anda harus bekerja selama ", tahun," tahun ", bulan, " bulan ", minggu," minggu", hari, " hari untuk memenuhi biaya pernikahan.")

if __name__ == "__main__" :
    main()
