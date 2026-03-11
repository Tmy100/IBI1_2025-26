#Infection.py
#calculate the num of days for the entire IBI1 class to become infected based on two starting variables.

#the number of infected students(a)
#the growth rate over 24hrs(b)
#the total number of students in the class(c)
#day passed(d)

a=5
b=0.40
c=91
d=1
print("Day",d,":",a,"students infected")

while a<c:
	d += 1
	a=a+a*b
	a=a-a%1
	print("Day %d : %.0f students infected"%(d,a))
#must remember to "tab"


print("It took", d, "days for all", c, "students to become infected.")

#Output:
#Day 1 : 5 students infected
#Day 2 : 7.0 students infected
#Day 3 : 9.8 students infected
#Day 4 : 13.72 students infected
#Day 5 : 19.208000000000002 students infected
#Day 6 : 26.891200000000005 students infected
#Day 7 : 37.64768000000001 students infected
#Day 8 : 52.70675200000001 students infected
#Day 9 : 73.78945280000002 students infected
#Day 10 : 103.30523392000003 students infected
#It took 10 days for all 91 students to become infected.