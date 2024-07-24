import math

def main_menu():
    print("MATEMATİK DENKLEMLERİ")
    print("1 - Doğrusal Denklem (ax + b = 0)")
    print("2 - İkinci Dereceden Denklem (ax^2 + bx + c = 0)")
    print("3 - Üs Alma (a^b)")
    print("4 - Logaritma (log_a(b))")
    print("5 - Sinüs, Kosinüs, Tanjant (sin, cos, tan)")
    print("6 - Permütasyon (P(n, r))")
    print("7 - Kombinasyon (C(n, r))")
    print("8 - Faktöriyel (n!)")
    print("9 - Mutlak Değer (|x|)")
    print("10 - Kareköklü Sayı (√x)")
    print("11 - Faulhaber's Formülü ile Seri Toplamı (∑k^p)")
    print("12 - Çıkış")
    choice = input("Seçiminizi yapınız: ")
    return choice

def linear_equation():
    print("Doğrusal Denklem: ax + b = 0")
    a = float(input("a değerini giriniz: "))
    b = float(input("b değerini giriniz: "))
    if a == 0:
        print("a değeri 0 olamaz.")
    else:
        x = -b / a
        print(f"Denklemin çözümü: x = {x}")

def quadratic_equation():
    print("İkinci Dereceden Denklem: ax^2 + bx + c = 0")
    a = float(input("a değerini giriniz: "))
    b = float(input("b değerini giriniz: "))
    c = float(input("c değerini giriniz: "))
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Denklemin reel kökü yoktur.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Denklemin tek kökü vardır: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Denklemin iki kökü vardır: x1 = {x1}, x2 = {x2}")

def power():
    print("Üs Alma: a^b")
    a = float(input("a değerini giriniz: "))
    b = float(input("b değerini giriniz: "))
    result = a ** b
    print(f"Sonuç: {a}^{b} = {result}")

def logarithm():
    print("Logaritma: log_a(b)")
    a = float(input("a (taban) değerini giriniz: "))
    b = float(input("b (logaritma alınacak sayı) değerini giriniz: "))
    if a <= 0 or a == 1 or b <= 0:
        print("Geçersiz değerler. a > 0, a ≠ 1 ve b > 0 olmalıdır.")
    else:
        result = math.log(b, a)
        print(f"Sonuç: log_{a}({b}) = {result}")

def trig_functions():
    print("Trigonometrik Fonksiyonlar: sin, cos, tan")
    angle = float(input("Açıyı derece cinsinden giriniz: "))
    radian = math.radians(angle)
    sin_value = math.sin(radian)
    cos_value = math.cos(radian)
    tan_value = math.tan(radian)
    print(f"sin({angle}) = {sin_value}")
    print(f"cos({angle}) = {cos_value}")
    print(f"tan({angle}) = {tan_value}")

def permutation():
    print("Permütasyon: P(n, r)")
    n = int(input("n değerini giriniz: "))
    r = int(input("r değerini giriniz: "))
    if n < r:
        print("n, r'den büyük veya eşit olmalıdır.")
    else:
        result = math.factorial(n) // math.factorial(n - r)
        print(f"Sonuç: P({n}, {r}) = {result}")

def combination():
    print("Kombinasyon: C(n, r)")
    n = int(input("n değerini giriniz: "))
    r = int(input("r değerini giriniz: "))
    if n < r:
        print("n, r'den büyük veya eşit olmalıdır.")
    else:
        result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        print(f"Sonuç: C({n}, {r}) = {result}")

def factorial():
    print("Faktöriyel: n!")
    n = int(input("n değerini giriniz: "))
    if n < 0:
        print("n negatif olamaz.")
    else:
        result = math.factorial(n)
        print(f"Sonuç: {n}! = {result}")

def absolute_value():
    print("Mutlak Değer: |x|")
    x = float(input("x değerini giriniz: "))
    result = abs(x)
    print(f"Sonuç: |{x}| = {result}")

def square_root():
    print("Kareköklü Sayı: √x")
    x = float(input("x değerini giriniz: "))
    if x < 0:
        print("x negatif olamaz.")
    else:
        result = math.sqrt(x)
        print(f"Sonuç: √{x} = {result}")

def faulhaber_sum():
    print("Faulhaber's Formülü ile Seri Toplamı: ∑k^p")
    n = int(input("n (serinin son terimi) değerini giriniz: "))
    p = int(input("p (kuvvet) değerini giriniz: "))
    result = sum(k**p for k in range(1, n+1))
    print(f"Sonuç: ∑k^{p} (k=1 to {n}) = {result}")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            linear_equation()
        elif choice == '2':
            quadratic_equation()
        elif choice == '3':
            power()
        elif choice == '4':
            logarithm()
        elif choice == '5':
            trig_functions()
        elif choice == '6':
            permutation()
        elif choice == '7':
            combination()
        elif choice == '8':
            factorial()
        elif choice == '9':
            absolute_value()
        elif choice == '10':
            square_root()
        elif choice == '11':
            faulhaber_sum()
        elif choice == '12':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")

if __name__ == "__main__":
    main()