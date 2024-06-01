print("BODY MASS INDEX CALCULATION PROGRAM")



try:
    isim = input("Lütfen İsminizi Giriniz : ")
    soyisim = input("Lütfen Soyisminizi Giriniz : ")
    yas = int(input("Lütfen Yaşınızı Giriniz: "))
    if yas <= 18:
        print(f"Sayın, {isim}\t{soyisim} \n 18 yaş altı için vücut kitle indeksi hesaplanmamaktadır.")
        exit()
    else:
        kilo = int(input("Lütfen Kilonuzu Giriniz(kg) :"))
        boy = float(input("Lütfen Boyunuzu Giriniz(m) : "))
        endex = kilo / (boy * boy)

    if yas <= 18:
        print(f"Sayın, {isim}\t{soyisim} \n 18 yaş altı için vücut kitle indeksi hesaplanmamaktadır.")

    elif yas >= 19 and yas <= 24:
        print(f"Sayın, {isim}\t{soyisim} \n Yaşınıza göre ideal vücut kitle indeks aralığı 19-24 BMI'dır.")
    elif yas >= 25 and yas <= 34:
        print(f"Sayın, {isim}\t{soyisim} \n Yaşınıza göre ideal vücut kitle indeks aralığı 20-25 BMI'dır.")
    elif yas >= 35 and yas <= 44:
        print(f"Sayın, {isim}\t{soyisim} \n Yaşınıza göre ideal vücut kitle indeks aralığı 21-26 BMI'dır.")
    elif yas >= 45 and yas <= 54:
        print(f"Sayın, {isim}\t{soyisim} \n Yaşınıza göre ideal vücut kitle indeks aralığı 22-27 BMI'dır.")
    elif yas >= 55 and yas <= 64:
        print(f"Sayın, {isim}\t{soyisim} \n Yaşınıza göre ideal vücut kitle indeks aralığı 23-28 BMI'dır.")
    else:
        print(f"Sayın, {isim}\t{soyisim} \n Yaşınıza göre ideal vücut kitle indeks aralığı 224-29 BMI'dır.")

    if endex <= 18.4:
        print(f'Vücut Kitle Endeksiniz : {endex} BMI -> Zayıf')
        print("Boyunuza oranla kilonuz yetersizdir.Bu sebeple diyetisyen eşliğinde sağlıklı bir şekilde kilo almalısınız.")

    elif endex >= 18.5 and endex <= 24.9:
        print(f'Vücut Kitle Endeksiniz : {endex} BMI -> Normal')
        print("İdeal kilodasınız.Düzenli, dengeli ve sağlıklı beslenmeye devam etmelisiniz. ")

    elif endex >= 25 and endex <= 29.9:
        print(f'Vücut Kitle Endeksiniz : {endex} BMI -> Fazla Kilolu')
        print("Boyunuza oranla kilonuz fazladır.Bu sebeple uygun diyet ile fazla kilolarından kurtulmalısınız.")

    elif endex >= 30 and endex <= 34.9:
        print(f'Vücut Kitle Endeksiniz : {endex} BMI -> Şişman(Birinci Derece Obez)')
        print("Kilonuz sağlık açısından risk oluşturabilecek düzeydedir.Bu sebeple diyetisyen yardımıyla kilo vermelisiniz.")

    elif endex >= 35 and endex <= 44.9:
        print(f'Vücut Kitle Endeksiniz : {endex} BMI -> Şişman(İkinci Derece Obez)')
        print("Kalp ve damar hastalıkları bakımından risk altındasınız.Kilo vermek için diyetisyene başvurmalısınız.")

    else:
        print(f'Vücut Kitle Endeksiniz : {endex} BMI -> Aşırı Şişman(Üçüncü Derece Obez)')
        print("Hastalık gelişme riskiniz oldukça yüksektir.Bu sebeple hekim ve diyetisyen eşliğinde kilo vermelisiniz.")

except ValueError:
    print("Lütfen Bilgilerinizi Kontol Ediniz!")
    exit()
except SyntaxError:
    print("Lütfen Bilgilerinizi Kontol Ediniz!")
    exit()
except TypeError:
    print("Lütfen Bilgilerinizi Kontol Ediniz!")