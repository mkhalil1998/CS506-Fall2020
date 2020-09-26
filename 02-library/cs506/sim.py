def euclidean_dist(x, y):
    #Checking
    if len(x)==0 or len(y)==0:
        return ValueError("lengths must not be zero")
    if len(x)!=len(y):
        return ValueError("lengths must be equal")
    #Calculating manhattan
    length= len(x)
    s_sum=0
    for i in range(length):
        s_sum += pow(abs(x[i]-y[i]),2)
    return pow(s_sum,2)


def manhattan_dist(x, y):
    #Checking
    if len(x)==0 or len(y)==0:
        return ValueError("lengths must not be zero")
    if len(x)!=len(y):
        return ValueError("lengths must be equal")
    #Calculating manhattan
    length= len(x)
    s_sum=0
    for i in range(length):
        s_sum += pow(abs(x[i]-y[i]),1)
    return pow(s_sum,1)
 
def jaccard_dist(x, y):
    if x==[] or y==[]:
        return "lengths must not be zero"
    else:
        intersection = len(list(set(x).intersection(y)))
        union = len(list(set(x).union(y)))
        j= 1 - float(intersection / union) # 1- Dividing intersection by union
        return(j)

def cosine_sim(x, y):
   import math 
   if len(x)==0 or len(y)==0:
        return ValueError("lengths must not be zero")
   if len(x)!=len(y):
        return ValueError("lengths must be equal")
   sumab=0 
   for i in range(len(x)):
        a=x[i]
        b=y[i]
        sumab += a*b
   return sumab/euclidean_dist(x,y)






    



