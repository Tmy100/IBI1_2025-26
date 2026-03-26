#Infection.py
#Aim: calculate the number of days for the entire IBI1 class to become infected based on two starting variables.

#Step1: list variables + print the initial values
#		the number of infected students(a)
#		the growth rate over 24hrs(b)
#		the total number of students in the class(c)
#		day passed(d)

a=5
b=0.40
c=91
d=1
print("Day",d,":",a,"students infected")

#Step2: calculate infected students using loop + print day and the number of infected students
#Logic: start from 5 students, end when it reached 91 students.
# 		IF accumulated infected students < the number of whole class, THEN accumulate the day +1
#		total infected students = (initial infect. num)+(initial infect. num)*(growth rate)

while a<c:
	d += 1
	a=a+a*b
	a=a-a%1 #this step is to round up the declimal points
	print("Day %d : %.0f students infected"%(d,a))


#Step3: make a conclude sentence.
print("It took", d, "days for all", c, "students to become infected.")
