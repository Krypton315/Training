import datetime

def validation_menu(x):
	x = x.strip()
	if not x:
		print("Tolong masukkan input\n")
		return None
	return x.lower()

def validation_waktu(x):
	x = x.strip()
	if not x:
		print("Tolong masukkan input\n")
		return None
	if not x.isdigit():
		print("Input harus Angka\n")
		return None
	n = int(x)
	return n

def validation_tanggal():
	while True:
		input_tanggal = input("Tanggal: ")
		tanggal = validation_waktu(input_tanggal)
		if tanggal is None:
			continue
		if tanggal <= 0 or tanggal > 31:
			print("Tanggal invalid\n")
			continue
		date = tanggal
		break

	while True:
		input_bulan = input("Bulan (Angka): ")
		bulan = validation_waktu(input_bulan)
		if bulan is None:
			continue
		if bulan <= 0 or bulan > 12:
			print("Bulan invalid\n")
			continue
		month = bulan
		break

	while True:
		input_tahun = input("Tahun: ")
		tahun = validation_waktu(input_tahun)
		if tahun is None:
			continue
		year = tahun
		break

	n = (year, month, date)
	return n

def validation_tambah_pengeluaran(x, y):
	if y == "Deskripsi":
		return x.strip()

	x = x.strip()
	if not x:
		print("Tolong masukkan input\n")
		return None

	match y:
		case "Jumlah":
			if not x.isdigit():
				print("Input harus angka\n")
				return None
			n = int(x)
			return n

		case "Kategori":
			if x.isdigit():
				print("Input harus string/teks\n")
				return None
			return x

		case "Tanggal":
			if x.lower() == "manual":
				tanggal = validation_tanggal()
				return tanggal
			if x.lower() == "otomatis":
				x = datetime.datetime.now()
				year = x.year
				month = x.strftime("%m")
				date = x.strftime("%d")
				n = (year, int(month), int(date))
				return n
			print("Hanya Manual dan Otomatis\n")

def validation_kategori(x):
	x = x.strip()
	if not x:
		print("Tolong masukkan input\n")
		return None
	if x.isdigit():
		print("Input harus string\n")
		return None
	while i in range(len(dataTemporary)):
		n = x.lower()
		if n != dataTemporary[i]["kategori"].lower():
			print("Kategori tidak tersedia\n")
			continue
		else:
			break
	return i

def tambahPengeluaran():
	dataState = {
	"id" : 0,
	"jumlah" : 0,
	"kategori" : "x",
	"deskripsi" : "x",           
	"tanggal" : ()
}

	print("\n=== Tambah Pengeluaran ===")
	while True:
		input_jumlah = input("Jumlah: ")
		jumlah = validation_tambah_pengeluaran(input_jumlah, "Jumlah")
		if jumlah is None:
			continue
		dataState["jumlah"] = jumlah
		break

	while True:
		input_kategori = input("Kategori: ")
		kategori = validation_tambah_pengeluaran(input_kategori, "Kategori")
		if kategori is None:
			continue
		dataState["kategori"] = kategori 
		break

	input_deskripsi = input("Deskripsi: ")
	deskripsi = validation_tambah_pengeluaran(input_deskripsi, "Deskripsi")
	dataState["deskripsi"] = deskripsi

	while True:
		input_waktu = input("Waktu pilih (Manual/Otomatis): ")
		tanggal = validation_tambah_pengeluaran(input_waktu, "Tanggal")
		if tanggal is None:
			continue
		dataState["tanggal"] = tanggal
		break

	n = len(dataTemporary) + 1
	dataState["id"] = n
	dataTemporary.append(dataState)

def lihatSemuaData():
	print("\n=== Semua data ===")
	print("ID", "Tanggal", "Kategori" , "Jumlah", "Deskripsi", sep=" | ")
	x = dataTemporary
	for i in range(len(dataTemporary)):
		d = x[i]["tanggal"][2]
		m = x[i]["tanggal"][1]
		y = x[i]["tanggal"][0]
		print(f"{x[i]["id"]}  | {y}-{m}-{d} | {x[i]["kategori"]} | {x[i]["jumlah"]} | {x[i]["deskripsi"]}")


def filterBerdasarkanKategori():
	print("\n=== Berdasarkan Kategori ===")
	while True:
		input_kategori = input("Pilih kategori: ")
		kategori = validation_kategori(input_kategori)
		if kategori is None:
			continue
		x = dataTemporary
		print(f"\n> Lihat {x[kategori]["kategori"]} ")
		print("ID", "Tanggal", "Jumlah", "Deskripsi", sep=" | ")
		print(kategori)
		d = x[i]["tanggal"][2]
		m = x[i]["tanggal"][1]
		y = x[i]["tanggal"][0]
		print(f"{x[i]["id"]}  | {y}-{m}-{d} | {x[i]["jumlah"]} | {x[i]["deskripsi"]}")
		break

def ringkasan():
	pass

def hapusData():
	pass


dataTemporary = []


while True:
	print("\n=== Expense Tracker ===")
	menuUtama = ("Tambah Pengeluaran", "Lihat semua Data", "Filter berdasarkan Kategori",
		"Ringkasan(Report)", "Hapus Data", "Keluar")

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
