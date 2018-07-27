from __future__ import print_function
import turtle

#lab01_D_YE_MuhammadFachryNataprawira_1706039704_pertarungan1
#membuat tangga dengan panjang input user

def main():

    #inisiasi turtle dengan t
    t = turtle.Turtle()
    
    #meminta input user untuk menentukan panjang sisi tangga
    panjang = input(" Masukkan panjang setiap anak tangga: ")
    panjang = int(panjang)
    t.pendown()

    #kode dibawah untuk membentuk awal garis kuning
    #dengan menggambar keatas lalu kekanan
    t.color("yellow")
    t.left(90)
    t.forward(panjang)
    t.right(90)
    t.forward(panjang)
    
    #kode dibawah untuk membentuk garis biru
    #dengan menggambar keatas lalu kekanan
    t.color("blue")
    t.left(90)
    t.forward(panjang)
    t.right(90)
    t.forward(panjang)

    #kode dibawah untuk membentuk garis merah
    #dengan menggambar keatas lalu kekanan
    t.color("red")
    t.left(90)
    t.forward(panjang)
    t.right(90)
    t.forward(panjang)

    #kode dibawah untuk membentuk garis hijau
    #untuk menutup tangga supaya terbentuk tangga yang utuh
    t.color("green")
    t.right(90) #belok 90 derajat
    t.forward(3*panjang)
    t.right(90)
    t.forward(3*panjang)

if __name__ == "__main__":
    main()

    
