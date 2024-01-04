import sqlite3
conn = sqlite3.connect('database_hewan.db')


conn.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('Orang utan', 'Mamalia', 'Sumatra', 14000, 2021)")
conn.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('Harimau Sumatra', 'Mamalia', 'Sumatra', 400, 2020)")
conn.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('Komodo', 'Reptil', 'Nusa Tenggara', 3000, 2019)")
conn.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('Anoa', 'Mamalia', 'Sulawesi', 5000, 2022)")
conn.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('Badak Jawa', 'Mamalia', 'Jawa', 72, 2021)")
conn.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('Kuskus', 'Mamalia', 'Papua', 50, 2020)")
conn.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('Trenggiling', 'Mamalia', 'Sumatra', 90, 2022)")
conn.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('Burung Cendrawasih', 'Burung', 'Papua', 45, 2021)")
conn.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('Penyu Hijau', 'Reptil', 'Nusa Tenggara Timur', 20, 2022)")
conn.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('Gajah Sumatra', 'Mamalia', 'Sumatra', 2500, 2023)")
conn.commit()

conn.close()