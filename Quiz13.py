#QUIZ 1
data = "1011001"
jumlah_1 = data.count("1")

#Paritas Genap (Even): Tambah '1' jika jumlah '1' ganjil
even = "1" if jumlah_1 % 2 != 0 else "0"

#Paritas Ganjil (Odd): Tambah '1' jika jumlah '1' genap
odd = "1" if jumlah_1 % 2 == 0 else "0"

print("Data + Even Parity:", data + even)
print("Data + Odd Parity:", data + odd)

#QUIZ 2
kata = "Trisakti"

total_ascii = sum(ord(huruf) for huruf in kata)

checksum = total_ascii % 256

print("Total Nilai ASCII:", total_ascii)
print("Hasil Checksum:", checksum)