def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
''')

def user_input():
    user_input=input(">")  
    return user_input 


menu = {
'wings':0,
'cookies':0,
'spring rolls':0,
'salmon':0,
'steak':0,
'meat tornado':0,
'a literal garden':0,   
'ice cream':0,
'cake':0,
'pie':0,  
'coffee':0,
'tea unicorn':0,
'tears':0   
}




def quit():
    print('thank for use our app')
    
def user_inputs():
   user_input=input('>') 
   return user_input.lower()

intro() 

user_input=user_inputs()
while(user_input.lower() !="quit"):


   if user_input in menu:
        menu[user_input]+= 1
        print(f' {menu[user_input]}  order of  {user_input}')
       
   else:
        print('we don\'t have this item')
   user_input =user_inputs() 
      
quit()
        