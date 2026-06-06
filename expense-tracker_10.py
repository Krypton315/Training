import datetime
import json

dataTemporary = []

def file_save_data():
	print("\nMenyimpan Data ke file...")
	data = json.dumps(dataTemporary)
	try:
		with open("data_tracker.json", "w") as file:
			file.write(data)
	except Exception as e:
		print(f"Data gagal disimpan ke File, ERROR: {e}")
	else:
		print("Data berhasil disimpan ke File")

def validation_input_none(input):
	x = input.strip()
	if not x:
		print("Tolong masukkan input\n")
		return None
	return x

def validation_input_int(input):
	x = validation_input_none(input)
	if x is None:
		return None
	if not x.isdigit():
		print("Input harus berupa Angka tanpa karakter lain(int)\n")
		return None
	return int(x)

def validation_input_str(input):
	x = validation_input_none(input)
	if x is None:
		return None
	if x.isdigit():
		print("Input harus berupa Kata(str)\n")
		return None
	return x

def input_waktu():
	while True:
		input_tanggal = input("Tanggal: ")
		date = validation_input_int(input_tanggal)
		if date is None:
			continue
		if date <= 0 or date > 31:
			print("Tanggal invalid\n")
			continue
		break
	while True:
		input_bulan = input("Bulan (Angka): ")
		month = validation_input_int(input_bulan)
		if month is None:
			continue
		if month <= 0 or month > 12:
			print("Bulan invalid\n")
			continue
		break
	while True:
		input_tahun = input("Tahun: ")
		year = validation_input_int(input_tahun)
		if year is None:
			continue
		break
	waktu = (year, month, date)
	return waktu

def pilih_waktu(input):
	x = validation_input_str(input)
	if x is None:
		return None
	if x.lower() == "manual":
		waktu = input_waktu()
		return waktu
	if x.lower() == "otomatis":
		waktu_sekarang = datetime.datetime.now()
		year = waktu_sekarang.year
		month = waktu_sekarang.strftime("%m")
		date = waktu_sekarang.strftime("%d")
		waktu = (year, int(month), int(date))
		return waktu
	print("Mohon masukkan Pilihan yang tersedia dengan Benar dan Jelas\n")

def cek_data(data):
	if len(data) == 0:
		print("Tidak ada Data\n")
		return None
	return data

def cek_kategori(kategori):
	data = dataTemporary
	jumlah_kategori_berbeda = 0
	for item in data:
		if kategori.lower() == item["kategori"].lower():
			break
		else:
			jumlah_kategori_berbeda += 1
	if jumlah_kategori_berbeda == len(data):
		print("Mohon masukkan Nama Kategori yang tersedia dengan Benar dan Jelas\n")
		return None
	return kategori

def id_unik():
	data = dataTemporary
	if len(data) > 0:
		daftar_id_terpakai = [item["id"] for item in data]
		target_id = len(data) + 1
		while target_id in daftar_id_terpakai:
			target_id += 1
		return target_id
	id_berikutnya = len(data) + 1
	return id_berikutnya
			

def tambahPengeluaran():
	print("\n=== Tambah Pengeluaran ===")
	data = dataTemporary
	dataState = {
	"id" : 0,
	"jumlah" : 0,
	"kategori" : "x",
	"deskripsi" : "x",           
	"waktu" : ()
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
		waktu = pilih_waktu(input_waktu)
		if waktu is None:
			continue
		dataState["waktu"] = waktu
		break
	Id = id_unik()
	dataState["id"] = Id
	data.append(dataState)
	print(f"\nData berhasil ditambahkan dengan ID: {Id}")
	file_save_data()

def lihatSemuaData():
	print("\n=== Semua data ===")
	data = cek_data(dataTemporary)
	if data is None:
		return None
	print("ID", "Tanggal", "Kategori" , "Jumlah", "Deskripsi", sep=" | ")
	for item in data:
		d = item["waktu"][2]
		m = item["waktu"][1]
		y = item["waktu"][0]
		print(f"{item["id"]}  | {y}-{m}-{d} | {item["kategori"]} | {item["jumlah"]} | {item["deskripsi"]}")

def filterBerdasarkanKategori():
	print("\n=== Berdasarkan Kategori ===")
	data = cek_data(dataTemporary)
	if data is None:
		return None
	while True:
		input_kategori = input("Pilih kategori: ")
		nama_kategori = validation_input_str(input_kategori)
		if nama_kategori is None:
			continue
		kategori = cek_kategori(nama_kategori)
		if kategori is None:
			return None
		print(f"\n> Lihat {nama_kategori} ")
		print("ID", "Tanggal", "Jumlah", "Deskripsi", sep=" | ")
		for item in data:
			if nama_kategori.lower() == item["kategori"].lower():
				d = item["waktu"][2]
				m = item["waktu"][1]
				y = item["waktu"][0]
				print(f"{item["id"]}  | {y}-{m}-{d} | {item["jumlah"]} | {item["deskripsi"]}")
		break

def ringkasan():
	print("\n=== Ringkasan ===")
	data = cek_data(dataTemporary)
	if data is None:
		return None
	total = 0
	for item in data:
		total += item["jumlah"]                                 
	print(f"Total: {total}\n")
	print("Per Kategori:")
	cek_kategori = []
	list_kategori = []
	for item in data:
		kategori = item["kategori"].lower()
		if kategori not in cek_kategori:
			cek_kategori.append(kategori)
			totalKategori = 0
			state_kategori = {"Nama_kategori" : "x", "Jumlah_total" : 0}
			for item_cek in data:
				if kategori == item_cek["kategori"].lower():
					totalKategori += item_cek["jumlah"]
			state_kategori["Nama_kategori"] = kategori
			state_kategori["Jumlah_total"] = totalKategori 
			list_kategori.append(state_kategori)
			print(f"- {item["kategori"].capitalize()}: {totalKategori}")
	cek_terbesar = max(list_kategori, key=lambda i: i["Jumlah_total"])	
	print(f"\nKategori terbesar: {cek_terbesar["Nama_kategori"].capitalize()}")

def hapusData():
	print("\n=== Hapus Data ====")
	data = cek_data(dataTemporary)
	if data is None:
		return None
	while True:
		input_id = input("> Hapus (id): ")
		data_id = validation_input_int(input_id)
		if data_id is None:
			continue
		for item in data:
			if data_id == item["id"]:
				data.remove(item)
				print(f"\nData dengan ID: {data_id}, berhasil dihapus")
				return file_save_data()
					
		print("Data tidak tersedia\n")
		break

while True:
	print("\n=== Expense Tracker ===")
	menuUtama = ("Tambah Pengeluaran", "Lihat semua Data", "Filter berdasarkan Kategori",
		"Ringkasan", "Hapus Data", "Keluar")
	for nomor, nama_menu in enumerate(menuUtama, 1):
		print(f"{nomor}. {nama_menu}")
	pilihanMenu = input("Pilih menu berdasarkan (Nama/Nomor): ")
	pilihan = validation_input_none(pilihanMenu)
	if pilihan is None:
		continue
	match pilihan.lower():
		case "1" | "tambah pengeluaran":
			tambahPengeluaran()
		case "2" | "lihat semua data":
			lihatSemuaData()
		case "3" | "filter berdasarkan kategori":
			filterBerdasarkanKategori()
		case "4" | "ringkasan":
			ringkasan()
		case "5" | "hapus data":
			hapusData()
		case "6" | "keluar":
			break
		case _:
			print("Mohon masukkan (Nama/Nomor) Menu yang tersedia dengan Benar dan Jelas")
