import random

#Kadir Aydın
print("                                  ")
print("GİRİŞ YAPMA SİSTEMİNE HOŞGELDİNİZ👋")
print("                                  ")
print("⬇⬇⬇SİSTEME KAYIT OLMAK İÇİN BİLGİLERİ DOLDURUN⬇⬇⬇")
print("                                  ")

k_adı_o = input("KULLANICI ADI OLUŞTURUN: ")
şif_o = input("ŞİFRENİZİ OLUŞTURUN: ")
şif_onay = input("ŞİFRENİZİ ONAYLAMAK İÇİN BİR DAHA YAZIN: ")

if şif_o == şif_onay:
    print("                                  ")
    print("KULLANICI ADI VE ŞİFRENİZ OLUŞTURULDU VE ONAYLANDI✔")
    print("ŞİMDİ GİRİŞ YAPABİLİRSİNİZ")
    print("                                  ")
    k_adı = input("SİSTEME GİRİŞ YAPMAK İÇİN KULLANICI ADINIZI GİRİN: ")
    şif = input("SİSTEME GİRİŞ YAPMAK İÇİN ŞİFRENİZİ GİRİN: ")
    tk_kod = random.randint(1000,9999)
    print("TEK KULLANIMLIK ŞİFRENİZ: " ,tk_kod)
    tk_kod_o = int(input("TEK KULLANIMLIK ŞİFRENİZİ GİRİN: "))

    if k_adı == k_adı_o and şif == şif_o and tk_kod == tk_kod_o:
        print("✔️SİSTEME BAŞARIYLA GİRİŞ YAPILDI  ✔️")
        print("HOŞGELDİNİZ!")
        print("@_kadiraydnn_")
        #Kadir Aydın

    else:
        print("❌ HATA , TEKRAR DENEYİN ❌")


else:
    print("⚠ŞİFRELER EŞLEŞMİYOR⚠")

#Kadir Aydın
