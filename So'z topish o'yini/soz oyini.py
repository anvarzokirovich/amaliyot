from uzwords import words
import random as r
from yoshirinsoz import yoshirin
word=r.choice(words).upper()
print(f"Men {len(word)}xonali so'z o'yladim topa olasizmi")
print(yoshirin(word))
qiymatlar=''
javob=''
soz1=word
def soz_top(soz):
    harflar=[]
    for i in soz:
        i=i.upper()
        harflar.append(i)
    
    javoblar=''
    taxmin=0
    while harflar:
        javob=input("Harf kiriting(krill alifbosida):").upper()
        taxmin+=1
        
        if javob in harflar:
            harflar.remove(javob)
            javoblar+=javob
            print(f"{javob} harfi to'gri")
            print(f"{yoshirin(soz, javoblar)}")
        elif javob in javoblar:
            print("Bu harf kiritildi boshqa kiriting:")
        else:
            javoblar+=javob
            print("Xato, bu harf mavjud emas")
            print(f"{yoshirin(soz, javoblar)}")
        if '*' not in yoshirin(soz, javoblar):
            break
        print(f"Hozirgacha kiritgan harflaringgiz:{javoblar}")
        
    return taxmin
        
        
            
son=soz_top(soz1)
print(f"Tabriklayman {son}ta taxmin bilan topdinggiz")
print(f"Yoshiringan sozimiz {word} edi")
       
        
    
    
    
    
    
    
    
    
    
    
    
    