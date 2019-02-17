a1=int(input("Δώστε αρχή διαστήματος"))
a2=int(input("Δώστε τέλος διαστήματος"))
a3=int(input("Δώστε διαφορά"))
list=[]
for i in range(a1,a2+1,1):
   if i!=0:
    if i==2:
        list.append(i)
    else:
     k="true"
     l=int(abs(i)**(1/2))
     
     for j in range(2,l+1,1):
       if abs(i)%j==0:
            k="false"
     if k=="true":
        list.append(i)

y="false"
for i in range(0,len(list)):
    if y=="true":
        break
    else:
     for j in range(i,len(list)):
      if abs(list[i]-list[j])==a3:
       print ("(",list[i],",",list[j],")") 
       y="true"
       break
if y=="false":
    print("Δέν υπάρχει τέτοιο διάστημα")
