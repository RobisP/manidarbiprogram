cb=[1,2,3,4,5]#nemaina saraksta elementus.
for a in cb:#pieejams indekss
    a+=10
    print(a)
print(cb)


aa = [1,2,3,4,5]
for i in range(len(aa)):
    aa[i] +=10
    print(aa[i])
print(aa)
#pieejams indekss, pat ssaraksta elements

aa=[1,2,3,4,5]
sum=0
for i,a in enumerate(aa):
    sum+= a
    aa[i]+=10
    print(aa, sum)
    
#Drukāšana
    
a = 23
print(f"{a}")


sar=list("asaka")
print(sar[3])


t1=input("Teksts1: ")
for t in t1:
    print(f"Burts ir {t}")\
                  
                  
sar=input("Teksts: ")
for i in range(len(sar)):
    print("sar[",i,"]=",sar[i])
    
    
sar=input("Teksts: ")
for i in range(len(sar)):
    print(f"sar[{i}]={sar[i]}")
    
    
    
                  
                  
                  

         