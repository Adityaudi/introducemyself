import emoji
import os

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
NIM         = 12211282
NAME        = "Aditya Udi Anggoro"
STUDY       = "Sistem Informasi"
LESSON      = "LOGIKA & ALGORITMA"
DOSEN       = "Ibu Ayuni Asistyasari"
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # TUGAS 1 
print ('\033[33m-    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -\033[33m\n')
INPUT_NAME = input("Masukan nama anda:  ")
print ("Hai hai\U0001F44B\U0001F44B " + INPUT_NAME + " Welcome to the club\U0001F601\n")

print ('\033[37m[ 1 ]' ' \033[36mSOAL NO.1')
print ('\033[37m[ 2 ] ' '\033[36mSOAL NO.2\n\n')
print ('\033[37m ---------------------')
CHOICE_SOAL = input('\033[36mTentukan soal yang ingin dipilih: \033[37m')
if CHOICE_SOAL == '1':
    os.system("feh soal/soal1.png")
    os.system("clear")
    print ('\033[37m  >> KESIMPULAN JAWABAN. ')
    print ('\033[36m | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |')
    print ('\033[36m |                                                                                               |')
    print ('\033[37m | Jadi, disini ibu akan memesan dengan 5 KG telur untuk membuat kue                             |')
    print ('\033[37m | dengan harga perkilo telurnya adalah Rp 26.000 dan ibu kepasar naik angkot yang saya          |')
    print ('\033[37m | categorykan kedalam biaya lain lain sebesar Rp 3.500 sekali naik angkot dan jika PP           |')
    print ('\033[37m | maka Rp 7.000. Ternyata ibu hanya membawa uang Rp 200.000. Nah jadi expetasi kita uang        |')
    print ('\033[37m | kembalian ibu adalah Rp 63.000. Jadi sisa kembalian nya adalah ' + '\033[33mRp 63.000                         \033[37m|') 
    print ('\033[37m |                                                                                               |')
    print ('\033[36m | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |\n\n')
    START_PROGRAMS = input('\033[36mJalankan Programs: Enter Y for yes or N for no \033[37m')

    if START_PROGRAMS in ['y', 'Y', 'yes']:
        os.system("clear")
        print ("Hai hai\U0001F44B\U0001F44B " + INPUT_NAME + " Welcome to the programs nomor 1\U0001F601\n")
        print ('\033[37m  >> MENU BELANJA. ')
        print ('\033[36m | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|')
        print ('\033[36m |                                                                                                  |')
        print ('\033[37m |      [+] Terigu >> Rp 35.000/Kg                 [+] Baking Soda  >> Rp 5.000                     |')
        print ('\033[37m |      [+] Gula   >> Rp 15.000/Kg                 [+] Mie Instan  >> Rp 2.500                      |')
        print ('\033[37m |      [+] Garem  >> Rp 1.000                     [+] Minyak Goreng >> Rp 29.000                   |')
        print ('\033[37m |      [+] Beras Premium  >> Rp 65.000/5Liter     [+] Mentega  >> Rp 6.000                         |')
        print ('\033[37m |      [+] Telor  >> Rp 26.000/Kg                                                                  |')
        print ('\033[37m |                                                                                                  |')
        print ('\033[36m | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  |\n\n')

        NAME_PRODUCT = input ("Name Product:  \033[37m")
        if NAME_PRODUCT in ['Terigu', 'terigu']:
                ID_PRODUCT = 'Terigu'
                PRICE_PRODUCT = 35000
        elif NAME_PRODUCT in ['Telor', 'telor']:
                ID_PRODUCT = 'Telor'
                PRICE_PRODUCT = 26000
        elif NAME_PRODUCT in ['Gula', 'gula']:
                ID_PRODUCT = 'Gula'
                PRICE_PRODUCT = 15000
        elif NAME_PRODUCT in ['Garem', 'garem']:
                ID_PRODUCT = 'Garem'
                PRICE_PRODUCT = 1000
        elif NAME_PRODUCT in ['Beras Premium', 'beras Premium']:
                ID_PRODUCT = 'Beras Premium'
                PRICE_PRODUCT = 65000
        elif NAME_PRODUCT in ['Baking Soda', 'baking Soda']:
                ID_PRODUCT = 'Baking Soda'
                PRICE_PRODUCT = 5000
        elif NAME_PRODUCT in ['Mie Instan', 'mie Instan']:
                ID_PRODUCT = 'Mie Instan'
                PRICE_PRODUCT = 2500
        elif NAME_PRODUCT in ['Minyak Goreng', 'minyak Goreng']:
                ID_PRODUCT = 'Minyak Goreng'
                PRICE_PRODUCT = 29000
        elif NAME_PRODUCT in ['Mentega', 'mentega']:
                ID_PRODUCT = 'Mentega'
                PRICE_PRODUCT = 6000
        else:
            print('Produk yang di ketik. Not Found!')
            print ("             program selesai.\U0001F570\U0001F570\U0001F570 \n\n")
            exit()
            
        QTY = int(input("\033[36mQty:  \033[37m"))
        OTHER = int(input("\033[36mOther:   Rp. \033[37m"))
        CONFIRM = input("\033[33mKlik OK untuk melanjutkan! ")
    #   Function Hitung
        TOTAL = PRICE_PRODUCT * QTY
        YANG_HARUS_DIBAYAR = TOTAL + OTHER
        if CONFIRM == 'OK':
            os.system("clear")
            print ('\033[37m ||==================================================================================================||')
            print ('\033[37m ||                                                                                                  ||')
            print ('\033[37m ||  NAME PRODUCT                                  |     PRICE       |    QTY     |      JUMLAH      ||')
            print ('\033[37m ||                                                                                                  ||')
            print ('\033[37m ||==================================================================================================||')
            print ('\033[37m ||  ', ID_PRODUCT,'                                       |     Rp ',PRICE_PRODUCT,'  |   ',QTY,'      |      Rp ',TOTAL,  ' ||')
            print ('\033[37m ||                                                                                ------------------||')
            print ('\033[37m || Total Belanja                                                                   :Rp ',TOTAL ,   '     ||')
            print ('\033[37m || Biaya lainnya                                                                   :Rp ',OTHER  ,   '         ||')
            print ('\033[37m || Yang harus dibayar                                                              :Rp ',TOTAL + OTHER,'     ||')

            UANG_IBU = int(input("\033[33mDibayar:                                                                      Rp.     "))
            print ('\033[37m || Kembalian                                                                    :Rp.     ',UANG_IBU - YANG_HARUS_DIBAYAR,'    ||')
            print ('\033[37m ||                                                                                                  ||')
            print ('\033[37m ||                                                                                                  ||')
            print ('\033[37m ||                                                                                                  ||')
            print ('\033[37m ||                                                                                                  ||')
            print ('\033[37m ||                                                                                                  ||')
            print ('\033[37m ||==================================================================================================||')
            print ("             program selesai. Terimakasih telah menggunakan programs no1\U0001F570\U0001F570\U0001F570 \n\n")
            exit()
        else: 
            print ("             Harap pilih sesuai ketentuan!.\U0001F570\U0001F570\U0001F570 \n\n")
            print ("             program selesai.\U0001F570\U0001F570\U0001F570 \n\n")
        
    else: 
        print ("             Harap pilih sesuai ketentuan!.\U0001F570\U0001F570\U0001F570 \n\n")
        print ("             program selesai.\U0001F570\U0001F570\U0001F570 \n\n")
        exit()
else:
    print ("             soal nomor 2sedang dikerjakan!.\U0001F570\U0001F570\U0001F570 \n\n")
    print ("             program selesai.\U0001F570\U0001F570\U0001F570 \n\n")
    exit()
