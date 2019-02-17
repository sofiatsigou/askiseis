def maxSequence(a):

  max=0
  for i in range(0,len(a)):
    sum=a[i]
    for j in range(i+1,len(a)):
        sum=sum+a[j]
        if sum>max :
            max=sum
            b=i
            f=j
  print(max,":")
  for k in range(b,f+1):
    print (a[k],",")
   

a=[-2,1,-3,4,-1,2,1,-5,4]  
maxSequence(a);
