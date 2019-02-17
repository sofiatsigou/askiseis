def sumintervals(a):
 
 list=[]
 for interval in a:
    
    k=len(interval)
    for j in range(interval[0],interval[k-1]):
        
        list.append(int(j))

 print (len(set(list)));


a=[[1,4],[7,10],[3,5]]
sumintervals(a);
