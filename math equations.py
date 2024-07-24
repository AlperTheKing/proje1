import math
import sympy as sp

def linear_solver(a, b):
    """Doğrusal Denklem Çözücü: ax + b = 0"""
    if a != 0:
        return -b / a
    else:
        return "Çözüm yok" if b != 0 else "Sonsuz Çözüm"

def quadratic_solver(a, b, c):
    """İkinci Dereceden Denklem Çözücü: ax^2 + bx + c = 0"""
    d = b**2 - 4*a*c
    if d >= 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return root1, root2
    else:
        return "Karmaşık kökler", None

def cubic_solver(a, b, c, d):
    """Üçüncü Dereceden Denklem Çözücü: ax^3 + bx^2 + cx + d = 0"""
    x = sp.Symbol('x')
    denklem = a*x**3 + b*x**2 + c*x + d
    kökler = sp.solve(denklem, x)
    return kökler

def factorial(n):
    """Bir Sayının Faktöriyeli"""
    return math.factorial(n)

def faulhaber_sum(n, p):
    """Faulhaber Formülü ile Seri Toplamı"""
    B = [sp.bernoulli(i) for i in range(p+1)]
    sonuç = sum(sp.binomial(p + 1, k) * B[k] * n**(p + 1 - k) / (p + 1) for k in range(p + 1))
    return sonuç

def permutation(n, r):
    """Permütasyon Hesaplama: P(n, r)"""
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    """Kombinasyon Hesaplama: C(n, r)"""
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def fibonacci(n):
    """n. Fibonacci Sayısı"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def prime_check(n):
    """Bir Sayının Asal Olup Olmadığını Kontrol Etme"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """En Büyük Ortak Bölen (EBOB)"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """En Küçük Ortak Kat (EKOK)"""
    return a * b // gcd(a, b)

def log_base_b(x, b):
    """Logaritma Hesaplama: log_b(x)"""
    return math.log(x, b)

def exp_function(x):
    """Üstel Fonksiyon: e^x"""
    return math.exp(x)

def trig_functions(angle, func):
    """Trigonometrik Fonksiyonlar: sin, cos, tan"""
    if func == 'sin':
        return math.sin(math.radians(angle))
    elif func == 'cos':
        return math.cos(math.radians(angle))
    elif func == 'tan':
        return math.tan(math.radians(angle))
    else:
        return "Geçersiz fonksiyon"

def complex_operations_menu():
    while True:
        print("╔══════════════════════════════════════════════════╗")
        print("║            Kompleks Sayılar Alt Menüsü           ║")
        print("╠══════════════════════════════════════════════════╣")
        print("║ 1. Kompleks Sayı Toplama                         ║")
        print("║ 2. Kompleks Sayı Çıkarma                         ║")
        print("║ 3. Kompleks Sayı Çarpma                          ║")
        print("║ 4. Kompleks Sayı Bölme                           ║")
        print("║ 5. Ana Menüye Dön                                ║")
        print("╚══════════════════════════════════════════════════╝")

        seçenek = input("Bir seçenek girin (1-5): ")

        if seçenek == '1':
            real1 = float(input("Birinci sayının reel kısmını girin: "))
            imag1 = float(input("Birinci sayının hayali kısmını girin: "))
            real2 = float(input("İkinci sayının reel kısmını girin: "))
            imag2 = float(input("İkinci sayının hayali kısmını girin: "))
            sonuç = complex(real1, imag1) + complex(real2, imag2)
            print("Sonuç:", sonuç)
        elif seçenek == '2':
            real1 = float(input("Birinci sayının reel kısmını girin: "))
            imag1 = float(input("Birinci sayının hayali kısmını girin: "))
            real2 = float(input("İkinci sayının reel kısmını girin: "))
            imag2 = float(input("İkinci sayının hayali kısmını girin: "))
            sonuç = complex(real1, imag1) - complex(real2, imag2)
            print("Sonuç:", sonuç)
        elif seçenek == '3':
            real1 = float(input("Birinci sayının reel kısmını girin: "))
            imag1 = float(input("Birinci sayının hayali kısmını girin: "))
            real2 = float(input("İkinci sayının reel kısmını girin: "))
            imag2 = float(input("İkinci sayının hayali kısmını girin: "))
            sonuç = complex(real1, imag1) * complex(real2, imag2)
            print("Sonuç:", sonuç)
        elif seçenek == '4':
            real1 = float(input("Birinci sayının reel kısmını girin: "))
            imag1 = float(input("Birinci sayının hayali kısmını girin: "))
            real2 = float(input("İkinci sayının reel kısmını girin: "))
            imag2 = float(input("İkinci sayının hayali kısmını girin: "))
            sonuç = complex(real1, imag1) / complex(real2, imag2)
            print("Sonuç:", sonuç)
        elif seçenek == '5':
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

def menu():
    while True:
        print("╔══════════════════════════════════════════════════╗")
        print("║                 Matematik Denklemleri            ║")
        print("╠══════════════════════════════════════════════════╣")
        print("║ 1. Birinci Dereceden Denklem Çözücü              ║")
        print("║ 2. İkinci Dereceden Denklem Çözücü               ║")
        print("║ 3. Üçüncü Dereceden Denklem Çözücü               ║")
        print("║ 4. Faktoriyel Hesapla                            ║")
        print("║ 5. Faulhaber Formülü ile Seri Toplamı            ║")
        print("║ 6. Permütasyon Hesaplama                         ║")
        print("║ 7. Kombinasyon Hesaplama                         ║")
        print("║ 8. Fibonacci Sayısı Hesapla                      ║")
        print("║ 9. Asal Sayı Kontrolü                            ║")
        print("║ 10. En Büyük Ortak Bölen (GCD)                   ║")
        print("║ 11. En Küçük Ortak Kat (LCM)                     ║")
        print("║ 12. Logaritma Hesaplama                          ║")
        print("║ 13. Üstel Fonksiyon Hesaplama                    ║")
        print("║ 14. Trigonometrik Fonksiyon Hesaplama            ║")
        print("║ 15. Kompleks Sayılar İşlemleri                   ║")
        print("║ 16. Çıkış                                        ║")
        print("╚══════════════════════════════════════════════════╝")

        seçenek = input("Bir seçenek girin (1-16): ")

        if seçenek == '1':
            a = float(input("Denklemdeki a katsayısını girin (ax + b = 0): "))
            b = float(input("Denklemdeki b katsayısını girin (ax + b = 0): "))
            kök = linear_solver(a, b)
            print("Çözüm:", kök)
        elif seçenek == '2':
            a = float(input("Denklemdeki a katsayısını girin (ax^2 + bx + c = 0): "))
            b = float(input("Denklemdeki b katsayısını girin (ax^2 + bx + c = 0): "))
            c = float(input("Denklemdeki c katsayısını girin (ax^2 + bx + c = 0): "))
            kökler = quadratic_solver(a, b, c)
            print("Kökler:", kökler)
        elif seçenek == '3':
            a = float(input("Denklemdeki a katsayısını girin (ax^3 + bx^2 + cx + d = 0): "))
            b = float(input("Denklemdeki b katsayısını girin (ax^3 + bx^2 + cx + d = 0): "))
            c = float(input("Denklemdeki c katsayısını girin (ax^3 + bx^2 + cx + d = 0): "))
            d = float(input("Denklemdeki d katsayısını girin (ax^3 + bx^2 + cx + d = 0): "))
            kökler = cubic_solver(a, b, c, d)
            print("Kökler:", kökler)
        elif seçenek == '4':
            n = int(input("Faktoriyelini hesaplamak istediğiniz sayıyı girin: "))
            print("Faktoriyel:", factorial(n))
        elif seçenek == '5':
            n = int(input("Seri toplamının son terimini girin: "))
            p = int(input("Seri toplamındaki kuvveti girin: "))
            print("Seri Toplamı:", faulhaber_sum(n, p))
        elif seçenek == '6':
            n = int(input("Permütasyon hesaplaması için n değerini girin: "))
            r = int(input("Permütasyon hesaplaması için r değerini girin: "))
            print("Permütasyon:", permutation(n, r))
        elif seçenek == '7':
            n = int(input("Kombinasyon hesaplaması için n değerini girin: "))
            r = int(input("Kombinasyon hesaplaması için r değerini girin: "))
            print("Kombinasyon:", combination(n, r))
        elif seçenek == '8':
            n = int(input("Hesaplamak istediğiniz Fibonacci sayısının indeksini girin: "))
            print("Fibonacci Sayısı:", fibonacci(n))
        elif seçenek == '9':
            n = int(input("Asal olup olmadığını kontrol etmek istediğiniz sayıyı girin: "))
            print("Asal mı:", prime_check(n))
        elif seçenek == '10':
            a = int(input("GCD hesaplamak için birinci sayıyı girin: "))
            b = int(input("GCD hesaplamak için ikinci sayıyı girin: "))
            print("GCD:", gcd(a, b))
        elif seçenek == '11':
            a = int(input("LCM hesaplamak için birinci sayıyı girin: "))
            b = int(input("LCM hesaplamak için ikinci sayıyı girin: "))
            print("LCM:", lcm(a, b))
        elif seçenek == '12':
            x = float(input("Logaritmasını hesaplamak istediğiniz sayıyı girin: "))
            b = float(input("Logaritma tabanını girin: "))
            print("Logaritma:", log_base_b(x, b))
        elif seçenek == '13':
            x = float(input("Üstel fonksiyon için x değerini girin (e^x): "))
            print("Üstel Fonksiyon Sonucu:", exp_function(x))
        elif seçenek == '14':
            angle = float(input("Açıyı derece cinsinden girin: "))
            func = input("Hangi trigonometrik fonksiyonu hesaplamak istiyorsunuz (sin, cos, tan): ")
            print(f"{func}({angle}) = {trig_functions(angle, func)}")
        elif seçenek == '15':
            complex_operations_menu()
        elif seçenek == '16':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()