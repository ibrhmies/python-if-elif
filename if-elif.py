x = int(input("Bir sayı giriniz: "))

if (x > 0):
    print("x pozitiftir.")
elif (x == 0):           # elif komutu if komutuna bağlı başka bir koşuldur 
                         #if komutu karşılanmıyorsa elif e bakılır 
                         # o da karşılanmıyorsa else komutu devreye girer
    print("x sıfırdır.")
else:                    # else komutundan sonra paranteze gerke yoktur else if komutunun karşılanmadığı zaman devreye girer.
    print("x negatiftir.")
    