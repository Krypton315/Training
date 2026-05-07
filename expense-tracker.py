def validationMenu(x):
	x = x.strip
	if not x:
		print("Tolong masukkan input")
		return None
	return x.lower()

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
			pass


def tambahPengeluaran():
	input_jumlah = input("Jumlah: ")
	jumlah = validation_tambah_pengeluaran(input_jumlah, "Jumlah")
	
	input_kategori = input("Kategori: ")
	kategori = validation_tambah_pengeluaran(input_kategori, "Kategori")
	
	input_deskripsi = input("Deskripsi: ")
	deskripsi = validation_tambah_pengeluaran(input_deskripsi, "Deskripsi")
	
	input_tanggal = input("Tanggal: ")
	tanggal = validation_tambah_pengeluaran(input_tanggal, "Tanggal")

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
	for i, x in enumerate(fiturUtama, 1):
		print(f"{i}. {x}")

	pilihanMenu = input("Pilih menu berdasarkan (Nama/Menu): ")
	pilihan = validationMenu(pilihanMenu)

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
