import datetime
import json

dataTemporary = []

def file_save_data():
	print("\nMenyimpan Data ke file...")
	try:
		with open("data_tracker.json", "w") as file:
			json.dump(dataTemporary, file, indent=4)
		print("Data berhasil disimpan ke File")
	except Exception as e:
		print(f"Data gagal disimpan ke File, ERROR: {e}")

def validation_input_none(input_usr):
	x = input_usr.strip()
	if not x:
		print("Tolong masukkan input\n")
		return None
	return x

def validation_input_int(input_usr):
	x = validation_input_none(input_usr)
	if x is None:
		return None
	if not x.isdigit():
		print("Input harus berupa Angka tanpa karakter lain(int)\n")
		return None
	return int(x)

def validation_input_str(input_usr):
	x = validation_input_none(input_usr)
	if x is None:
		return None
	if x.isdigit():
		print("Input harus berupa Kata(str)\n")
		return None
	return x

def input_waktu():
	while True:
		date = validation_input_int(input("Tanggal: "))
		if date is None: continue
		
		if date <= 0 or date > 31:
			print("Tanggal invalid\n")
			continue
		break
	
	while True:
		month = validation_input_int(input("Bulan (Angka): "))
		if month is None: continue
		
		if month <= 0 or month > 12:
			print("Bulan invalid\n")
			continue
		break
	
	while True:
		input_tahun = input("Tahun: ")
		year = validation_input_int(input_tahun)
		if year is not None: break
	 
	return (year, month, date)

def pilih_waktu(input_usr):
	x = validation_input_str(input_usr)
	if x is None:
		return None
	
	pilihan = x.lower()
	if x.lower() == "manual":
		return input_waktu()
	elif x.lower() == "otomatis":
		waktu_sekarang = datetime.datetime.now()
		return (waktu_sekarang.year, int(waktu_sekarang.month), int(waktu_sekarang.day))
	
	print("Mohon masukkan Pilihan yang tersedia dengan Benar dan Jelas\n")
	return None

def cek_data(data):
	if not data:
		print("Tidak ada Data\n")
		return None
	return data

def id_unik():
	if not dataTemporary:
		return 1
	return max(item["id"] for item in dataTemporary) + 1			

def tambahPengeluaran():
	print("\n=== Tambah Pengeluaran ===")
	data = dataTemporary
	
	while True:
		jumlah = validation_input_int(input("Jumlah: "))
		if jumlah is not None: break
	
	while True:
		kategori = validation_input_str(input("Kategori:"))
		if kategori is not None: break

	deskripsi = input("Deskripsi: ").strip()
	
	while True:
		waktu = pilih_waktu(input("Waktu (Manual/Otomatis): "))
		if waktu is not None: break
	
	dataNew = {
		"id" : id_unik(),
		"jumlah" : jumlah,
		"kategori" : kategori,
		"deskripsi" : deskripsi,           
		"waktu" : waktu
	}
	
	dataTemporary.append(dataNew)
	print(f"\nData berhasil ditambahkan dengan ID: {dataNew['id']}")
	file_save_data()

def lihatSemuaData():
	print("\n=== Semua data ===")
	data = cek_data(dataTemporary)
	if data is None: return 
	
	print("ID | Tanggal | Kategori | Jumlah | Deskripsi")
	for item in data:
		y, m ,d = item["waktu"]
		print(f"{item["id"]} | {y}-{m:02d}-{d:02d} | {item["kategori"]} | {item["jumlah"]} | {item["deskripsi"]}")

def filterBerdasarkanKategori():
	print("\n=== Berdasarkan Kategori ===")
	data = cek_data(dataTemporary)
	if data is None: return 
	
	while True:
		input_kategori = validation_input_str(input("Pilih kategori: "))
		if input_kategori is None: continue
		
		cek_kategori = any(input_kategori.lower() == item["kategori"].lower() for item in dataTemporary)
		if not cek_kategori:
			print("Mohon masukkan Kategori yang tersedia dengan Benar dan Jelas")
			return
		
		print(f"\n> Lihat {input_kategori} ")
		print("ID | Tanggal | Jumlah | Deskripsi")
		for item in data:
			if input_kategori.lower() == item["kategori"].lower():
				y, m, d = item["waktu"]
				print(f"{item["id"]} | {y}-{m:02d}-{d:02d} | {item["jumlah"]} | {item["deskripsi"]}")
		break

def ringkasan():
	print("\n=== Ringkasan ===")
	data = cek_data(dataTemporary)
	if data is None: return

	total = 0
	kategori_map = {}

	for item in data:
		total += item["jumlah"]
		kat_key = item["kategori"].lower()

		kategori_map[kat_key] = kategori_map.get(kat_key, 0) + item["jumlah"]

	print(f"Total: {total}\n")
	print("Per Kategori:")
	for kat, jml in kategori_map.items():
		print(f"- {kat.capitalize()}: {jml}")

	nama_terbesar = max(kategori_map, key=kategori_map.get)
	nilai_terbesar = kategori_map[nama_terbesar]

	print(f"\nKategori terbesar: {nama_terbesar}")
	print(f"Kategori sama besar lainnya:")

	ada_yang_sama = False
	for kat, jml in kategori_map.items():
		if jml == nilai_terbesar and kat != nama_terbesar:
			print(f"- {kat.capitalize()}")
			ada_yang_sama = True
			
	if not ada_yang_sama:
		print("- (Tidak ada)")
		

def hapusData():
	print("\n=== Hapus Data ====")
	data = cek_data(dataTemporary)
	if data is None: return
		
	while True:
		input_id = validation_input_int(input("> Hapus (id): "))
		if input_id is None: continue
		
		for item in data:
			if input_id == item["id"]:
				data.remove(item)
				print(f"\nData dengan ID: {input_id}, berhasil dihapus")
				file_save_data()
				return 
		
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
