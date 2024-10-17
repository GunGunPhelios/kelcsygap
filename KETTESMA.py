names=[]
with open ("nevek.txt", "r") as file:
    lines= file.readlines()
    for line in lines:
        line=line.strip()
        name= line.split(";")
        names.append(name)

names.sort
print(names)



numbers=[]
with open ("numbers.txt", "r") as file:
        lines= file.readlines()
        for i in lines:
         i= i.strip()
         

numbers=[int(num) for num in numbers]




nevekesatlag=[]
with open("osztalyatlag.txt","r") as file:
    lines= file.readlines()
    for i in lines:
        i=i.strip()
        nev,atl= i.split(";")
        nevekesatlag.append(nev,float(atl))

print(nevekesatlag)

negyesfelettiek=[]
eredmenyek=0
for nev,atl in nevekesatlag:
        eredmenyek+=atl
        if atl> 4:
             negyesfelettiek.append(nev)
print(negyesfelettiek)
with open("atlag.txt", "r") as file:
     file.write(f"Az átlag: {eredmenyek/len(names)}")
     file.write(";".join(map,str(negyesfelettiek)))
print(f"A negyes atlag felettiek{negyesfelettiek}")


