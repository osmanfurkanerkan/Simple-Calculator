def sayıları_al():
    number1 = int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz: "))
    number2 = int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz: "))
    return number1, number2

def toplama(number1, number2):
    return number1 + number2

def çıkarma(number1, number2):
    return number1 - number2

def çarpma(number1, number2):
    return number1 * number2

def bölme(number1, number2):
    while number2==0:
        print("Hata: bir sayı 0a bölünemez!. Lütfen yeni bir ikinci sayı giriniz ")
        number2 = int(input("Yeni ikinci sayıyı giriniz: "))
    return number1/number2

def main():
    print("WELCOME CALCULATOR")

    number1, number2 = sayıları_al()
    işlem_sayısı = 0
    Flag1 = True

    while Flag1:
        while True:
            işlem = int(input("Hangi işlemi yapmak istersiniz? (1-toplama, 2-çıkarma, 3-çarpma, 4-bölme) : "))
            if işlem in [1, 2, 3, 4]:
                break
            else:
                print("Geçerli bir işlem numarası giriniz!")

        if işlem == 1:
            sonuç = toplama(number1, number2)
        elif işlem == 2:
            sonuç = çıkarma(number1, number2)
        elif işlem == 3:
            sonuç = çarpma(number1, number2)
        else:
            sonuç = bölme(number1, number2)

        # Bölme işlemi geçerli değilse (sıfıra bölme hatası) işlemi tekrarlama
        if sonuç is not None:
            işlem_sayısı += 1
            print(f"{işlem_sayısı}. işlem sonucunda sonuç = {sonuç}")

        # Kullanıcıya devam etmek isteyip istemediğini sor
        other_cal = input("İşleme devam etmek ister misiniz? (y/Y/n/N): ")
        if other_cal in ["n", "N"]:
            Flag1 = False
            print("Hesap makinesindençıkış yapılıyor")
        elif other_cal in ["y", "Y"]:
            number1 = sonuç  # Önceki sonucu yeni işlem için birinci sayı yap
            number2 = int(input("Yeni ikinci sayıyı giriniz: "))  # Yeni ikinci sayıyı al

main()







