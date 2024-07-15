import math

def izracunaj_drugu_stranicu(hipotenuza, prilezeca_stranica):
    druga_stranica = math.sqrt(hipotenuza**2 - prilezeca_stranica**2)
    return druga_stranica

def izracunaj_kuteve(hipotenuza, prilezeca_stranica):
    druga_stranica = izracunaj_drugu_stranicu(hipotenuza, prilezeca_stranica)
    
    sin_A = prilezeca_stranica / hipotenuza
    sin_B = druga_stranica / hipotenuza
    sin_C = prilezeca_stranica / druga_stranica
    
    cos_A = druga_stranica / hipotenuza
    cos_B = prilezeca_stranica / hipotenuza
    cos_C = druga_stranica / prilezeca_stranica
    
    tan_A = prilezeca_stranica / druga_stranica
    tan_B = druga_stranica / prilezeca_stranica
    tan_C = prilezeca_stranica / hipotenuza
    
    cot_A = druga_stranica / prilezeca_stranica
    cot_B = prilezeca_stranica / druga_stranica
    cot_C = hipotenuza / prilezeca_stranica
    
    return druga_stranica, sin_A, sin_B, sin_C, cos_A, cos_B, cos_C, tan_A, tan_B, tan_C, cot_A, cot_B, cot_C

# Unesite hipotenuzu i priležeću stranicu
hipotenuza = float(input("Unesite hipotenuzu: "))
prilezeca_stranica = float(input("Unesite duljinu priležeće stranice: "))

# Izračunaj drugu priležeću stranicu i kuteve
druga_stranica, kutevi = izracunaj_drugu_stranicu(hipotenuza, prilezeca_stranica), izracunaj_kuteve(hipotenuza, prilezeca_stranica)

# Ispiši rezultate
print("Druga priležeća stranica: ", druga_stranica)
print("Sinusi kuteva: ", kutevi[1:4])
print("Kosinusi kuteva: ", kutevi[4:7])
print("Tangensi kuteva: ", kutevi[7:10])
print("Kotangensi kuteva: ", kutevi[10:])
