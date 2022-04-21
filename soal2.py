#membuka file
file = open('data_soal2.txt')

#inisiasi variable
hasil = ''
soal = ''
kunci = ''

#untuk mengcek setiap baris dalam file
for line in file:

    #memisahkan dengan karakter '||'
    hasil = line.split('||')

    #memasukkan soal
    soal = hasil[0]

    #memasukkan kunci
    kunci = hasil[1]

    #menghapus karakter yang ada di kanan
    kunci = kunci.rstrip()

    #menghapus karakter yang ada di kiri
    kunci = kunci.lstrip()

    #untuk mengatasi sensitive case
    kunci = kunci.lower()

    #cetak soal
    print(soal, end='\n')

    #user menginputkan jawaban
    jawab = input('Jawab :')

    #supaya sama dengan kunci (mengatasi sensitive case)
    jawab = jawab.lower()

    #mengcek jawaban apakah benar
    if jawab == kunci:
        print('Jawaban Benar !')
    else :
        print('Jawaban salah !')


'''SEKIAN DAN TERIMAKASIH DARI SAYA, KALAU MASIH EROR BERARTI DEVICE ANDA KUNO:)'''

