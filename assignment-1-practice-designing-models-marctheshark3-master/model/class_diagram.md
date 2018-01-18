## Smart City Automated Grocery List Model - Class Diagram



**DESCRIPTION**
To start the User has to give some information as to what meals they want to eat. To do this the Meal Library is called to the user to show what is available. The users answer is stored into meal_list which is then compared to the meal_lib to then be stored as a new list called meals_updated. This list is then called to compare it against the recipe library where the ingredients & instructions are stored. Once compared the ingredients for the chosen meals are then store in verify_rec to be verified by the user to decide if ingredients need to be add or taken away. A new list is made called ingredient_grcy which is now the newly verfied list sent from the user. The instructions are also updated respective of the ingredients. The system then asks the user if the list can be sent to the grocery store using the snd_grcy, and granted verification by go_snd which will then allow the list to be sent to the store. After the store will alert the user when it is ready for pickup.

![Class_Diagram](../images/CLASS_Dia.png)

