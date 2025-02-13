def sayıları_al():
    try:
        number1 = int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz: "))
    except:
        print("Geçersiz giriş! Lütfen bir sayı girin.")
    return number1

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

def üs_Al(number1,number2):
    return number1**number2

def kök_hesapla(number1):
    return number1**(1/2)

def faktöriyel_hesap(number1):
    faktöriyel=1
    for i in range(1,(number1+1)):
        faktöriyel*=i
    return faktöriyel

def main():
    print("WELCOME CALCULATOR")
    işlem_sayısı = 0
    Flag1 = True
    result = None  
    while Flag1:
        while True:
            try:
                işlem = int(input("Hangi işlemi yapmak istersiniz? (1-toplama, 2-çıkarma, 3-çarpma, 4-bölme , 5-üs alma , 6-kök alma , 7-faktöriyel hesaplama) : "))
                if işlem in [1, 2, 3, 4, 5, 6, 7]:
                    break
                else:
                    print("Geçersiz sayı! Lütfen yalnızca 1, 2, 3, 4, 5, 6, 7'yi girin.")
            except ValueError:
                print("Geçersiz giriş! Lütfen bir sayı girin.")

        
        if result is None:  
            number1 = sayıları_al()
        else:
            number1 = result

        if işlem in [6, 7]:  
            number2 = None
        elif işlem in [1, 2, 3, 4, 5]:  
            number2 = int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz: "))
        else:
            number2 = None

        
        if işlem == 1:
            result = toplama(number1, number2)
        elif işlem == 2:
            result = çıkarma(number1, number2)
        elif işlem == 3:
            result = çarpma(number1, number2)
        elif işlem == 4:
            result = bölme(number1, number2)
        elif işlem == 5:
            result = üs_Al(number1, number2)
        elif işlem == 6:
            result = kök_hesapla(number1)
        elif işlem == 7:
            result = faktöriyel_hesap(number1)

        
        işlem_sayısı += 1
        print(f"{işlem_sayısı}. işlem sonucunda sonuç = {result}")

        
        other_cal = input("İşleme devam etmek ister misiniz? (y/Y/n/N): ")
        if other_cal in ["y", "Y"]:
            reset = input("Sonuçları sıfırlamak ister misiniz? (y/Y/n/N): ")
            if reset in ["y", "Y"]:  
                result = None  
                print("Sonuç sıfırlandı. Yeni bir işlem yapabilirsiniz.")
                continue  
            else:
                continue
            continue  
        else:
            Flag1 = False  


        
main()















