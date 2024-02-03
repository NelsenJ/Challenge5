print("\t TiketBus \t")
print("-"*25)
print("Kode Kota :")
print("1. Prabumulih")
print("2. Muara Enim")
print("3. Lubuklinggau")
kotaselect = int( input("Pilihan Kota (1/2/3) : "))
print("Kode Kelas :")
print("1. Ekonomi")
print("2. Bisnis")
print("3. Eksekutif")
classselect = int( input("Pilihan Ketas (1/2/3) : "))
tiket = int(input("Banyak TIket : "))
if kotaselect == 1:
    kodepromo = 0
    if classselect == 1:
        harga = 100000
    elif classselect == 2:
        harga = 400000
    elif classselect == 3:
        harga = 700000
elif kotaselect == 2:
    kodepromo = input("Kode Promo : ")
    if classselect == 1:
        harga = 200000
    elif classselect == 2:
        harga = 500000
    elif classselect == 3:
        harga = 800000
elif kotaselect == 3:
    kodepromo = input("Kode Promo : ")
    if classselect == 1:
        harga = 300000
    elif classselect == 2:
        harga = 600000
    elif classselect == 3:
        harga = 900000
subtotal = harga*tiket
if kodepromo == "igs":
    diskon = int(subtotal/10)
else:
    diskon = 0
TotalBayar = subtotal - diskon




print("-"*25)
print("Harga Tiket :\t Rp. ", harga)
print("Sub Total :\t Rp. ", subtotal)
print("Diskon :\t Rp. ", diskon)
print("Total Bayar :\t Rp. ", TotalBayar)
