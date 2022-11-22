import datetime

#Capstone project Modul 1
#Aji Wibowo Sanjaya
#Case Study: Data Karyawan Perusahaan

#Data awal.
dk = {'101':['Maria Triningsih', '28/11/1989', 'P', 'General Manager', '0813-9457-6214'],
'102':['Luthfie Simanjuntak', '03/08/1993', 'L', 'Manager', '0825-4391-8888'],
'103':['Evan Hartanto', '15/04/1990', 'L', 'Admin Staff', '0829-6341-5987'],
'104':['Stevani Gloria', '20/05/1992', 'P', 'Admin Staff', '0813-4621-9393'],
'105':['Muhammad Fajar', '09/12/1997', 'L', 'Logistic Staff', '0812-2543-9180']}

#Function to print dictionary into table format
def print_table(dict):
    print("{:5} {:<20} {:<15} {:<15} {:<18} {:<10}".format('ID','Nama','Tanggal Lahir','Jenis Kelamin','Jabatan','No. HP'))
    for k, v in dict.items():
        name, date, jk, jabatan, no_HP = v
        print("{:<5} {:<20} {:<15} {:<15} {:<18} {:<10}".format(k, name, date, jk, jabatan, no_HP))

#Function to print data based on ID
def print_data_id(dict, ID):
    print("{:5} {:<20} {:<15} {:<15} {:<18} {:<10}".format('ID','Nama','Tanggal Lahir','Jenis Kelamin','Jabatan','No. HP'))
    print("{:<5} {:<20} {:<15} {:<15} {:<18} {:<10}".format(ID, dict[ID][0], dict[ID][1], dict[ID][2], dict[ID][3], dict[ID][4]))

#Name capitalizer function
def capitalizer(words):
    lower_words = words.lower()
    split_words = lower_words.split(' ')
    cap_words = [word.capitalize() for word in split_words]
    return ' '.join(cap_words)

#Phone number splitter function
def no_HP_separator(no_HP):
    split_n = 4
    split_no_HP = [no_HP[i:i+split_n] for i in range(0,len(no_HP),split_n)]
    return '-'.join(split_no_HP)

#Stopper digunakan sebagai penanda untuk menghentikan while loop.
stopper = True
while stopper:
    print('\nMENU UTAMA(E)')
    print('1. LIHAT DATA KARYAWAN')
    print('2. TAMBAH DATA KARYAWAN')
    print('3. UBAH DATA KARYAWAN')
    print('4. HAPUS DATA KARYAWAN')
    print('5. KELUAR\n')
 
    menu = int(input('PILIH MENU(E): '))
    print(f'ANDA MEMLIH OPSI {menu}')

    if menu == 1:
        stopper_A = True
        while stopper_A:
            print('\nMENU LIHAT DATA (A)')
            print('1. LIHAT DATA SELURUH KARYAWAN.')
            print('2. LIHAT DATA KARYAWAN BERDASARKAN ID.')
            print('3. KEMBALI KE MENU UTAMA (E).\n')
            menu_A = int(input('PILIH MENU(A):'))
            print(f'ANDA MEMILIH OPSI {menu_A}')
            if menu_A == 1:
                print_table(dk)
            elif menu_A == 2:
                ID = input('\nMASUKAN ID KARYAWAN: ')
                print('')
                if ID in dk.keys():
                    print_data_id(dk,ID)
                else:
                    print('\nID TIDAK TERDAFTAR.\n')
            elif menu_A == 3:
                stopper_A = False
    elif menu == 2:
        stopper_B = True
        while stopper_B:
            print('\nMENU TAMBAH DATA (B)')
            print('1. TAMBAH DATA KARYAWAN.')
            print('2. KEMBALI KE MENU UTAMA.\n')
            menu_B = int(input('PILIH MENU(B): '))
            print(f'ANDA MEMILIH OPSI {menu_B}.')
            if menu_B == 1:
                ID = input('\nMASUKAN ID KARYAWAN YANG INGIN DITAMBAHKAN: ')
                if ID in dk.keys():
                    print('\nNOMOR ID SUDAH TERPAKAI. KEMBALI KE MENU B.\n')
                else:
                    nama = capitalizer(input('MASUKAN NAMA KARYAWAN: '))
                    stopper_tanggal = True
                    while stopper_tanggal:
                        tanggal_lahir = input('MASUKAN TANGGAL LAHIR KARYAWAN (DD/MM/YYYY): ')
                        try:
                            datetime.datetime.strptime(tanggal_lahir, '%d/%m/%Y')
                            stopper_tanggal = False
                        except:
                            print("FORMAT TANGGAL SALAH, MASUKAN SESUAI FORMAT BERIKUT: DD/MM/YYYY.\n")
                    jenis_kelamin = input('MASUKAN JENIS KELAMIN KARYAWAN (L/P): ').upper()
                    jabatan = capitalizer(input('MASUKAN JABATAN KARYAWAN: '))
                    no_HP = no_HP_separator(input('MASUKAN NO. HP KARYAWAN: '))
                    simpan = input(f'\nID: {ID}\nNAMA: {nama}\nTANGGAL LAHIR: {tanggal_lahir}\nJENIS KELAMIN: {jenis_kelamin}\nJABATAN: {jabatan}\nNO. HP: {no_HP}\nAPAKAH ANDA INGIN MENYIMPAN DATA BERIKUT? (Y/N): ')
                    if simpan.lower() == 'y':
                        dk[ID] = [nama, tanggal_lahir, jenis_kelamin, jabatan, no_HP]
                        print('\nDATA BARU TELAH TERSIMPAN. KEMBALI KE MENU B\n')
                    else:
                        print('\nDATA BARU TIDAK TERSIMPAN. KEMBALI KE MENU B\n')
            elif menu_B == 2:
                stopper_B = False
    elif menu == 3:
        stopper_C = True
        while stopper_C:
            print('\nMENU UBAH DATA (C)')
            print('1. UBAH DATA KARYAWAN.')
            print('2. KEMBALI KE MENU UTAMA (E).\n')
            menu_C = int(input('PILIH MENU(C): '))
            print(f'ANDA MEMILIH OPSI {menu_C}.')
            if menu_C == 1:
                print_table(dk)
                ID = input('\nMASUKAN ID KARYAWAN YANG INGIN DIUBAH: ')
                if ID in dk.keys():
                    print('')
                    print_data_id(dk,ID)
                    stopper_C_1 = True
                    while stopper_C_1:
                        print('\n MENU PEMILIHAN KOLOM:')
                        print('1. NAMA.')
                        print('2. TANGGAL LAHIR.')
                        print('3. JENIS KELAMIN.')
                        print('4. JABATAN.')
                        print('5. NO. HP')
                        print('KETIK ANGKA SELAIN ANGKA DIATAS UNTUK KEMBALI KE MENU C.\n')
                        p = int(input('PILIH KOLOM YANG INGIN DIGANTI (1-5): '))
                        print('')
                        if p == 1:
                            print('MENGANTI KOLOM NAMA.')
                            nama_baru = capitalizer(input('MASUKAN DATA NAMA BARU: '))
                            simpan = input(f'NAMA: {nama_baru}\nAPAKAH ANDA INGIN MENYIMPAN DATA BARU? (Y/N): ')
                            if simpan.lower() == 'y':
                                dk[ID][0] = nama_baru
                                print('\nDATA BARU TELAH TERSIMPAN.\n')
                                print_data_id(dk,ID)
                                print('')
                            else:
                                print('\nDATA BARU TIDAK TERSIMPAN.\n')
                        elif p == 2:
                            print('MENGANTI KOLOM TANGGAL LAHIR.')
                            stopper_tanggal = True
                            while stopper_tanggal:
                                tanggal_lahir_baru = input('MASUKAN DATA TANGGAL LAHIR BARU (DD/MM/YYYY): ')
                                try:
                                    datetime.datetime.strptime(tanggal_lahir_baru, '%d/%m/%Y')
                                    stopper_tanggal = False
                                except:
                                    print("FORMAT TANGGAL SALAH, MASUKAN SESUAI FORMAT BERIKUT: DD/MM/YYYY.\n")
                            simpan = input(f'TANGGAL LAHIR: {tanggal_lahir_baru}\nAPAKAH ANDA INGIN MENYIMPAN DATA BARU? (Y/N): ')
                            if simpan.lower() == 'y':
                                dk[ID][1] = tanggal_lahir_baru
                                print('\nDATA BARU TELAH TERSIMPAN.\n')
                                print_data_id(dk,ID)
                                print('')
                            else:
                                print('\nDATA BARU TIDAK TERSIMPAN.\n')
                        elif p == 3:
                            print('MENGANTI KOLOM JENIS KELAMIN.')
                            jenis_kelamin_baru = capitalizer(input('MASUKAN DATA JENIS KELAMIN BARU (L/P): '))
                            simpan = input(f'JENIS KELAMIN: {jenis_kelamin_baru}\nAPAKAH ANDA INGIN MENYIMPAN DATA BARU? (Y/N): ')
                            if simpan.lower() == 'y':
                                dk[ID][2] = jenis_kelamin_baru
                                print('\nDATA BARU TELAH TERSIMPAN.\n')
                                print_data_id(dk,ID)
                                print('')
                            else:
                                print('\nDATA BARU TIDAK TERSIMPAN.\n')
                        elif p == 4:
                            print('MENGANTI KOLOM JABATAN.')
                            jabatan_baru = capitalizer(input('MASUKAN DATA JABATAN BARU: '))
                            simpan = input(f'JABATAN: {jabatan_baru}\nAPAKAH ANDA INGIN MENYIMPAN DATA BARU? (Y/N): ')
                            if simpan.lower() == 'y':
                                dk[ID][3] = jabatan_baru
                                print('\nDATA BARU TELAH TERSIMPAN.\n')
                                print_data_id(dk,ID)
                                print('')
                            else:
                                print('\nDATA BARU TIDAK TERSIMPAN.\n')
                        elif p == 5:
                            print('MENGANTI KOLOM NO.HP .')
                            no_HP_baru = no_HP_separator(input('MASUKAN DATA NO. HP BARU: '))
                            simpan = input(f'NO. HP: {no_HP_baru}\nAPAKAH ANDA INGIN MENYIMPAN DATA BARU? (Y/N): ')
                            if simpan.lower() == 'y':
                                dk[ID][4] = no_HP_baru
                                print('\nDATA BARU TELAH TERSIMPAN.\n')
                                print_data_id(dk,ID)
                                print('')
                            else:
                                print('\nDATA BARU TIDAK TERSIMPAN.\n')
                        else:
                            stopper_C_1 = False
                else:
                    print('\nID TIDAK TERDAFTAR.\n')
            elif menu_C == 2:
                stopper_C = False
    elif menu == 4:
        stopper_D = True
        while stopper_D:
            print('\nMENU HAPUS DATA (D)')
            print('1. HAPUS DATA KARYAWAN.')
            print('2. KEMBALI KE MENU UTAMA (E).\n')
            menu_D = int(input('PILIH MENU(D): '))
            print(f'ANDA MEMILIH OPSI {menu_D}.')
            if menu_D == 1:
                print_table(dk)
                ID = input('\nMASUKAN ID KARYAWAN YANG INGIN DIHAPUS: ')
                if ID in dk.keys():
                    print_data_id(dk,ID)
                    hapus = input('APAKAH ANDA YAKIN AKAN MENGHAPUS DATA KARYAWAN BERIKUT ?(Y/N): ')
                    if hapus.lower() == 'y':
                        del(dk[ID])
                        print('\nDATA TERHAPUS.\n')
                    else:
                        print('\nDATA TIDAK TERHAPUS, KEMBALI KE MENU D.\n')
                else:
                    print('\nID TIDAK TERDAFTAR.\n')
            elif menu_D == 2:
                stopper_D = False
    elif menu == 5:
        print('\nSESSION ENDED.\n')
        stopper = False
    else:
        print('\nPILIHAN YANG ANDA MASUKAN SALAH.\n')
