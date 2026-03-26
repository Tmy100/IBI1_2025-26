#Variables.py
#estimated population of Scotland in 2004(a),2014(b),2024(c)

a=5.08*10**6
b=5.33*10**6
c=5.55*10**6

#the change in population between 2004 and 2014(d)
d=b-a
print("the change in population between 2004 and 2014 is %.0f" %d) #float: 0f,zero declimal point; 1f, one declimal point

#the change in population between 2014 and 2024(e)
e=c-b
print("the change in population between 2014 and 2024 is %.0f"%e)

#compare d and e
if d < e :
    print ("The change in population between 2014 and 2024 is larger. It is accelerating.")
else :
    print ("The change in population between 2004 and 2014 is larger. It is decelerating.")

#Larger:d
#Population Growth: Decelarating

#Booleans:
X=True
Y=False
w= X or Y, X or X, Y or X, Y or Y
print("Truth table:", w)

#Output: 
# True or False = True
# True or True = True
# False or True = True
# False or False = False


