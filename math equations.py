import math
import sympy as sp

def linear_solver(a, b):
    """Linear Equation Solver: ax + b = 0"""
    if a != 0:
        return -b / a
    else:
        return "No solution" if b != 0 else "Infinite solutions"

def quadratic_solver(a, b, c):
    """Quadratic Equation Solver: ax^2 + bx + c = 0"""
    d = b**2 - 4*a*c
    if d >= 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return root1, root2
    else:
        return "Complex Roots", None

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

def arithmetic_series_sum(a, d, n):
    """Sum of Arithmetic Series: a, a+d, a+2d, ..., a+(n-1)d"""
    return n * (2*a + (n-1)*d) // 2

def geometric_series_sum(a, r, n):
    """Sum of Geometric Series: a, ar, ar^2, ..., ar^(n-1)"""
    return a * (1 - r**n) // (1 - r)

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

def complex_operations_menu():
    while True:
        print("\nKompleks Sayılar Alt Menüsü:")
        print("1. Kompleks Sayı Toplama")
        print("2. Kompleks Sayı Çıkarma")
        print("3. Kompleks Sayı Çarpma")
        print("4. Kompleks Sayı Bölme")
        print("5. Ana Menüye Dön")

        choice = input("Bir seçenek girin (1-5): ")

        if choice == '1':
            real1 = float(input("Birinci sayının reel kısmı: "))
            imag1 = float(input("Birinci sayının imaginer kısmı: "))
            real2 = float(input("İkinci sayının reel kısmı: "))
            imag2 = float(input("İkinci sayının imaginer kısmı: "))
            result = complex(real1, imag1) + complex(real2, imag2)
            print("Sonuç:", result)
        elif choice == '2':
            real1 = float(input("Birinci sayının reel kısmı: "))
            imag1 = float(input("Birinci sayının imaginer kısmı: "))
            real2 = float(input("İkinci sayının reel kısmı: "))
            imag2 = float(input("İkinci sayının imaginer kısmı: "))
            result = complex(real1, imag1) - complex(real2, imag2)
            print("Sonuç:", result)
        elif choice == '3':
            real1 = float(input("Birinci sayının reel kısmı: "))
            imag1 = float(input("Birinci sayının imaginer kısmı: "))
            real2 = float(input("İkinci sayının reel kısmı: "))
            imag2 = float(input("İkinci sayının imaginer kısmı: "))
            result = complex(real1, imag1) * complex(real2, imag2)
            print("Sonuç:", result)
        elif choice == '4':
            real1 = float(input("Birinci sayının reel kısmı: "))
            imag1 = float(input("Birinci sayının imaginer kısmı: "))
            real2 = float(input("İkinci sayının reel kısmı: "))
            imag2 = float(input("İkinci sayının imaginer kısmı: "))
            result = complex(real1, imag1) / complex(real2, imag2)
            print("Sonuç:", result)
        elif choice == '5':
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

def menu():
    while True:
        print("\nMatematik Denklemleri:")
        print("1. Birinci Dereceden Denklem Çözücü")
        print("2. İkinci Dereceden Denklem Çözücü")
        print("3. Üçüncü Dereceden Denklem Çözücü")
        print("4. Faktoriyel Hesapla")
        print("5. Faulhaber Formülü ile Seri Toplamı")
        print("6. Aritmetik Seri Toplamı")
        print("7. Geometrik Seri Toplamı")
        print("8. Fibonacci Sayısı Hesapla")
        print("9. Asal Sayı Kontrolü")
        print("10. En Büyük Ortak Bölen (GCD)")
        print("11. En Küçük Ortak Kat (LCM)")
        print("12. Kompleks Sayılar İşlemleri")
        print("13. Çıkış")

        choice = input("Bir seçenek girin (1-13): ")

        if choice == '1':
            a = float(input("a: "))
            b = float(input("b: "))
            root = linear_solver(a, b)
            print("Çözüm:", root)
        elif choice == '2':
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            roots = quadratic_solver(a, b, c)
            print("Kökler:", roots)
        elif choice == '3':
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            d = float(input("d: "))
            roots = cubic_solver(a, b, c, d)
            print("Kökler:", roots)
        elif choice == '4':
            n = int(input("n: "))
            print("Faktoriyel:", factorial(n))
        elif choice == '5':
            n = int(input("n: "))
            p = int(input("p: "))
            print("Seri Toplamı:", faulhaber_sum(n, p))
        elif choice == '6':
            a = int(input("İlk terim (a): "))
            d = int(input("Oran (d): "))
            n = int(input("Terim sayısı (n): "))
            print("Aritmetik Seri Toplamı:", arithmetic_series_sum(a, d, n))
        elif choice == '7':
            a = int(input("İlk terim (a): "))
            r = float(input("Oran (r): "))
            n = int(input("Terim sayısı (n): "))
            print("Geometrik Seri Toplamı:", geometric_series_sum(a, r, n))
        elif choice == '8':
            n = int(input("n: "))
            print("Fibonacci Sayısı:", fibonacci(n))
        elif choice == '9':
            n = int(input("n: "))
            print("Asal mı:", prime_check(n))
        elif choice == '10':
            a = int(input("a: "))
            b = int(input("b: "))
            print("GCD:", gcd(a, b))
        elif choice == '11':
            a = int(input("a: "))
            b = int(input("b: "))
            print("LCM:", lcm(a, b))
        elif choice == '12':
            complex_operations_menu()
        elif choice == '13':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()