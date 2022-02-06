def yoshirin(b_soz, k_soz=None):
    qiymat=''
    sozlar=[]
    if k_soz!=None:
        for i in k_soz:
            sozlar.append(i)
        for i in b_soz:
            if i in sozlar:
                qiymat+=i
                sozlar.remove(i)
            else:
                qiymat+='*'
    else:
        for i in range(len(b_soz)):
            qiymat+='*'
            
        
    return qiymat

    