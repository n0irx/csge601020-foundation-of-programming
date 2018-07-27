import random
import turtle

#initialize turtle dan screen
t = turtle.Turtle()
s = turtle.Screen()
t.hideturtle()
s.screensize(2000, 2000)

#variable yang menyimpan banyak kotak, pixel kotak, dan banyak petals
rows = int(turtle.numinput("Colorful chessboard", "Enter the number of rows:", minval=2, maxval=25))
pixels = int(turtle.numinput("Colorful chessboard", "Enter the square size (pixels):", minval=1))
petals = int(turtle.numinput("Colorful chessboard", "Enter the number of petals of the flower:", minval=1))

#konfigurasi turtle agar cepat bergerak dan menuju pada koordinat yang diinginkan
t.speed(0) 
t.up() 
t.goto(0, 215) 
t.down()  

#main function, main of program
def main():

    #loop untuk membuat petals
    for i in range(petals): #i adalah iterasi
        draw_petal() #memanggil fungsi menggambar petals
        t.left(360/petals) #perubahan 

    #memulai menggambar kotak di kordinat yang diinginkan
    t.up() 
    t.goto(-(pixels*rows)//2, 90)
    t.down()

    #loop untuk membuat petals
    for i in range(rows*rows): 

        i+=1 #supaya tidak 0
        
        if i % rows == 0:
            draw_sqr(pixels) #memanggil fungsi
            go_to(pixels, rows) #saat sudah sampai di n pena di pindahkan ke pada posisi awal lalu kebawah sejauh n*length
        else:
            draw_sqr(pixels) #jika bukan kelipatan n maka kotak akan terus dibuat

    #untuk di tampikan di akhir
    msg = "Colorful Chessboard of " + str(rows*rows) + " Squares and Flower of " + str(petals) + " Petals"
    t.goto(0, -(pixels*rows)+50)
    t.color('blue')
    t.write(msg, False, 'center', font=('Arial', 16, 'normal'))
    t.hideturtle()

#fungsi untuk pena berpindah saat sudah keliapatan n
def go_to(pixels, rows):
	t.penup() 
	t.left(180)
	t.forward(pixels*rows)
	t.left(90)
	t.forward(pixels)
	t.left(90)

#fungsi untuk menggambar petal
def draw_petal():
    #random variable float untuk jadi parameter fungsi color (r,g,b)
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)
    t.color(r, g, b)
    rad = 100
    #draw petals
    t.circle(rad, 60)
    t.left(120)
    t.circle(rad, 60)
    t.left(120)

#fungsi untuk menggambar kotak
def draw_sqr(pixels):
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)
    t.color(r, g, b)
    t.begin_fill()
    t.forward(pixels)
    t.right(90)
    t.forward(pixels)
    t.right(90)
    t.forward(pixels)
    t.right(90)
    t.forward(pixels)
    t.right(90)
    t.forward(pixels)
    t.end_fill()

main() #main function
turtle.getscreen()._root.mainloop() #exit