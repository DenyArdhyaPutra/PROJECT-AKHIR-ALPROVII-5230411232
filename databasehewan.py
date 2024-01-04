import sqlite3
koneksi = sqlite3.connect('database_hewan.db')

koneksi.execute('''
                CREATE TABLE HEWAN(
                 id_Hewan INTEGER PRIMARY KEY AUTOINCREMENT,
                 nama VARCHAR(50),
                 jenis VARCHAR(50),
                 asal VARCHAR(50),
                 jml_skrng INTEGER(10),
                 thn_ditemukan INTEGER(10)
                )
                ''')

koneksi.close()  