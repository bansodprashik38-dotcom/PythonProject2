birth_year = int(input("Apna birth year enter karo: "))
current_year = 2026

age = current_year - birth_year

print("Aap", age, "saal ke ho.")

if age >= 18:
    print("Aap vote de sakte ho.")
else:
    print("Aap abhi vote nahi de sakte.")