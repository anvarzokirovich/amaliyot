import random as r

def odam_top(x=10):
    son=r.randint(1,x)
    print(f"1dan {x}gacha son o'yladim topib ko'ringchi?")
    taxmin=0
    while True:
        taxmin+=1
        javob=int(input("Javobingiz:"))
        if javob!=son:
            if javob<son:
                qisqa="katta"
            else:
                qisqa="kichik"
            print(f"Xato men o'ylagan son bundan {qisqa}, yana urinib ko'ring! ")
        else:
            print(f"Tabriklayman, {taxmin}ta taxmin bilan topdingiz")
            break
    return taxmin
    
def kom_top(x=10):
    print(f"1dan {x}gacha son o'ylang men topaman!")
    input("Son o'ylagan bo'lsangiz 'ENTER' tugmasini bosing!")
    a=1
    b=x
    taxmin=0
    while True:
        taxmin+=1
        qiymat=r.randint(a, b)
        javob=input(f"Siz o'ylagan son {qiymat}ga teng:\n"
                    f"Tog'ri(t), yo'q men o'ylagan son bundan katta(+) yoki kichik(-)??")
        if javob.upper()=='T':
            print(f"Qoyil, {taxmin}ta taxmin bilan topdim!")
            break
        else:
            if javob=='+':
                a=qiymat+1
            else:
                b=qiymat-1
    return taxmin

def boshla(x=10):
    savol=1
    while savol:
        odam=odam_top(x)
        kompyuter=kom_top(x)
        if odam>kompyuter:
            print(f"{kompyuter}ta tamin bilan men yutdim")
        elif odam==kompyuter:
            print(f"Durrang, ikkalamiz ham {odam}ta taxmin bilan topdik")
        else:
            print(f"Tabriklayman, {odam}ta taxmin bilan siz yutdingiz")
        savol=int(input("Yana o'ynaymizmi:ha(1), yo'q(0)??"))
            
            
        
        
    
    
        
    










                
        