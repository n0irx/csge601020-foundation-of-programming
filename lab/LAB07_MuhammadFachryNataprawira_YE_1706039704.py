class BenJek():
	"""
	Kelas BenJek ini adalah blueprint dari perusahan milik Beni
	"""
	benJekMoney = 0
	#initialisasi konstruktor untuk objek
	def __init__(this, nama, jenis):
		"""
		Konstruktor dari init
		Jenis = jenis dari driver benJek yang dibuat
		Nama = nama dari driver
		Pendapatan = pendapatan driver yang sudah dijadikan 80% dari mentahnya
		Minimal Perjalanan = minimal
		"""
		this.jenis = jenis
		this.nama = nama
		this.pendapatan = 0

		#normal driver
		if(this.jenis == "Normal"):
			this.minimalPerjalanan = 0
			this.ratePerKM = 1000
		#sport driver
		elif(this.jenis == "Sport"):
			this.minimalPerjalanan = 10
			this.ratePerKM = 2500
		#cruiser driver
		elif(this.jenis == "Cruiser"):
			this.minimalPerjalanan = 25
			this.ratePerKM = 7500
	#for printing cek pendapatan driver		

	def driveJek(this, jarak):
		#jika jarak yang diminta sesuai dengan minimal, maka transaksi dijalankan
		if jarak >= this.minimalPerjalanan:
			#money adalah hitungan mentah dari pendapatan
			money = this.ratePerKM*jarak
			moneyDriver = money*(4/5)
			moneyBen = money*(1/5)
			this.pendapatan += moneyDriver		#80% utk driver
			BenJek.benJekMoney += moneyBen	#20% utk benJek
			print("{nama} melakukan perjalanan sejauh {jarak} KM dan mendapatkan pendapatan sebesar {pendapatan}".format(nama = this.nama,
				jarak = jarak, pendapatan = moneyDriver))
		#jika tidak driver, sistem menolak pesanan
		else:
			print("{nama} tidak bisa melakukan perjalanan".format(nama = this.nama))

	def __str__(this):
		return ("{} memiliki pendapatan sebesar Rp.{}".format(this.nama, this.pendapatan))

#para driver
theDriver = {}
#session
session = True

while(session):

	#getting user input
	usrInput = input().split()
	usrCmd = usrInput[0].upper()

	if usrCmd == "DAFTAR":
		#DAFTAR​ ​<nama_driver>​ ​<NORMAL/SPORT>
		usrName = usrInput[1].lower().capitalize()
		usrJenis = usrInput[2].lower().capitalize()
		if usrName not in theDriver:
			theDriver[usrName] = BenJek(usrName, usrJenis)
			print("{nama} berhasil mendaftar sebagai driver BenJek layanan {jenis}".format(nama = usrName, jenis = usrJenis))
		else:
			print("{nama} gagal mendaftar sebagai driver BenJek".format(nama = usrName))

	elif usrCmd == "MULAI":
		#MULAI​ ​PERJALANAN​ ​<nama_driver>​ ​<jarak_ditempuh_km>
		usrName = usrInput[2].lower().capitalize()
		usrJarak = int(usrInput[3])
		#jika driver ada di dalam sistem maka panggil method driverJek untuk jalan
		if usrName in theDriver:
			theDriver[usrName].driveJek(usrJarak)
		#jika tridak ada driver di dalam sistem, benJek akan menolak pesanan
		else:
			print("{nama} tidak ada di dalam sistem".format(nama = usrName))

	elif usrCmd == "CEK":
		#CEK​ ​PENDAPATAN​ ​<nama_driver>
		usrName = usrInput[2].lower().capitalize()
		#jika driver ada di dalam sistem makan akan print info
		if usrName in theDriver:
			print(theDriver[usrName])
		else:
			print("{nama} tidak ada di dalam sistem".format(nama = usrName))

	elif usrCmd == "AKHIR":
		#AKHIR​ ​BULAN
		print("Sudah akhir bulan! Pendapatan BenJek bulan ini adalah Rp.{benmoney} Daftar pendapatan pengemudi:".format(benmoney = BenJek.benJekMoney))
		for key in theDriver:
			print("{nama}: Rp.{pendapatan}".format(nama = key, pendapatan = theDriver[key].pendapatan))

		#jika sudah akhir bulan, maka program akan terminate
		session = False