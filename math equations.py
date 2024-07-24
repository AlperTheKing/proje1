import math
import sympy as sp

def linear_solver(a, b):
    """Linear Equation Solver: ax + b = 0"""
    if a != 0:
        return -b / a
    else:
        return "Çözüm yok" if b != 0 else "Sonsuz çözüm"

def quadratic_solver(a, b, c):
    """Quadratic Equation Solver: ax^2 + bx + c = 0"""
    d = b**2 - 4*a*c
    if d >= 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return root1, root2
    else:
        return "Karmaşık kökler", None

def cubic_solver(a, b, c, d):
    """Cubic Equation Solver: ax^3 + bx^2 + cx + d = 0"""
    x = sp.Symbol('x')
    equation = a*x**3 + b*x**2 + c*x + d
    roots = sp.solve(equation, x)
    return roots

def factorial(n):
    """Factorial of a Number"""
    return math.factorial(n)

def faulhaber_sum(n, p):
    """Faulhaber Formula for Sum of Powers using Faulhaber Algorithm"""
    B = [sp.bernoulli(i) for i in range(p+1)]
    result = sum(sp.binomial(p + 1, k) * B[k] * n**(p + 1 - k) / (p + 1) for k in range(p + 1))
    return result

def permutation(n, r):
    """Permutation Calculation: P(n, r)"""
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    """Combination Calculation: C(n, r)"""
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def fibonacci(n):
    """nth Fibonacci Number"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def prime_check(n):
    """Check if a Number is Prime"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Greatest Common Divisor (GCD)"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least Common Multiple (LCM)"""
    return a * b // gcd(a, b)

def log_base_b(x, b):
    """Logarithm Calculation: log_b(x)"""
    return math.log(x, b)

def exp_function(x):
    """Exponential Function: e^x"""
    return math.exp(x)

def trig_functions(angle, func):
    """Trigonometric Functions: sin, cos, tan"""
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

        choice = input("Bir seçenek girin (1-5): ")

        if choice == '1':
            real1 = float(input("Birinci sayının reel kısmını girin: "))
            imag1 = float(input("Birinci sayının imaginer kısmını girin: "))
            real2 = float(input("İkinci sayının reel kısmını girin: "))
            imag2 = float(input("İkinci sayının imaginer kısmını girin: "))
            result = complex(real1, imag1) + complex(real2, imag2)
            print("Sonuç:", result)
        elif choice == '2':
            real1 = float(input("Birinci sayının reel kısmını girin: "))
            imag1 = float(input("Birinci sayının imaginer kısmını girin: "))
            real2 = float(input("İkinci sayının reel kısmını girin: "))
            imag2 = float(input("İkinci sayının imaginer kısmını girin: "))
            result = complex(real1, imag1) - complex(real2, imag2)
            print("Sonuç:", result)
        elif choice == '3':
            real1 = float(input("Birinci sayının reel kısmını girin: "))
            imag1 = float(input("Birinci sayının imaginer kısmını girin: "))
            real2 = float(input("İkinci sayının reel kısmını girin: "))
            imag2 = float(input("İkinci sayının imaginer kısmını girin: "))
            result = complex(real1, imag1) * complex(real2, imag2)
            print("Sonuç:", result)
        elif choice == '4':
            real1 = float(input("Birinci sayının reel kısmını girin: "))
            imag1 = float(input("Birinci sayının imaginer kısmını girin: "))
            real2 = float(input("İkinci sayının reel kısmını girin: "))
            imag2 = float(input("İkinci sayının imaginer kısmını girin: "))
            result = complex(real1, imag1) / complex(real2, imag2)
            print("Sonuç:", result)
        elif choice == '5':
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

        choice = input("Bir seçenek girin (1-16): ")

        if choice == '1':
            a = float(input("Denklemdeki a katsayısını girin (ax + b = 0): "))
            b = float(input("Denklemdeki b katsayısını girin (ax + b = 0): "))
            root = linear_solver(a, b)
            print("Çözüm:", root)
        elif choice == '2':
            a = float(input("Denklemdeki a katsayısını girin (ax^2 + bx + c = 0): "))
            b = float(input("Denklemdeki b katsayısını girin (ax^2 + bx + c = 0): "))
            c = float(input("Denklemdeki c katsayısını girin (ax^2 + bx + c = 0): "))
            roots = quadratic_solver(a, b, c)
            print("Kökler:", roots)
        elif choice == '3':
            a = float(input("Denklemdeki a katsayısını girin (ax^3 + bx^2 + cx + d = 0): "))
            b = float(input("Denklemdeki b katsayısını girin (ax^3 + bx^2 + cx + d = 0): "))
            c = float(input("Denklemdeki c katsayısını girin (ax^3 + bx^2 + cx + d = 0): "))
            d = float(input("Denklemdeki d katsayısını girin (ax^3 + bx^2 + cx + d = 0): "))
            roots = cubic_solver(a, b, c, d)
            print("Kökler:", roots)
        elif choice == '4':
            n = int(input("Faktoriyelini hesaplamak istediğiniz sayıyı girin: "))
            print("Faktoriyel:", factorial(n))
        elif choice == '5':
            n = int(input("Seri toplamının son terimini girin: "))
            p = int(input("Seri toplamındaki kuvveti girin: "))
            print("Seri Toplamı:", faulhaber_sum(n, p))
        elif choice == '6':
            n = int(input("Permütasyon hesaplaması için n değerini girin: "))
            r = int(input("Permütasyon hesaplaması için r değerini girin: "))
            print("Permütasyon:", permutation(n, r))
        elif choice == '7':
            n = int(input("Kombinasyon hesaplaması için n değerini girin: "))
            r = int(input("Kombinasyon hesaplaması için r değerini girin: "))
            print("Kombinasyon:", combination(n, r))
        elif choice == '8':
            n = int(input("Hesaplamak istediğiniz Fibonacci sayısının indeksini girin: "))
            print("Fibonacci Sayısı:", fibonacci(n))
        elif choice == '9':
            n = int(input("Asal olup olmadığını kontrol etmek istediğiniz sayıyı girin: "))
            print("Asal mı:", prime_check(n))
        elif choice == '10':
            a = int(input("GCD hesaplamak için birinci sayıyı girin: "))
            b = int(input("GCD hesaplamak için ikinci sayıyı girin: "))
            print("GCD:", gcd(a, b))
        elif choice == '11':
            a = int(input("LCM hesaplamak için birinci sayıyı girin: "))
            b = int(input("LCM hesaplamak için ikinci sayıyı girin: "))
            print("LCM:", lcm(a, b))
        elif choice == '12':
            x = float(input("Logaritmasını hesaplamak istediğiniz sayıyı girin: "))
            b = float(input("Logaritma tabanını girin: "))
            print("Logaritma:", log_base_b(x, b))
        elif choice == '13':
            x = float(input("Üstel fonksiyon için x değerini girin (e^x): "))
            print("Üstel Fonksiyon Sonucu:", exp_function(x))
        elif choice == '14':
            angle = float(input("Açıyı derece cinsinden girin: "))
            func = input("Hangi trigonometrik fonksiyonu hesaplamak istiyorsunuz (sin, cos, tan): ")
            print(f"{func}({angle}) = {trig_functions(angle, func)}")
        elif choice == '15':
            complex_operations_menu()
        elif choice == '16':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()