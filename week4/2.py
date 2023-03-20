liste = [2,5,98,4,4]

def fonk(liste):

    liste1=[]
    for i in liste:
        liste1+=[i/sum(liste)]
    return liste1

print(fonk(liste))