
import random 
dobas= ["F", "I"]
dobasok= []
for i in range(5):
    dob=random.choice(dobas)
dobasok.append(dob)
print(".".join(dobasok))
feldobas= random.choice(dobasok)
tipp= input(f"Kérek egy tippet(F/I): ")
with open("coinflip.txt", "w") as file:
    file.write(f"A tipp {tipp} dobás eredménye {feldobas}")
    if tipp== feldobas:
        file.write("Eltaláltad!")
        print("Eltaláltad!")
    else:
        file.write("Meghaltál")
        print("Meghaltál")
        
