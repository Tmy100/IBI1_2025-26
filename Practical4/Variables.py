#Variables.py
#estimated population of Scotland in 2004(a),2014(b),2024(c)
#the change in population between 2004 and 2014(d)
#the change in population between 2014 and 2024(e)

a=5.08*10**6
b=5.33*10**6
c=5.55*10**6

d=b-a
print("%.0f" %d) #float: 0f,zero declimal point; 1f, one declimal point

e=c-b
print("%.0f"%e)

if d < e :
    print ("The change in population between 2014 and 2024 is larger. It is accelerating.")
else :
    print ("The change in population between 2004 and 2014 is larger. It is decelerating.")


#compare d and e
#Larger:d
#Population Growth: Decelarating

#Booleans:
X=True
Y=False
w=X or Y
print(w)



