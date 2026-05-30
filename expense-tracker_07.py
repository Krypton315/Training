import datetime
import json
import difflib

dataTemporary = []

def file_data():
	with open("data_tracker.md", "w") as file:
		x = json.dumps(dataTemporary)
		file.write(x)
	
def validation_input_none(x):
	x = x.strip()
	if not x:
		print("Tolong masukkan input\n")
		return None
	return x

def validation_input_int(x):
	i = validation_input_none(x)
	if i is None:
		return None
	if not i.isdigit():
		return None
	return int(i)

def validation_input_str(x):
	i = validation_input_none(x)
	if i is None:
		return None
	return i

def validation_tanggal():
	while True:
		input_tanggal = input("Tanggal: ")
		tanggal = validation_input_int(input_tanggal)
		if tanggal is None:
			continue
		if tanggal <= 0 or tanggal > 31:
			print("Tanggal invalid\n")
			continue
		date = tanggal
		break
	while True:
		input_bulan = input("Bulan (Angka): ")
		bulan = validation_input_int(input_bulan)
		if bulan is None:
			continue
		if bulan <= 0 or bulan > 12:
			print("Bulan invalid\n")
			continue
		month = bulan
		break
	while True:
		input_tahun = input("Tahun: ")
		tahun = validation_input_int(input_tahun)
		if tahun is None:
			continue
		year = tahun
		break
	n = (year, month, date)
	return n

def validation_waktu(x):
	i = validation_input_str(x)
	if i is None:
		return None
	if i.lower() == "manual":
		tanggal = validation_tanggal()
		return tanggal
	if i.lower() == "otomatis":
		x = datetime.datetime.now()
		year = x.year
		month = x.strftime("%m")
		date = x.strftime("%d")
		n = (year, int(month), int(date))
		return n
	print("Hanya Manual dan Otomatis\n")

def validation_cek_data(x):
	if len(x) == 0:
		print("Tidak ada Data\n")
		return None
	return x

def validation_id():
	x = len(dataTemporary)
	if x > 0:
		for i in range(x):
			n = x + 1
			if n == x[i]["id"]:
				n += 1
				return n
	x += 1
	return x
			

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
		jumlah = validation_input_int(input_jumlah)
		if jumlah is None:
			continue
		dataState["jumlah"] = jumlah
		break
	while True:
		input_kategori = input("Kategori: ")
		kategori = validation_input_str(input_kategori)
		if kategori is None:
			continue
		dataState["kategori"] = kategori 
		break
	input_deskripsi = input("Deskripsi: ")
	deskripsi = input_deskripsi.strip()
	dataState["deskripsi"] = deskripsi
	while True:
		input_waktu = input("Waktu pilih (Manual/Otomatis): ")
		tanggal = validation_waktu(input_waktu)
		if tanggal is None:
			continue
		dataState["tanggal"] = tanggal
		break
	id_unik = validation_id()
	dataState["id"] = id_unik
	dataTemporary.append(dataState)
	file_data()

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
		kategori = validation_input_str(input_kategori)
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
	x = validation_cek_data(dataTemporary)
	if x is None:
		return None
	while True:
		input_id = input("> Hapus (id): ")
		data_id = validation_input_int(input_id)
		if data_id is None:
			continue
		for i in range(len(x)):
			if data_id == x[i]["id"]:
				del x[i]
				file_data()
				print(f"Data dengan id {data_id} berhasil dihapus\n")
				break		
		break
		print("Data tidak tersedia\n")
		continue

while True:
	print("\n=== Expense Tracker ===")
	menuUtama = ("Tambah Pengeluaran", "Lihat semua Data", "Filter berdasarkan Kategori",
		"Ringkasan(Report)", "Hapus Data", "Keluar")
	for i, x in enumerate(menuUtama, 1):
		print(f"{i}. {x}")
	pilihanMenu = input("Pilih menu berdasarkan (Nama/Nomor): ")
	pilihan = validation_input_none(pilihanMenu)
	if pilihan is None:
		continue
	pilihan = pilihan.lower()
	similiraty = difflib.get_close_matches(pilihan, menuUtama.lower(), n=1, cutoff=0.6)
	match similiraty.lower():
		case "tambah pengeluaran":
			tambahPengeluaran()
		case "lihat semua data":
			lihatSemuaData()
		case "filter berdasarkan kategori":
			filterBerdasarkanKategori()
		case "ringkasan(report)":
			ringkasan()
		case "hapus data":
			hapusData()
		case "keluar":
			break
		case _:
			print("Menu tidak tersedia")
