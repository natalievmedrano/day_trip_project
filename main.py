#Store the trip options for destinations, restaurants, transportation, and entertainment each in their own List 
#Get a random element from each of those sets of options. 
#Display the initial random trip to your user
#Prompt the user to see if they are satisfied
#If not, find out which trip feature they want to change and randomly select a new feature.
#Keep doing this process until the user is satisfied with the trip

greeting_message= "WELCOME TO 'MY U.S.A DAY TRIP GENERATOR' WE LOOK FORWARD TO HELP YOU PLAN THE VACATION OF YOUR DREAMS"
print(greeting_message)

#variables
usa_destinations=['New York City,NY','Atlanta,GA',"Washington,D.C","Austin,TX","Las Vegas NV","Los Angeles,CA"]
usa_resturants=['Mcdonalds','Cheesecake Factory','Taco Cabana','Cheddars','Wings n More','Texas Road House']
usa_transportations=['train','car','plane','bus','walking','swimming']
usa_entertainments=['casino','museum','movies','shopping','theme park','kayaking']

#selected things/choices for user
import random
def choice(self, seq):
    destinations= random.choice(usa_destinations)
    resturants= random.choice(usa_resturants)
    transportations= random.choice(usa_transportations)
    entertainments= random.choice(usa_entertainments)

#second greeting

second_greeting = 'Here is the first selected trip for you!'
print(second_greeting)

# when program is ran these will be the first ones chosen
chosen_destination= 'For your destination: {destination}'
chosen_resturant= 'For refreshments and meals: {resturants}'
chosen_transportation= 'For transportation: {transportations}'
chosen_entertainment= 'For entertainment: {entertainments}'

print('ARE YOU SATISFIED WITH THIS TRIP? please state yes or no.')


#allow user to confirm or deny trip
user_confirmation= input('Type YES or NO to confirm.')

#if user isnt satisfied with the selections...
print("Thank you for your input! Let's change that really quick which part of your trip would you like to change?")

#destinations= print()
#testurants=print()
#transportations= print()
#entertainments= print()
#i think i have to create many elifs for this part 

#print("ARE YOU HAPPY WITH YOUR U.S.A VACATION? Y OR N")
#here i have to create a boolean i think

#print (WHICH PART OF YOUR TRIP WOULD YOU LIKE TO CHANGE?)
# for this part we need to use an input function

#print ('ANYTHING ELSE YOU WOULD LIKE TO CHANGE Y OR N)

#print('CONFIRM TRIP BY SAYING YES OR NO')

#print("")

