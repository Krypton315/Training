import datetime
dataTemporary = []

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
	return x

def validation_cek_data(x):
	if len(x) == 0:
		print("Tidak ada Data\n")
		return None
	return x

def validation_id(x):
	x = x.strip()
	if not x:
		print("Tolong masukkan input\n")
		return None
	if not x.isdigit():
		print("Harus berupa id (Angka)\n")
		return None
	for i in range(len(dataTemporary)):
		if int(x) == dataTemporary[i]["id"]:
			return int(x)
		else:
			print("Data tidak tersedia\n")
			return None


def tambahPengeluaran():
	print("\n=== Tambah Pengeluaran ===")
	dataState = {
	"id" : 0,
	"jumlah" : 0,
	"kategori" : "x",
	"deskripsi" : "x",           
	"tanggal" : ()
}
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
	x = validation_cek_data(dataTemporary)
	if x is None:
		return None
	print("ID", "Tanggal", "Kategori" , "Jumlah", "Deskripsi", sep=" | ")
	for i in range(len(dataTemporary)):
		d = x[i]["tanggal"][2]
		m = x[i]["tanggal"][1]
		y = x[i]["tanggal"][0]
		print(f"{x[i]["id"]}  | {y}-{m}-{d} | {x[i]["kategori"]} | {x[i]["jumlah"]} | {x[i]["deskripsi"]}")

def filterBerdasarkanKategori():
	print("\n=== Berdasarkan Kategori ===")
	data = validation_cek_data(dataTemporary)
	if data is None:
		return None
	while True:
		input_kategori = input("Pilih kategori: ")
		kategori = validation_kategori(input_kategori)
		if kategori is None:
			continue
		x = data
		print(f"\n> Lihat {kategori} ")
		print("ID", "Tanggal", "Jumlah", "Deskripsi", sep=" | ")
		for i in range(len(x)):
			if kategori == x[i]["kategori"].lower():
				d = x[i]["tanggal"][2]
				m = x[i]["tanggal"][1]
				y = x[i]["tanggal"][0]
				print(f"{x[i]["id"]}  | {y}-{m}-{d} | {x[i]["jumlah"]} | {x[i]["deskripsi"]}")
		break

def ringkasan():
	print("\n=== Ringkasan ===")
	x = validation_cek_data(dataTemporary)
	if x is None:
		return None
	total = 0
	for i in range(len(x)):
		total += x[i]["jumlah"]                                 
	print(f"Total: {total}\n")
	print("Per Kategori:")
	cek_kategori = []
	list_kategori = []
	
	for i in range(len(x)):
		kategori = x[i]["kategori"]
		if kategori not in cek_kategori:
			cek_kategori.append(kategori)
			totalKategori = 0
			state_kategori = {"Nama_kategori" : "x", "Jumlah_total" : 0}
			for n in range(len(x)):
				if kategori == x[n]["kategori"]:
					totalKategori += x[n]["jumlah"]
			
			state_kategori["Nama_kategori"] = kategori
			state_kategori["Jumlah_total"] = totalKategori 
			list_kategori.append(state_kategori)
			print(f"- {x[i]["kategori"]}: {totalKategori}")
	
	cek_terbesar = max(list_kategori, key=lambda i: i["Jumlah_total"])	
	print(f"\nKategori terbesar: {cek_terbesar["Nama_kategori"]}")

def hapusData():
	print("\n=== Hapus Data ====")
	input_id = input("> Hapus (id): ")
	data_id = validation_id(input_id)
	x = dataTemporary
	for i in range(len(x)):
		if data_id == x[i]["id"]:
			del x[i]
	print(f"\nData dengan id {data_id} berhasil dihapus")


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
