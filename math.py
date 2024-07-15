import math

def izracunaj_hipotenuzu(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def izracunaj_kuteve(a, b):
    c = izracunaj_hipotenuzu(a, b)
    
    sin_A = a / c
    sin_B = b / c
    sin_C = a / b
    
    cos_A = b / c
    cos_B = a / c
    cos_C = b / a
    
    tan_A = a / b
    tan_B = b / a
    tan_C = a / b
    
    cot_A = b / a
    cot_B = a / b
    cot_C = b / c
    
    return sin_A, sin_B, sin_C, cos_A, cos_B, cos_C, tan_A, tan_B, tan_C, cot_A, cot_B, cot_C

# Unesite duljine stranica trokuta
stranica_a = float(input("Unesite duljinu stranice a: "))
stranica_b = float(input("Unesite duljinu stranice b: "))

# Izračunaj hipotenuzu i kuteve
hipotenuza = izracunaj_hipotenuzu(stranica_a, stranica_b)
kutevi = izracunaj_kuteve(stranica_a, stranica_b)

# Ispiši rezultate
print("Hipotenuza: ", hipotenuza)
print("Sinusi kuteva: ", kutevi[:3])
print("Kosinusi kuteva: ", kutevi[3:6])
print("Tangensi kuteva: ", kutevi[6:9])
print("Kotangensi kuteva: ", kutevi[9:])
