import datetime

def validation_menu(x):
	x = x.strip()
	if not x:
		print("Tolong masukkan input")
		return None
	return x.lower()

def validation_waktu(x):
	x = x.strip()
	if not x:
		print("Tolong masukkan input")
		return None
	if not x.isdigit():
		print("Input harus Angka")
		return None
	n = int(x)
	return n

def validation_tanggal():
	while True:
		input_tanggal = input("Tanggal: ")
		tanggal = validation_waktu(input_tanggal)
		if tanggal is None:
			continue
		date = tanggal
		break

	while True:
		input_bulan = input("Bulan (Angka): ")
		bulan = validation_waktu(input_bulan)
		if bulan is None:
			continue
		month = bulan
		break

	while True:
		input_tahun = input("Tahun: ")
		tahun = validation_tahun(input_tahun)
		if tahun is None:
			continue
		year = tahun
		break

	n = [year, month, date]
	return n

def validation_tambah_pengeluaran(x, y):
	if y == "Deskripsi":
		return x.strip()

	x = x.strip()
	if not x:
		print("Tolong masukkan input")
		return None
	
	match y:
		case "Jumlah":
			if not x.isdigit():
				print("Input harus angka")
				return None
			n = float(x)
			return n 
		
		case "Kategori":
			if x.isdigit():
				print("Input harus string/teks")
				return None
			return x

		case "Tanggal":
			if x.lower == "manual":
				tanggal = validation_tanggal()
				return tanggal

			if x.lower == "otomatis":
				x = datetime.datetime.now()
				year = x.year
				month = x.strftime("%m")
				date = x.strftime("%d")
				n = [year, month, date]
				return n

def tambahPengeluaran():
	print("\n=== Tambah Pengeluaran ===")
	while True:
		input_jumlah = input("Jumlah: ")
		jumlah = validation_tambah_pengeluaran(input_jumlah, "Jumlah")
		if jumlah is None:
			continue
		break
	
	while True:
		input_kategori = input("Kategori: ")
		kategori = validation_tambah_pengeluaran(input_kategori, "Kategori")
		if kategori is None:
			continue
		break

	input_deskripsi = input("Deskripsi: ")
	deskripsi = validation_tambah_pengeluaran(input_deskripsi, "Deskripsi")
	
	while True:
		input_waktu = input("Waktu pilih (Manual/Otomatis): ")
		waktu = validation_tambah_pengeluaran(input_waktu, "Tanggal")
		if waktu is None:
			continue
		break


def lihatSemuaData():
	pass

def filterBerdasarkanKategori():
	pass

def ringkasan():
	pass

def hapusData():
	pass



while True:
	print("=== Expense Tracker ===")
	menuUtama = ("Tambah Pengeluaran", "Lihat semua Data", "Filter berdasarkan Kategori", "Ringkasan(Report)", "Hapus Data")
	for i, x in enumerate(menuUtama, 1):
		print(f"{i}. {x}")

	pilihanMenu = input("Pilih menu berdasarkan (Nama/Nomor): ")
	pilihan = validation_menu(pilihanMenu)

	if pilihan is None:
		continue

	match pilihan:
		case "1" | "tambah pengeluaran":
			tambahPengeluaran()

		case "2" | "lihat semua data":
			lihatSemuaData()

		case "3" | "filter berdasarkan kategori":
			filterBerdasarkanKategori()

		case "4" | "ringkasan" | "report" | "ringkasan(report)":
			ringkasan()

		case "5" | "hapus data":
			hapusData()

		case "6" | "keluar":
			break

		case _:
			print("Menu tidak tersedia")
