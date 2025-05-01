'''@classmethod jardeminde kalkulyator'''

# Ozgeriwhiler
amel = int(input("Amel kirgiz:\n1.Qosiw\n2.Aliw\n3.Kobeytiw\n4.Boliw\n> "))
san_1 = int(input("1-san kirgiz: "))
san_2 = int(input("2-san kirgiz: "))

# Class Jaratiw
class calculator:
    
    # Qosiw
    @classmethod
    def qosiw(cls, a, b):
        return a + b
    
    # Aliw
    @classmethod
    def aliw(cls, a, b):
        return a - b
    
    # Kobeytiw
    @classmethod
    def kobeytiw(cls, a, b):
        return a * b
    
    # Bo'liw
    @classmethod
    def boliw(cls, a, b):
        return a / b

# Ozgeriwshiler 
if amel == 1:
    qosiw = calculator.qosiw(san_1, san_2)
    print(f"{san_1} + {san_2} = {qosiw}")
    
elif amel == 2:
    aliw = calculator.aliw(san_1, san_2)
    print(f"{san_1} - {san_2} = {aliw}")

elif amel == 3:
    kobeytiw = calculator.kobeytiw(san_1, san_2)
    print(f"{san_1} * {san_2} = {kobeytiw}")

elif amel == 4:
    boliw = calculator.boliw(san_1, san_2)
    print(f"{san_1} / {san_2} = {boliw}")

else:
    print(f"Ameldin sanin duris kirgizin")