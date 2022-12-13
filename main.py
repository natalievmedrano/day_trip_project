import random
greeting_message= "WELCOME TO 'MY U.S.A DAY TRIP GENERATOR' WE LOOK FORWARD TO HELP YOU PLAN THE U.S.A VACATION OF YOUR DREAMS"
print(greeting_message)
second_greeting="Here is the trip we have chosen for you!"
print(second_greeting)

#variables
def trip_generator():
    usa_destinations=['New York City,NY','Atlanta,GA',"Washington,D.C","Austin,TX","Las Vegas NV","Los Angeles,CA"]
    usa_resturants=['Tacos Locos','Crab Shack','Blue Dynasty','BurgerFi','Wings n More','Texas Road House']
    usa_transportations=['Train','Car','Plane','Bus','Boat','Swimming']
    usa_entertainments=['Casino','Museum','Movies','Shopping','Theme park','Kayaking']

#selected things/choices for user


    destinations= random.choice(usa_destinations)
    resturants= random.choice(usa_resturants)
    transportations= random.choice(usa_transportations)
    entertainment= random.choice(usa_entertainments)

    return f'''
For your Destination:{destinations}
For your meals:{resturants}
For your transportation:{transportations} 
For your entertainment:{entertainment}
'''


print()

def confirmed_trip():
    user_response= "NO"
    while user_response != "YES":
        usa_trip= trip_generator()
        print(usa_trip)
        response= input("Are you satisfied with these selections? Type YES or NO to confirm.")
    return usa_trip
   
def user_confirmed_trip(confirmed_trip):
    print()
    print('ENJOY YOUR TRIP!!!')
    print(user_confirmed_trip)
    

def run():
    confirm_trip = confirmed_trip()
    user_confirmed_trip(confirmed_trip)

run()

print('ENJOY YOUR TRIP!!!!')
