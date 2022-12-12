#Store the trip options for destinations, restaurants, transportation, and entertainment each in their own List 
#Get a random element from each of those sets of options. 
#Display the initial random trip to your user
#Prompt the user to see if they are satisfied
#If not, find out which trip feature they want to change and randomly select a new feature.
#Keep doing this process until the user is satisfied with the trip

greeting_message= "WELCOME TO 'MY U.S.A DAY TRIP GENERATOR' WE LOOK FORWARD TO HELP YOU PLAN THE U.S.A VACATION OF YOUR DREAMS"
print(greeting_message)
second_greeting="Here is the trip we have chosen for you!"
print(second_greeting)

#variables
usa_destinations=['New York City,NY','Atlanta,GA',"Washington,D.C","Austin,TX","Las Vegas NV","Los Angeles,CA"]
usa_resturants=['Tacos Locos','Crab Shack','Blue Dynasty','BurgerFi','Wings n More','Texas Road House']
usa_transportations=['Train','Car','Plane','Bus','Boat','Swimming']
usa_entertainments=['Casino','Museum','Movies','Shopping','Theme park','Kayaking']

#selected things/choices for user
import random

destinations= random.choice(usa_destinations)
resturants= random.choice(usa_resturants)
transportations= random.choice(usa_transportations)
entertainments= random.choice(usa_entertainments)

print(f'For your U.S.A Destination:{destinations}',f'For your meals:{resturants}',f'For your transportation:{transportations}',f'For your entertainment:{entertainments}')

#allow user to confirm or deny trip
print(f'Are you satisfied with these selections?')
user_confirmation= input('Type YES or NO to confirm.')

#if user isnt satisfied with the selections...

def new_usa_destination(user_confirmation):
        while user_confirmation != 'YES':
            chosen_destination= random.choice(usa_destinations)
            user_confirmation= input(f"Is {destinations} a more suitable choice for you?")
        else:
            print(f"You chose {destinations} as your Destination!")

    
new_usa_destination(user_confirmation)



def new_usa_resturant (user_confirmation):

        while user_confirmation != 'YES':
            chosen_resturant= random.choice(usa_resturants)
            user_confirmation= input(f"Sorry you were not satisfied with our choice, is {resturants} a more suitable choice?")
        else:
            print(f'Awesome! you have selected {resturants}.')

new_usa_resturant(user_confirmation)



def new_usa_transportation (user_confirmation):
        while user_confirmation != 'YES':
            chosen_transportation= random.choice(usa_transportations)
            user_confirmation= input(f"Sorry you weren't happy with our choices,is {transportations} a more suitable choice?")
        else:
            print(f'You chose {transportations} as your transportation method!')

new_usa_transportation(user_confirmation)



def new_usa_entertainment(user_confirmation):
        while user_confirmation != 'YES':
            chosen_entertainment= random.choice(usa_entertainments)
            user_confirmation= input(f"Sorry you weren't satisfied with our choice")
        else:
            print(f'You have chosen {entertainments} as your entertainment!')

new_usa_entertainment(user_confirmation)

print("We hope you enjoy your trip! ENJOY!!!!!!!")
