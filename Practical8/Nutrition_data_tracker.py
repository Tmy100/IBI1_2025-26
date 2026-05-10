#Nutrition_data_tracker
#Calculate and report the total calories,protein,carbohydrate and fat consumed by an individual over a 24hrs period.

#Create a class called food_item to track the nutritional input  
class food_item ():
    def __init__ (self,name,a,b,c,d):
            self.name = name
            self.a = a #calories
            self.b = b #protein
            self.c = c #carbohydrates
            self.d = d #fat

    def nutrients (self):
            print (f"{self.name} has {self.a} calories, {self.b}g protein, {self.c}g carbohydrate and {self.d}g fat.")

print ("== Class output ==")
food_intake = food_item("Apple",60,0.3,15,0.5)
food_intake.nutrients()


#Create a function to calculate and report the total nutrients
def calculate_with_list (food_list):
    '''
    Calculate and report the total calories, protein, carbohydrate and fat consumed over a 24hr period.
    Report warning if an individual has consumed over more than 2500 calories or 90g fat.
    '''
    totals = [0,0,0,0]

    for food in food_list:
         #Index 0 is calories
         totals [0] += food.a

         #Index 1 is protein
         totals [1] += food.b

         #Index 2 is carbohydrates 
         totals [2] += food.c

         #Index 3 is fat
         totals [3] += food.d

    print("\n == Individual nutrition report ==")
    print (f'Total calories:{totals[0]}')
    print (f'Total protein:{totals[1]}g')
    print (f'Total carbohydrates:{totals[2]}g')
    print (f'Total fat:{totals[3]}g')

    return totals

#List of food that the individual has consumed last 24hr period
chicken_breast = food_item("Chicken_breast",101000,18,0,1)
potatoes = food_item("Potatoes", 95000,2,45,0)
white_rice = food_item("White_rice",205000,4,45,0)
brocolli = food_item("Brocolli",7000,0.6,1.5,0)

#Put them in a list
foods = [chicken_breast,potatoes,white_rice,brocolli]

#Calculate the total cal,pro,carbs,fat
calculated_totals = calculate_with_list(foods)
total_cal = calculated_totals[0]
total_fat = calculated_totals[3]

#Give the individual warning if he/she consumed too much calories and fat
if total_cal >= 2500 and total_fat >= 90:
    print ("Warning! You have consumed more than 2500 calories and 90g fat.")
elif total_cal < 2500 and total_fat >= 90:
    print ("Warning! You have consumed more than 90g fat.")
elif total_cal >= 2500 and total_fat < 90:
    print ("Warning! You have consumed more than 2500 calories.")
else:
    print("You have an appropriate intake of nutrients.")
    


