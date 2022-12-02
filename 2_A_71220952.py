k = input('Masukkan kata: ')

#Cetak_kata
def cetak_kata(str): 
    panjang=len(str) 
    if panjang % 2 == 0 :
        return str[0]+str[1]+str[2]+ 'dan' +str[-3]+[-2]+[-1]
    else:
        mid= int(panjang/2)
        return str[mid-1]+str[mid]+str[mid1]

a=input('Masukkan kata: ')
b=membuathuruf(a)
print('Huruf yang diambil pada ', a , 'adalah', b)

    