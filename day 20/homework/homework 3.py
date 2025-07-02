animals = ["მელია", "მგელი", "ქათამი", "ხბო"]

for animal in animals:
    if len(animal) < 5 and animal.istitle():
        print(animal[:3])
    else:
        print("ეს სიტყვა გრძელია")

 

