kanan = "NAMA : RHENO JULIUS A. ".ljust(30,'=')
print(""+kanan+"")
kanan = "NIM : 222410102053 ".ljust(30,'=')
print(""+kanan+"")

tugas = "tugas algo 3".center(30,'=')
print(""+tugas+"")

#===================================================================#

jumlah = int(input("\nJUMLAH KATA : "))
list_nama = []

for x in range(jumlah) :
  nama = input("MASUKKAN KATA : ")
  list_nama.append(nama)

for x in range(len(list_nama)) :
  hasil = list(list_nama[x])
  print("\nHASIL : \n")

  for y in range(len(hasil) - 1 ) :
    if ord(hasil[y]) < ord(hasil[y + 1]):
      print("{} KURANG DARI {}, SELISIHNYA ADALAH {}".format(hasil[y], hasil[y + 1],ord(hasil[y + 1]) - (ord(hasil[y]))))

    if ord(hasil[y]) > ord(hasil[y + 1]):
      print("{} LEBIH DARI {}, SELISIHNYA ADALAH {}".format(hasil[y], hasil[y + 1],ord(hasil[y]) - (ord(hasil[y + 1]))))

    if ord(hasil[y]) == ord(hasil[y + 1]):
      print("{} SAMA DENGAN {}, SELISIHNYA ADALAH {}".format(hasil[y], hasil[y + 1], ord(hasil[y + 1]) - (ord(hasil[y]))))