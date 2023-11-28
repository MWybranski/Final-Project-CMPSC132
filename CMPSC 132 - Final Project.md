# **Joyful Journeys**

Mathew Danese & Matthew Wybranski

**Goal**

Our program aims to help others and advance their happiness by giving them suggestions on what they can do. The ultimate aim is to contribute to people's happiness. Happiness can be subjective, but our program aims to suggest activities or actions that align with an individual's interests, ultimately leading them to a happier state.

**Significance**

The program can give the user compliments in order to brighten their day. It can also give the user a list of fun activities through questions and user input that they can do to help make their day better. Incorporating compliments into the program is a wonderful way to start the interaction on a positive note. A genuine compliment can uplift the user's mood, fostering a positive atmosphere from the beginning.

**Installation and Usage Instructions**

- **Installation**

1. Install pythonds
2. Import Deque from pythonds
3. Run the program

- **Usage**

1. When asked for user input, type either compliments, activities, or exit
2. If user enters activities, they will need to choose which ones they want to do

**Code Structure**

See image in Github

**List of Functionalities and Test Results**

First, the user will be prompted to answer a question and provide a response. Based on the response, the function joyful\_journeys() will know what to do. If the user enters compliments, it will display one of the six compliments stored in the deque such as "You're a gift to those around you."

On the other hand, if the user enters activities the program will provide 6 would you rather questions that will provide a list of the six activities the user selected from the options provided. For example, this list could be a result based on user input ['Play video games', 'Exercise for 30 minutes', 'Go to a football game', 'Watch a movie', 'Go to an aquarium', 'Stay inside and read a book'].

Finally, if the user does not type compliments, activities, or exit the program will print out an error message that says "You must type in either Compliments, Activities, or Exit."

**Discussion and Conclusions**

Limitations/Issues:

- We cannot randomize the order of the compliments
- Invalid user input for the activities will lead to empty spaces in the list

Application of course learnings:

- We used deque to store the compliments
- We used list to store the activities that the user will participate in
- We recursively called the functions