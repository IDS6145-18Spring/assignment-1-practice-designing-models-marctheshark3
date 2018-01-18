#USER INTERACTIONS

def main():

    weekly_list = [] #creating empty list
   
    meal = input("\n What would you like to have for dinner? \n" " A)  Chicken with Mashed Potatoes, B) Chicken with veggies, C) Steak and Mashed Potatoes? \n")

    x = (meal)
    
    #if statements to tell the user what they have chosen,
    # and stores it in the empty list
    if 'a' in x:
            a = 'Chicken & Mashed Potatoes' 
            print("You have chosen" ,a ,"as your Meal")
            weekly_list.append(a)
    elif 'b'in x:
            b = 'Steak & Mashed Potatoes'
            print("You have chosen" ,b ,"as your Meal")
            weekly_list.append(b)
    elif 'c' in x:
            c = 'Chicken & Veggies'
            print("you have chosen" ,c ,"as you Meal")
            weekly_list.append(c)

    print("Youre list for today is", weekly_list)
    return



main()
