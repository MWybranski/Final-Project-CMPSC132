from pythonds.basic import Deque

#Creates a deque to store compliments
compliment_list = Deque()
compliment_list.addRear("Your creativity knows no bounds.")
compliment_list.addFront("You should be proud of yourself.")
compliment_list.addRear("You're a gift to those around you.")
compliment_list.addFront("You are enough.")
compliment_list.addRear("You are making a difference.")
compliment_list.addFront("On a scale from 1 to 10, you're an 11.")

def joyful_journeys():
    #Asks the user to choose between compliments, activities, or exiting the program
    main_question = input("Which part would you like to use today: Compliments or Activities (enter 'exit' to leave) ")
    #If the user chooses compliments
    if main_question.lower() == "compliments":
      #Remove and display the next compliment from the deque
      next_compliment = compliment_list.removeRear()
      compliment_list.addFront(next_compliment)
      print(next_compliment)
      #Recursively call the function for more choices
      joyful_journeys()
    #If the user chooses activities
    elif main_question.lower() == "activities":
      #Initialize an empty list to store chosen activities
      activity_list = []
      #Ask the user for preferences on various activities
      activity1 = input("Would you rather go for a walk or play video games? Type walk or video games: ")
      if activity1.lower() == "walk":
        activity_list.append("Go for a walk")
      elif activity1.lower() == "video games":
        activity_list.append("Play video games")
      activity2 = input("Would you rather spend 30 minutes exercising or meditating? Type exercising or meditating: ")
      if activity2.lower() == "exercising":
        activity_list.append("Exercise for 30 minutes")
      elif activity2.lower() == "meditating":
        activity_list.append("Meditate for 30 minutes")
      activity3 = input("Would you rather go to a concert or go to a football game? Type concert or game: ")
      if activity3.lower() == "concert":
        activity_list.append("Go to a concert")
      elif activity3.lower() == "game":
        activity_list.append("Go to a football game")
      activity4 = input("Would you rather watch a movie or start a new TV show? Type movie or show: ")
      if activity4.lower() == "movie":
        activity_list.append("Watch a movie")
      elif activity4.lower() == "show":
        activity_list.append("Start a new TV show")
      activity5 = input("Would you rather go to an aquarium or go to a zoo? Type aquarium or zoo: ")
      if activity5.lower() == "aquarium":
        activity_list.append("Go to an aquarium")
      elif activity5.lower() == "zoo":
        activity_list.append("Go to a zoo")
      activity6 = input("Would you rather read a book or go to a museum? Type book or museum: ")
      if activity6.lower() == "book":
        activity_list.append("Stay inside and read a book")
      elif activity6.lower() == "museum":
        activity_list.append("Go out to a museum")
      #Prints the list of chosen activities
      print(activity_list)
      #Recursively call the function for more choices
      joyful_journeys()
    #If the user enters an invalid choice for main_question
    elif not main_question.lower() == "compliments" and not main_question.lower() == "activities" and not main_question.lower() == "exit":
      print("You must type in either Compliments, Activities, or Exit")
      #Recursively call the function for another attempt
      joyful_journeys()

#Starts the program
joyful_journeys()