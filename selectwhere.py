import sqlite3

koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()
kursor.execute("SELECT * FROM HEWAN WHERE jenis = 'Mamalia'")
baris_table = kursor.fetchall()

print("Data Hewan:")
print("==============================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<10}".format("id", "nama", "jenis", "asal", "jml_skrng", "thn_ditemukan"))
print("--------------------------------------------------------------")
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<10}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()