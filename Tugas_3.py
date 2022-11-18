barang = "rinso cair"
nobarang = "0001"
tanggal_masuk = "2002-03-21"

kode = "RC0001/2022/03"
myorder = "SAYA MEMESAN {} barang ,{} nobarang,{} tanggal_masuk"
print (myorder.format(barang,nobarang,tanggal_masuk))








import datetime

y=datetime.datetime(2022,3,21)

print(y)

x = datetime.datetime.now()
print("hari ini",x)

print("tahun:",x.year)
print("bulan:",x.month)
print("day:",x.day)

print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%w"))

