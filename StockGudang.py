barang_gudang = [
    
    {'nama' : 'Processor', 'stock' : 5, 'hargasatuan' : 1500000, 'hargatotal' : 7500000 },

    {'nama' : 'Vga', 'stock' : 3, 'hargasatuan' : 3000000, 'hargatotal' : 9000000 },

    {'nama' : 'Ram', 'stock' : 10, 'hargasatuan' : 700000, 'hargatotal' : 7000000 },

]
    

def PilihanMenu():
     global pilihanselanjutnya 
     
     pilihanselanjutnya = input('''
Silahkan Tentukan Pilihan Selanjutnya :
1. Menambah Daftar Barang
2. Menghapus Daftar Barang
3. Mengedit Daftar Barang
4. Kembali Ke Menu Utama\n
Masukkan Angka Menu Pilihan Anda = ''')

def tampilan_barang():
    # Tampilan Title Table
    title_table = 'Daftar Barang di Gudang'
    title_table_header = f'| {title_table:^69} |'

    print('-' * len(title_table_header))
    print(title_table_header)
    print('-' * len(title_table_header))

    #Tampilan Header Tiap Coloumn
    header1, header2, header3, header4, header5  = 'Index', 'Nama', 'Stock', 'Harga Satuan', 'Harga Total'
    table_header = f'| {header1:<7} | {header2:<13} | {header3:<5} | {header4:<16} | {header5:<16} |'

    print('-' * len(table_header))
    print(table_header)
    print('-' * len(table_header))

    #Tampilan List Value Dari Dalam List barang_gudang
    for i in range(len(barang_gudang)) :
          coloumn_barang = f"| {i:<7} | {barang_gudang[i]['nama']:<13} | {barang_gudang[i]['stock']:<5} | Rp.{barang_gudang[i]['hargasatuan']:<13,} | Rp.{barang_gudang[i]['hargatotal']:<13,} |"
          print(coloumn_barang)
    print('-' * len(table_header))

def menambah_barang():
   print(end="\033c")
   tampilan_barang()
   namaBarang = input('Masukkan Nama Barang : ')
   stockBarang = int(input('Masukkan Stock Barang : '))
   hargaBarang = int(input('Masukkan Harga Barang : Rp. '))
   barang_gudang.append({ 'nama': namaBarang.title(), 'stock': stockBarang, 'hargasatuan': hargaBarang, 'hargatotal': stockBarang * hargaBarang })
   print(end="\033c")
   tampilan_barang()

def menghapus_barang():
    print(end="\033c")
    tampilan_barang()
    indexBarang = int(input('Masukkan Index Barang Yang Ingin Dihapus : '))
    if indexBarang >= 0 and indexBarang < len(barang_gudang):
        del barang_gudang[indexBarang]
        print(end="\033c")
        print(f'Barang Dengan Index No.{indexBarang} Berhasil Dihapus !!! ')
        tampilan_barang()
    else:
        print(f'\nNomor Index {indexBarang} Yang Anda Masukkan Tidak Tersedia Di List Barang')

def mengedit_barang():
    print(end="\033c")
    tampilan_barang()
    indexBarangbaru = int(input('Masukkan index barang yang ingin diedit : '))
    if indexBarangbaru >= 0 and indexBarangbaru < len(barang_gudang):
     namaBarangbaru = input('Masukkan Nama Barang : ')
     stockBarangbaru = int(input('Masukkan Stock Barang : '))
     hargaBarangbaru = int(input('Masukkan Harga Barang : Rp. '))
     barang_gudang[indexBarangbaru] = ({ 'nama': namaBarangbaru.title(), 'stock': stockBarangbaru, 'hargasatuan': hargaBarangbaru, 'hargatotal': stockBarangbaru * hargaBarangbaru })
     print(end="\033c")
     print(f'Barang Dengan Index No.{indexBarangbaru} Berhasil Di Edit !!! ')
     tampilan_barang()

    else:
     print(f'\nNomor Index {indexBarangbaru} Yang Anda Masukkan Tidak Tersedia Di List Barang')


     
     
     


while True :

    # Menu Utama
    pilihanMenu = input('''
Selamat Datang di Gudang Toko Komputer

List Menu :
1. Menampilkan Daftar Barang
2. Keluar Dari Aplikasi

Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
     print(end="\033c")
     tampilan_barang()
     while True:
        PilihanMenu()
        # Menu Menambah Barang Ke Dalam Gudang
        if(pilihanselanjutnya == '1'):
           menambah_barang()
           
    
        # Menu Menghapus Barang Dari Dalam Gudang
        elif(pilihanselanjutnya == '2') :
           menghapus_barang()


        # Menu Mengedit Barang Di Dalam Gudang
        elif(pilihanselanjutnya == '3'):
            mengedit_barang()

        # Exit Ke Menu Utama
        elif(pilihanselanjutnya == '4') :
         print(end="\033c")
         break
    
        # Exit Dari Program
    elif(pilihanMenu == '2'):
        print(end="\033c")
        break

    else:
       print(end="\033c")
       print('Invalid Input, Silahkan Masukkan Input Yang Sesuai')
         
    

    