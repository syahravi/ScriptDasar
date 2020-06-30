'''
mengaplikasikan fungsi:
def,
while, True,
break,
if name == main,
try,
except,
if,
elif,
print,
int,
input
'''
def Tambah(a,b):
	print(f"{a} + {b} Sama Dengan ", a+b)
def Kurang(a,b):
	print(f"{a} - {b} Sama Dengan ", a-b)
def Kali(a,b):
	print(f"{a} X {b} Sama Dengan ", a*b)
def Bagi(a,b):
	print(f"{a} / {b} Sama Dengan ", a/b)

def Tehee():
	print("""=========================================================
	///////////TABEL OF OPERATIONS//////////
	1.\tPertambahan
	2.\tPengurangan
	3.\tPerkalian
	4.\tPembagian
	0.\tExit""")
	opsional = {
	1: Tambah,
	2: Kurang,
	3: Kali,
	4: Bagi
}
	while True:
		try:
			pilih = int(input("Metode Matematika\t\t#"))
			if pilih == 0:
				print("Terima Kasih")
				break
			one = int(input("Angka Pertama\t#"))
			two = int(input("Angka Kedua\t#"))
			opsional[pilih](one,two)#Pahami ini :)
		except:
			te = input("Keluar? (Y/N)")
			if te.upper() == "Y":
				print("Terima kasih :)")
				break
			elif te == '':
				print("""=========================================================
				///////////TABEL OF OPERATIONS//////////
				1.\tPertambahan
				2.\tPengurangan
				3.\tPerkalian
				4.\tPembagian
				0.\tExit""")

if __name__ == '__main__':
	Tehee()