import random
x = random.random()
if x<0.3:
    x = "sang"
elif x>=0.3 and x<=0.6:
    x = "gheychi"
else:
    x = "kaghaz"

y = input("entekhabe shoma")

if x==y:
    print("=== mosavi ===")
    print("x =", x)
    print("entekhabe shoma =", y)
    
elif x=="sang" and y=="gheychi":
    print("x barande ast")
    print("x =", x)
    print("entekhabe shoma =", y)
    
elif x=="gheychi" and y=="kaghaz":
    print("x barande ast")
    print("x =", x)
    print("entekhabe shoma =", y)
    
elif x=="kaghaz" and y=="sang":
    print("x barande ast")
    print("x =", x)
    print("entekhabe shoma =", y)
    
else:
    print("Tabrik! shoma barande shodid")
    print("x =", x)
    print("entekhabe shoma =", y)
    
