class BenCoin(object):
	"""
	Class for creating BenCoin account
	"""
	#variable for all instances
	dataAcc, listMataUang, session = {}, {}, True
	def __init__(this, name, jenis):
		#decalre object's variables
		this.name = name
		this.jenis = jenis
		this.saldo = 0
		this.history = []

		#per type of BenCoin Account
		if this.jenis == "Pelajar":
			this.batasTransaksi = 25
			this.batasTabungan = 150
			this.feeTransaksi = 0
		elif this.jenis == "Reguler":
			this.batasTransaksi = 100
			this.batasTabungan = 500
			this.feeTransaksi = 5
		elif this.jenis == "Bisnis":
			this.batasTransaksi = 500
			this.batasTabungan = 2000
			this.feeTransaksi = 15
		elif this.jenis == "Elite":
			this.batasTransaksi = 10000
			this.batasTabungan = 100000
			this.feeTransaksi = 50

		print("Akun atas nama {} telah terdaftar dengan paket {}".format(this.name, this.jenis))

	#untuk print INFO statement
	def __str__(this):
		#for printing info
		return """
		Nama :	{}
		Jenis Akun : {}
		Jumlah BenCoin : {:.1f}
		Transaksi :
		{}
		""".format(this.name, this.jenis, this.saldo, '\n\t\t'.join(this.history))

	#setor uang, dan juga set batas uang yang masuk
	def setor(this, nominal, matauang):
		#format: SETOR [nama] [nominal] [matauang]
		#jika jenis uang telah ditambahkan, maka lanjut
		if (matauang in BenCoin.listMataUang):
			#membentuk setoran yaitu dalam satuan BenCoin
			setoran = (nominal/BenCoin.listMataUang[matauang])
			#if saldo is not full yet
			if (this.saldo < this.batasTabungan):
				#if saldo + setoran is greater than batas tabungan,
				#then just store BenCoin until the same as batas tabungan
				if ((this.saldo + setoran) > this.batasTabungan):
					setoran = this.batasTabungan - this.saldo
					this.saldo += setoran
					this.history.append("SETOR {} {} {:.1f}".format(matauang, nominal, setoran))
					print("Akun {} telah bertambah {} BenCoin".format(this.name, setoran))
				#if saldo + setoran is lesser than batas tabungan, just store the benCoin
				else:
					this.saldo += setoran
					this.history.append("SETOR {} {} {:.1f}".format(matauang, nominal, setoran))
					print("Akun {} telah bertambah {} BenCoin".format(this.name, setoran))
			#if saldo is full
			else:
				print("Akun {} sudah memenuhi kapasitas".format(this.name))
		#if there is no mataUang in list, then print
		else:
			print("Mata uang {} tidak ada, silahkan tambah mata uang".format(matauang))

	#for tarik saldo
	def tarik(this, bencoin, matauang):
		#if saldo exists, next
		if (this.saldo > 0):
			#if matauang exsist in list, next
			if (matauang in BenCoin.listMataUang):
				#tarikan is amount of money that will be taken
				#if more than batas, jadi batas
				if bencoin > this.batasTransaksi:
					bencoin = this.batasTransaksi

				tarikan = (bencoin*BenCoin.listMataUang[matauang])
				if  (this.saldo - (bencoin + this.feeTransaksi)) >= 0:
					this.saldo -= (bencoin + this.feeTransaksi)
					this.history.append("TARIK {} {} {}".format(matauang, int(tarikan), int(bencoin)))
					print("Penarikan {} dari akun {} berhasil !".format(int(tarikan), this.name))
				#if the amout that want to be taken is less, can not take money
				else:
					print("Akun {} sudah kurang uang".format(this.name))
			#tereksekusi jika tidak ada mata uang yang disebut kan
			else:
				print("Mata uang {} tidak ada, silahkan tambah mata uang".format(matauang))
		#if saldo is 0, can not take anything
		else:
			print("Saldo anda kurang")

	#for transfer
	def transfer(this, penerima, nominal):
		#if the amount is greater than 0, next
		if (this.saldo > this.feeTransaksi):
			#if the amount that wanna be transfered is greater than batasTransaksi
			#then just transfer max or the same as batasTransaksi, if not, just next
			if (nominal >= this.batasTransaksi):
				nominal = this.batasTransaksi
			#if the amount of money that want to be transfered greater than and
			#equal to current saldo, then just transfer the amount that is allowed
			if (nominal >= this.saldo):
				saldoTerima = nominal - this.feeTransaksi
				this.saldo -= (saldoTerima + this.feeTransaksi)
				#if the amount that taken by taker make the tabungan full
				#send back the remainder value(wihout fee, of course)
				if(penerima.saldo + saldoTerima > penerima.batasTabungan):
					saldoSisa = (saldoTerima - (penerima.saldo + penerima.batasTabungan))
					saldoTerima = (penerima.batasTabungan - penerima.saldo)
					if(saldoTerima > 0):
						this.saldo += saldoSisa
						penerima.saldo += saldoTerima
						#make a history
						this.history.append("TRANSFER {} {}".format(penerima.name, saldoTerima))
						print("{} berhasil mentransfer {} BenCoin kepada {}".format(this.name, saldoTerima, penerima.name))
					else:
						this.saldo += (SaldoTerima + this.feeTransaksi)
						print("Akun {} sudah penuh".format(penerima.name))
				#if not, just do it
				else:
					penerima.saldo += saldoTerima
					this.history.append("TRANSFER {} {}".format(penerima.name, saldoTerima))
					print("{} berhasil mentransfer {} BenCoin kepada {}".format(this.name, saldoTerima, penerima.name))
			#no problems, just do the things
			else:
				this.saldo -= (nominal+this.feeTransaksi)
				#jika uang yang ditransfer memenuhi tabungan penerima maka
				#transfer sebagian, dan kembalikan sisanya
				if(penerima.saldo + nominal > penerima.batasTabungan):
					saldoTerima = penerima.batasTabungan - penerima.saldo
					saldoSisa = (nominal + penerima.saldo - penerima.batasTabungan)
					#if yang dikirim lebih dari no, lanjut
					if(saldoTerima > 0):
						penerima.saldo += saldoTerima
						this.saldo += saldoSisa
						#make a history
						this.history.append("TRANSFER {} {}".format(penerima.name, saldoTerima))
						print("{} berhasil mentransfer {} BenCoin kepada {}".format(this.name, saldoTerima, penerima.name))
					else:
						this.saldo += (saldoTerima + this.feeTransaksi + saldoSisa)
						print("Akun {} sudah penuh".format(penerima.name))
				else:
					#jika tidak ada kasus
					penerima.saldo += nominal
					#make a history
					this.history.append("TRANSFER {} {}".format(penerima.name, nominal))
					print("{} berhasil mentransfer {} BenCoin kepada {}".format(this.name, nominal, penerima.name))
		else:
			print("Akun {} tidak cukup untuk melakukan transfer".format(this.name))

		#fungsi untuk tambah mata uang
	def tambah(mataUang, nilaiTukar):
			BenCoin.listMataUang[mataUang] = int(nilaiTukar)
			print("Mata uang {} telah ditambahkan dengan rate {} per BenCoin.".format(mataUang, nilaiTukar))
	def ubah(mataUang, nilaiTukar):
			BenCoin.listMataUang[mataUang] = int(nilaiTukar)
			print("Rate mata uang {} berubah menjadi {} per BenCoin.".format(mataUang, nilaiTukar))

if __name__ == '__main__':
	while(BenCoin.session):
		try:
			#getting usr input
			usrInput = input().split()
			#variables for command
			usrCmd = usrInput[0].upper()

			if usrCmd == "DAFTAR":
				#DAFTAR <nama> <jenis akun>
				usrName = usrInput[1].lower().capitalize()
				usrJenis = usrInput[2].lower().capitalize()
				if usrName not in BenCoin.dataAcc:
					if usrJenis in ["Pelajar", "Reguler", "Bisnis", "Elite"]:
						BenCoin.dataAcc[usrName] = BenCoin(usrName, usrJenis)
					else:
						print("Mohon maaf kami tidak menyediakan jenis {}".format(usrJenis))
				else:
					print("Akun {} sudah ada".format(usrName))

			elif usrCmd == "SETOR":
				#SETOR [USER] [NOMINAL] [MATAUANG]
				usrName = usrInput[1].lower().capitalize()
				if usrName in BenCoin.dataAcc:
					nominalUang = int(usrInput[2])
					mataUang = usrInput[3].upper()
					BenCoin.dataAcc[usrName].setor(nominalUang, mataUang)
				else:
					print("Akun atas nama {} tidak ada, silahkan buat akun".format(usrName))

			elif usrCmd == "TARIK":
				#TARIK [USER] [BENCOIN] [MATAUANG]
				usrName = usrInput[1].lower().capitalize()
				if usrName in BenCoin.dataAcc:
					usrName = usrInput[1].lower().capitalize()
					mataUang = usrInput[3].upper()
					benCoin = float(usrInput[2])
					BenCoin.dataAcc[usrName].tarik(benCoin, mataUang)
				else:
					print("Akun atas nama {} tidak ada, silahkan buat akun".format(usrName))

			elif usrCmd == "TRANSFER":
				#TRANSFER [SENDER] [RECEIVER] [BENCOIN]
				usrName = usrInput[1].lower().capitalize()
				usrPenerima = usrInput[2].lower().capitalize()
				usrPenerimaObj = BenCoin.dataAcc[usrPenerima]
				if usrPenerima != usrName:
					if usrName in BenCoin.dataAcc and usrPenerima in BenCoin.dataAcc:
						benCoin = float(usrInput[3])
						BenCoin.dataAcc[usrName].transfer(usrPenerimaObj, benCoin)
					else:
						print("Akun atas nama {} atau {} tidak ada, silahkan buat akun".format(usrName, usrPenerima))
				else:
					print("Tidak bisa transfer ke diri sendiri")

			elif usrCmd == "TAMBAH":
				#TAMBAH [MATAUANG] [RATEAWAL]
				mataUang = usrInput[1].upper()
				rateUang = int(usrInput[2])
				if(mataUang not in BenCoin.listMataUang):
					if rateUang > 0:
						BenCoin.tambah(mataUang, rateUang)
					else:
						print("Masukan rate yang benar")
				else:
					print("Mata uang {} telah ada, silahkan gunakan comand ubah".format(mataUang))

			elif usrCmd == "UBAH":
				#TAMBAH [MATAUANG] [RATEBARU]
				mataUang = usrInput[1].upper()
				rateUang = int(usrInput[2])
				if(mataUang not in BenCoin.listMataUang):
					print("Mata uang {} tidak tersedia, silahkan tambahkan".format(mataUang))
				else:
					if rateUang > 0:
						BenCoin.ubah(mataUang, rateUang)
					else:
						print("Masukan rate yang benar")

			elif usrCmd == "INFO":
				usrName = usrInput[1].lower().capitalize()
				#printing info, invoke __STR__
				if usrName in BenCoin.dataAcc:
					print(BenCoin.dataAcc[usrName])
				else:
					print("Akun atas nama {} tidak ada, silahkan buat akun".format(usrName))
			#jika tidak ada command yang memenuhi
			elif usrCmd == "EXIT":
				BenCoin.session = False
			#command salah (default)
			else:
				print("Tidak ada command {}, silahkan pilih command lagi".format(usrCmd))
		#jika argumen kurang, atau ada typo saat input, akan di handle oleh exception.
		except:
			print("Command anda salah")
