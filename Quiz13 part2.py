#QUIZ 1
def hitung_paritas(data_bit):
  jumlah_satu = data_bit.count('1')

  even_parity = '1' if jumlah_satu % 2 != 0 else '0'
  data_even = data_bit + even_parity

  odd_parity = '1' if jumlah_satu % 2 == 0 else '0'
  data_odd = data_bit + odd_parity

  print('=== HASIL PERHITUNGAN PARITAS ===')
  print(f'Data Bit Awal        : {data_bit}')
  print(f'Jumlah Bit "1"       : {jumlah_satu}')
  print(f'-----------------------------------')
  print(f'Bit Paritas Genap    : {even_parity}')
  print(f'Data Akhir (Even)    : {data_even}')
  print(f'-----------------------------------')
  print(f'Bit Paritas Ganjil   : {odd_parity}')
  print(f'Data Akhir (Odd)     : {data_odd}')

input_data = '1011001'
hitung_paritas(input_data)

#QUIZ 2
def hitung_checksum_kata(kata):
  print(f'=== PERHITUNGAN CHECKSUM KATA: "{kata}" ===')
  total_ascii = 0

  # Menampilkan nilai ASCII dari setiap karakter
  for char in kata:
    nilai_ascii = ord(char)
    total_ascii += nilai_ascii
    print(f"Karakter '{char}' -> ASCII: {nilai_ascii} (Hex: {hex(nilai_ascii)})")

  print(f'---------------------------------------------')
  print(f'Total Jumlah Nilai ASCII : {total_ascii}')

  # Menghitung checksum sederhana menggunakan Modulo 256 (8-bit checksum)
  checksum_mod = total_ascii % 256

  # Menghitung nilai 1's Complement 8-bit dari checksum (opsional umum dalam jaringan)
  checksum_ones_complement = 255 - checksum_mod

  print(f'Checksum (Modulo 256)    : {checksum_mod} (Hex: {hex(checksum_mod)})')
  print(
      f"Checksum (1's Complement): {checksum_ones_complement} (Hex:"
      f' {hex(checksum_ones_complement)})'
  )

  return checksum_mod

hitung_checksum_kata('Trisakti')