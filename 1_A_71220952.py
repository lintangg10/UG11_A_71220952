print('======= Program Manipulasi String ======')
print('pilihan menu:')
print('1. Hitung kata')
print('2. Ubah Kata')
m = input('Pilihan anda: ')

def hitung():
    kalimat1 = input ('Masukkan sebuah kalimat/kata: ')
    kt = input ('Masukkan kata yang ingin anda hitung: ')
    x = kalimat1.count(kt)
    print('Terdapat sebanyak', x, 'kata', kt, 'didalam kalimat')
    return x

def ubah():
    kalimat = input ('Masukkan sebuah kalimat/kata: ')
    gg = input ('Masukkan kata yang ingin diubah: ')
    pg = input('Masukkan kata pengganti: ')

    ganti = kalimat.replace(gg, pg)

    print(f'String berhasil Diubah menajadi{ganti}')
    return ganti

if m == '1' :
    hitung()
elif m == '2' :
    ubah()
else :
    print('Pilihan yang anda input tidak terdaftar di daftra pilihan')
