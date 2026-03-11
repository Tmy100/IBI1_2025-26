

#initial variables
gender="female" #cannot write as gender=female
age=int(input("What is the age?"))
weight=int(input("what is the weight?"))
gender=input("what is the gender?")
cr=int(input("what is the cr?"))

#validation checks
if age >=100 :
    print ("Age needs corrected. Choose a variable <100")
elif weight >=80 and weight <=20:
    print ("Weight needs corrected. Choose a variable between 20 and 80")
elif gender != "male" and gender != "female":
    print("Gender needs corrected. Choose 'male' or 'female'")
elif cr <=0 and cr >=100:
    print("Choose between 0 and 100")
else:
    print("everything nice")

    #calculations
    if gender == "male":
            Crcl=(140-age)*weight/(72*cr)
            print("Crcl for male is",Crcl)
    elif gender == "female": 
            Crcl=(140-age)*weight/(72*cr)*0.85
            print("Crcl for female is %d" %Crcl) #to make it into an integer

 