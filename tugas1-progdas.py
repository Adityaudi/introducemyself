import emoji
# # Set variables NIM, Name, Umur, Prodi, Sedang_apa

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
NIM         = 12211282
NAME        = "Aditya Udi Anggoro"
AGE         = 19
STUDY       = "Sistem Informasi"
DOSEN       = "calon ibu gina"

# Print Type data python with variable
print ("----------------------------------------------------------------------\n")
print ("Hai teman-teman dan " + DOSEN + " hehe\U0001F44B\U0001F601.. berikut adalah biodata ku:\n")
print ("")
print ("----------------------------------------------------------------------")
print ("\U0001F22F", NIM)
print ("\U0001F466 " + NAME)
print ("\U0001F4C6", AGE)
print ("\U0001F3DA " + STUDY)
print ("----------------------------------------------------------------------\n\n")

# Print kalimat pertanyaan berupa string dan mengoutputkan nya
print ("----------------------------------------------------------------------\n")
NICKNAME = input("Haii\U0001F44B, " + NAME + " aku jadinya manggil kamu siapa nih??  ")
# CALL_ME = NICKNAME
print ("Wahh salam kenal yah\U0001F44B " + NICKNAME + " nama yang bagus banget, pasti aku cepet untuk mengingatnya nih hehe\U0001F601..\n")
print ("----------------------------------------------------------------------\n\n")

# Print kalimat pertanyaan berupa hanya 2 jawaban yang harus dijawab yang berupa boolean 
print ("----------------------------------------------------------------------\n")
QNA = input("ohh iyah btw, Kamu punya komentar tentang aku gakk?? Enter Y for yes or N for no \n")
if QNA in ['n', 'N', 'no']:
    print ("yahh oke deh nice to meet youu " + NICKNAME)
    print ("----------------------------------------------------------------------")
    print ("             program selesai.\U0001F570\U0001F570\U0001F570 \n\n")
    exit()
elif QNA in ['y', 'Y', 'yes']:
    COMMENT = input(
        '''
        '''
    )
    print ("Comment berhasil di sampan thank you\U0001F601")
    print ("----------------------------------------------------------------------")
    print ("             program selesai.\U0001F570\U0001F570\U0001F570 \n\n")
    exit()
else:
    print ("----------------------------------------------------------------------")
    print ("             program selesai.\U0001F570\U0001F570\U0001F570 \n\n")
    exit()

