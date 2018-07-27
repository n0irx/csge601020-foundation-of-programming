

def cetak_pertanyaan(urutan, angka_biner):

	print("Soal {}: Berapakah angka desimal dari bilangan biner {}".format(urutan, angka_biner))	# print function

def cek_jawaban(jawaban, angka_biner):
	if jawaban == int(angka_biner, 2):																# return True jika jawaban benar
		return True																
	else:
		return False 																				# return False jika jawaban salah

def main():
	print("Selamat datang di Mini Kuis DDP-1: Sistem Bilangan!")									# kata pengantar awal program
	soal1 = "11111100001"
	soal2 = "11111001111"
	soal3 = "10001100"
	soal4 = "100011101"
	counter_soal = 1
	skor = 0
	while counter_soal <= 4:																		# perulangan while untuk print dan cek soal

		if counter_soal == 1:
			angka_biner = soal1
		elif counter_soal == 2:
			angka_biner = soal2
		elif counter_soal == 3:
			angka_biner = soal3
		elif counter_soal == 4:
			angka_biner = soal4

		cetak_pertanyaan(counter_soal, angka_biner)													# print pertanyaan

		jawaban = int(input("Jawab: "))																# minta input orang untuk di cek

		if cek_jawaban(jawaban, angka_biner):														# jika jawaban benar maka skor bertambah
			skor+=25

		counter_soal+=1																				# setiap while berlangsung, counter bertambah

	print("Skor akhir : {}".format(skor))															# print hasil akhir score

def main2():																						# bonus, yeay
	print("Selamat datang di Mini Kuis DDP-1: Sistem Bilangan!")
	soal1, soal2, soal3, soal4 = input("Masukkan 4 Soal : ").split()								# terima inputan user untuk mendapatkan soal
	counter_soal = 1																				# counter soal set ke angka 1
	skor = 0
	while counter_soal <= 4:
		# if dibawah sini untuk memeriksa soal berapa yang ingin digunakan
		if counter_soal == 1:																		
			angka_biner = soal1
		elif counter_soal == 2:
			angka_biner = soal2
		elif counter_soal == 3:
			angka_biner = soal3
		elif counter_soal == 4:
			angka_biner = soal4
		#cetak pertanyaan
		cetak_pertanyaan(counter_soal, angka_biner)
		# mendapatkan inputan user dan dimasukan ke var jawaban
		jawaban = int(input("Jawab: "))
		# jika jawaban benar maka skor bertambah sebanyak 25
		if cek_jawaban(jawaban, angka_biner):
			skor+=25

		counter_soal+=1

	print("Skor akhir : {}".format(skor))


if __name__ == "__main__":																			# pemanggilan fungsi main dan main2
	main()
	main2()