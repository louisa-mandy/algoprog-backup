''' THEORY FOR TAROT CARDS

Total Tarots cards available = 78 

it is devided in to 2 sections, which are the major arcana
and the minor arcana 

major arcana contains : 
 - from cards number 0 till 21 

the major arcana cards mostly describes about ones life journey. 
it talks about ones present state and the possibility / outcome 
its more to understanding ones feelings and awareness, even psychological,
spiritual development, and evolution. 

the major arcana has a larger and more crucial meaning compared to the minor arcana cards. 

minor arcana cards : 
 - from cards number 22 till 78 
 1. The Wands
 2. The Cups 
 3. The Swords 
 4. The Coins / pentacles 


from the name itself, these cards represents the minor or small mysteries and secrets of us who gets them. 

The minow arcana cards represents our daily activities / lives, snipets from our past/ present / future. 
contains slight information about your work, feelings, thoughts and even finances. 
'''

''' # IMPORTING AN IMAGE IN PYTHON
import tkinter as tk
from PIL import ImageTk, Image 
# PIL stands for pillow, which imports an image in this code  

# creating the main window for the image to pop up 
window = tk.Tk()
window.title("the_fool")
window.geometry("800x600") - maximum window size in replit 

# to load our image 
print("This is the result of your single daily reading card")
random_tarot_card = random.choice(tarot_cards)

image = Image.open(random_tarot_card)
photo = ImageTk.PhotoImage(image)
label = tk.Label(window, image = photo)
label.pack()
window.mainloop()

'''
import os  # to os clear / clear previous history
import random  # to randomize when shuffling the cards
import tkinter as tk  # importing tkinter for PIL to work

from PIL import Image, ImageTk


class person:

  #init to show the given variables
  def __init__(self, Intro, Occupation, Age, Hobby):

    # Instance Variable
    self.Intro = Intro
    self.Occupation = Occupation
    self.Age = Age
    self.Hobby = Hobby


tarot_cards = [
    "major_arcana/death.png","major_arcana/Reversed_death.png", "major_arcana/judgement.png","major_arcana/Reversed_judgement.png",
    "major_arcana/temperence.png", "major_arcana/Reversed_temperence.png","major_arcana/The_Chariot.png", "major_arcana/Reversed_The_Chariot.png",
    "major_arcana/The_Devil.png", "major_arcana/Reversed_The_Devil.png", "major_arcana/The_Emperor.png", "major_arcana/Reversed_The_Emperor.png",
    "major_arcana/The_Empress.png", "major_arcana/Reversed_The_Empress.png", "major_arcana/The_Fool.png", "major_arcana/Reversed_The_Fool.png", 
    "major_arcana/The_Hanged_Man.png", "major_arcana/Reversed_The_Hanged_Man.png", "major_arcana/The_Hermit.png", "major_arcana/Reversed_The_Hermit.png",
    "major_arcana/The_Hierophant.png", "major_arcana/Reversed_The_Hierophant.png", "major_arcana/The_High_Priestess.png", "major_arcana/Reversed_The_High_Priestess.png",
    "major_arcana/The_Justice.png", "major_arcana/Reversed_The_Justice.png", "major_arcana/The_Lovers.png", "major_arcana/Reversed_The_Lovers.png",
    "major_arcana/The_Magician.png", "major_arcana/Reversed_The_Magician.png", "major_arcana/The_Moon.png", "major_arcana/Reversed_The_Moon.png",
    "major_arcana/The_Star.png", "major_arcana/Reversed_The_Star.png", "major_arcana/The_Strength.png", "major_arcana/Reversed_The_Strength.png",
    "major_arcana/The_Sun.png", "major_arcana/Reversed_The_Sun.png", "major_arcana/The_Tower.png", "major_arcana/Reversed_The_Tower.png",
    "major_arcana/The_Wheel_Of_Fortune.png", "major_arcana/Reversed_The_Wheel_Of_Fortune.png", "major_arcana/The_World.png", "major_arcana/Reversed_The_World.png",
    "minor_arcana/41.png","minor_arcana/42.png", "minor_arcana/43.png", "minor_arcana/44.png", "minor_arcana/45.png",
    "minor_arcana/46.png", "minor_arcana/47.png", "minor_arcana/48.png", "minor_arcana/49.png", "minor_arcana/50.png", "minor_arcana/51.png",
    "minor_arcana/52.png", "minor_arcana/53.png", "minor_arcana/54.png", "minor_arcana/55.png", "minor_arcana/56.png",
    "minor_arcana/57.png", "minor_arcana/58.png", "minor_arcana/59.png", "minor_arcana/60.png", "minor_arcana/61.png",
    "minor_arcana/62.png", "minor_arcana/63.png", "minor_arcana/64.png", "minor_arcana/65.png", "minor_arcana/66.png",
    "minor_arcana/67.png", "minor_arcana/68.png", "minor_arcana/69.png", "minor_arcana/70.png","minor_arcana/71.png",
    "minor_arcana/72.png", "minor_arcana/73.png", "minor_arcana/74.png", "minor_arcana/75.png", "minor_arcana/76.png",
    "minor_arcana/77.png", "minor_arcana/78.png", "minor_arcana/79.png", "minor_arcana/80.png", "minor_arcana/81.png",
    "minor_arcana/82.png", "minor_arcana/83.png", "minor_arcana/84.png", "minor_arcana/85.png", "minor_arcana/86.png",
    "minor_arcana/87.png", "minor_arcana/88.png", "minor_arcana/89.png", "minor_arcana/90.png", "minor_arcana/91.png",
    "minor_arcana/92.png", "minor_arcana/93.png", "minor_arcana/94.png", "minor_arcana/95.png", "minor_arcana/96.png",
    "minor_arcana/97.png", "minor_arcana/98.png", "minor_arcana/99.png", "minor_arcana/100.png", "minor_arcana/101.png",
    "minor_arcana/102.png", "minor_arcana/103.png", "minor_arcana/104.png", "minor_arcana/105.png", "minor_arcana/106.png",
    "minor_arcana/107.png", "minor_arcana/108.png", "minor_arcana/109.png", "minor_arcana/110.png", "minor_arcana/111.png",
    "minor_arcana/112.png", "minor_arcana/113.png", "minor_arcana/114.png", "minor_arcana/115.png", "minor_arcana/116.png",
    "minor_arcana/117.png", "minor_arcana/118.png", "minor_arcana/119.png", "minor_arcana/120.png", "minor_arcana/121.png",
    "minor_arcana/122.png", "minor_arcana/123.png", "minor_arcana/124.png", "minor_arcana/125.png", "minor_arcana/126.png",
    "minor_arcana/127.png", "minor_arcana/128.png", "minor_arcana/129.png", "minor_arcana/130.png", "minor_arcana/131.png",
    "minor_arcana/132.png", "minor_arcana/133.png", "minor_arcana/134.png", "minor_arcana/135.png", "minor_arcana/136.png",
    "minor_arcana/137.png", "minor_arcana/138.png", "minor_arcana/139.png", "minor_arcana/140.png", "minor_arcana/141.png", 
    "minor_arcana/142.png", "minor_arcana/143.png", "minor_arcana/144.png", "minor_arcana/145.png", "minor_arcana/146.png",
    "minor_arcana/147.png", "minor_arcana/148.png", "minor_arcana/149.png", "minor_arcana/150.png", "minor_arcana/151.png",
    "minor_arcana/152.png", "minor_arcana/153.png", "minor_arcana/154.png", "minor_arcana/155.png", "minor_arcana/156.png"
]

window_size = "900x600" # use this instead of repeating the window size

title = " Welcome To Your Trusty Online Tarot Reading!! "
decorated_title = title.center(50)

print("=" * 72)
print("")
print(("=" * 10), decorated_title, ("=" * 10))
print("")
print("=" * 72)

input()

while True:
  print("")
  print("which type of reading would you like to do?")

  print(
      "1. Second Party Tarot Reading \n2. Personal Tarot Reading")
  print("3. Clear History \n4. EXIT PROGRAM")
  print("")
  user_input = int(input("enter an option: "))  #user input

  if user_input == 1: # option 1. where the user wants to read about somebody else 
    print("Let's start reading their cards!")
    print("")
    user_name = input(
        "enter the name of the person that you want to do a reading on")
    user_job = input("enter their occupation")
    user_age = int(input("enter their age"))
    user_hobby = input("enter their hobby")
    print("")
    
    # Objects
    user = person(user_name, user_job, user_age, user_hobby)
    print("")
    print("Users Info :")
    print("")
    print("1. Name :", user.Intro)
    print("")
    print("2. Occupation :", user.Occupation)
    print("")
    print("3. Age :", user.Age)
    print("")
    print("4. Hobby :", user.Hobby)

    print("")
    print("Tarot Cards are divided into multiple types of reading styles,")

    print("and that includes these 5 options.")
    print("")

    print("Please choose one of the reading options below")
    print("according to what you want to know about", user_name )
    print("")

    print("1. General \n2. Spiritual \n3. Growth \n4. Love \n5. Career")

    print("6. Rate The Program ;) \n7. EXIT PROGRAM ")

    print("")
    user_input = int(input("enter an option: "))  #user input

    if user_input == 1:
      print("")  #adds a space
      print("When reading a general card, there are a few ways to do it")

      print("1. a Single Card for", user_name, "-" * 5)
      print("")
      print(
          " ",
          "For daily readings and yes or no questions related to", user_name,"'s", " current situation"
      )

      print("")  #adds a space

      print("2.", user_name, "'s", "Past, Present, Future", "-" * 5)
      print("")
      print(
          " ",
          "a deeper understanding of", user_name, "'s", "journey in the Past, Present, and Future"
      )

      print("")  #adds a space

      print("3.", user_name, "'s", "Situation, Action, Outcome", "-" * 5)
      print("")
      print(
          " ",
          "Helps to understand how", user_name, "can affect a particular situation")

      print("")  #adds a space

      print("4. Three Options for", user_name, "-" * 5)
      print("")
      print(" ", "To help" , user_name, "think through three choices")

      user_input = int(input("enter an option: "))  #user input

      if user_input == 1:

        print("")
        print("This is the result of", user_name,"'s", "daily reading card")

        window = tk.Tk()
        window.title("Reading")  # naming the pop up window
        window.geometry(window_size)  # window size

        random_tarot_card = random.choice(tarot_cards)

        # to load image
        image = Image.open(random_tarot_card)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=photo)
        label.pack()
        window.mainloop()

      elif user_input == 2:
        print("")
        print(
            "This is the result of", user_name ,"'s", "Past, Present, And Future reading card"
        )

        for _ in range(3):

          window_names = ["Past", "Present", "Future"]
          window = tk.Tk()
          window.title(window_names[_])  # looping the window

          window.geometry(window_size)  # window size

          random_tarot_card = random.choice(tarot_cards)

          # to load image
          image = Image.open(random_tarot_card)
          photo = ImageTk.PhotoImage(image)
          label = tk.Label(window, image=photo)
          label.pack()
          window.mainloop()

      elif user_input == 3:
        print("")
        print(
            "This is the result of", user_name,"'s"," Situation, Action, And Outcome reading card"
        )

        for _ in range(3):  # looping the card to shuffle for 3 times

          window_names = ["Situation", "Action", "Outcome"]
          window = tk.Tk()
          window.title(window_names[_]
                       )  # naming the pop up window as how many times it loops

          window.geometry(window_size)  # window size

          random_tarot_card = random.choice(tarot_cards)

          # to load image
          image = Image.open(random_tarot_card)
          photo = ImageTk.PhotoImage(image)
          label = tk.Label(window, image=photo)
          label.pack()
          window.mainloop()

      elif user_input == 4:
        print("")
        print("These are the available options for", user_name)
        for _ in range(3):  # looping the card to shuffle for 3 times

          window_names = ["Option_1", "Option_2", "Option_3"]
          window = tk.Tk()
          window.title(window_names[_]
                       )  # naming the pop up window as how many times it loops

          window.geometry(window_size)  # window size

          random_tarot_card = random.choice(tarot_cards)

          # to load image
          image = Image.open(random_tarot_card)
          photo = ImageTk.PhotoImage(image)
          label = tk.Label(window, image=photo)
          label.pack()
          window.mainloop()

      else:
        print("Please input a number available from the option ")

    elif user_input == 2: 
      print("There are two ways to read a spiritual tarot card:")

      print("")
      print("1. Mind, Body, Spirit")
      print("")
      print("", "an overall reflection of" , user_name,"'s", "current self")
      print("", "depending on their situation")

      print("")
      print("2. Dream Interpretation")
      print("")
      print("", "After waking up from a powerful dream,")
      print("","these cards will help" , user_name, "to understand the subconscious meaning behind it all")

      print("")
      user_input = int(input("Enter an Option here:"))

      if user_input == 1:  # if user input 'Mind, Body, Spirit'
        print("")
        print("These cards represents" , user_name,"'s", "mind, body, and spirit")

        for _ in range(3):  # looping the card to shuffle for 3 times

          window_names = ["Mind", "Body", "Spirit"]
          window = tk.Tk()
          window.title(window_names[_]
                       )  # naming the pop up window as how many times it loops

          window.geometry(window_size)  # window size

          random_tarot_card = random.choice(tarot_cards)

          # to load image
          image = Image.open(random_tarot_card)
          photo = ImageTk.PhotoImage(image)
          label = tk.Label(window, image=photo)
          label.pack()
          window.mainloop()

      elif user_input == 2:  # if user input 'Dream interpertation'
        print("")
        print("These cards represents on how" , user_name," can interprets dreams")
        for _ in range(3):  # looping the card to shuffle for 3 times

          window_names = [
              "Dream_Origin", "Dream_Message", "Dream_interpertation"
          ]
          window = tk.Tk()
          window.title(window_names[_]
                       )  # naming the pop up window as how many times it loops

          window.geometry(window_size)  # window size

          random_tarot_card = random.choice(tarot_cards)

          # to load image
          image = Image.open(random_tarot_card)
          photo = ImageTk.PhotoImage(image)
          label = tk.Label(window, image=photo)
          label.pack()
          window.mainloop()
      else:
        print("Please input a number available from the option ")

    elif user_input == 3:  #if user inputs Growth

      print("")
      print("Self Assessment and Advice")
      print("")
      print("", "How", user_name,"should approach a problem")
      print("", "given the level of weakness and strenghts they have")

      print("")
      print("These cards shows", user_name,"'s", "weaknesses, strenghts, and advices")

      for _ in range(3):  # looping the card to shuffle for 3 times

        window_names = ["weaknesses", "Strengths", "Advices"]
        window = tk.Tk()
        window.title(window_names[_]
                     )  # naming the pop up window as how many times it loops

        window.geometry(window_size)  # window size

        random_tarot_card = random.choice(tarot_cards)

        # to load image
        image = Image.open(random_tarot_card)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=photo)
        label.pack()
        window.mainloop()

    elif user_input == 4:  # user inputs Love
      print("")
      print("When talking about love,")
      print("surely you are curious on how their relationship will go")
      print("")
      print("this is a short reading to know", user_name,"'s", "relationship dynamics")
      print("with their significant other")
      print("")
      print("These cards represents" , user_name, user_name,"'s","Dynamics, and", user_name,"'s", "Partner")

      for _ in range(3):  # looping the card to shuffle for 3 times

        window_names = ["Them", "Relationship_Dynamic", "Their_Partner"]
        window = tk.Tk()
        window.title(window_names[_]
                     )  # naming the pop up window as how many times it loops

        window.geometry(window_size)  # window size

        random_tarot_card = random.choice(tarot_cards)

        # to load image
        image = Image.open(random_tarot_card)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=photo)
        label.pack()
        window.mainloop()

    elif user_input == 5:  # user inputs career

      print("")
      print("These cards represents:")
      print("Card 1 = Will money be coming to" , user_name,"'s", "life very soon?")
      print(
          "Card 2 = What career opportunities does", user_name, "need to consider more closely?"
      )
      print(
          "Card 3 = What allies or obsticles will" , user_name, "face along the way to financial statisfication?"
      )

      for _ in range(3):  # looping the card to shuffle for 3 times

        window_names = ["Possible_Income", "career_opportunities", "Obsticles"]
        window = tk.Tk()
        window.title(window_names[_]
                     )  # naming the pop up window as how many times it loops

        window.geometry(window_size)  # window size

        random_tarot_card = random.choice(tarot_cards)

        # to load image
        image = Image.open(random_tarot_card)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=photo)
        label.pack()
        window.mainloop()

    elif user_input == 6:
      print("")
      print(
          "What do you think of this tarot reading program ?, Rate it from 1-5 pls ( > 3 <333 ) "
      )
      print("")
      print(
          "1. WOWWW AMAZING JNCIAHCJ \n2. pretty coollll-- \n3. Its Okelah *thumbs up*"
      )
      print("4. ehm Mid -_- \n5. no comment....")
      user_input = int(input("please enter rating: "))

      if user_input == 1:
        print("OMG SLAYYY PURR THANK YEWW ")

      elif user_input == 2:
        print("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧ ")

      elif user_input == 3:
        print(" <⁠(⁠￣⁠︶⁠￣⁠)⁠> ")

      elif user_input == 4:
        print(" hshshs i'll do better :⁠'⁠( ")

      elif user_input == 5:
        print(" bruh :-: ")
      else:
        print(" ಠ⁠ ⁠೧⁠ ⁠ಠ wow ")

    elif user_input == 7:  # for exiting the program
      print(" Thank you for experiencing 'Your Trusty Online Tarot Reading'")
      break

    else:
      print("")
      print(" Please input a valid number available from the option")

  elif user_input == 2:
    print("")
    print("")
    print("Tarot Cards are divided into multiple types of reading styles,")

    print("and that includes these 5 options.")
    print("")

    print("Please choose one of the reading options below")
    print("according to what you want to know about yourself.")
    print("")

    print("1. General \n2. Spiritual \n3. Growth \n4. Love \n5. Career")

    print("6. Rate The Program ;) \n7. EXIT PROGRAM ")

    print("")
    user_input = int(input("enter an option: "))  #user input

    if user_input == 1:
      print("")  #adds a space
      print("When reading a general card, there are a few ways to do it")

      print("1. Single Card ", "-" * 5)
      print("")
      print(
          " ",
          "For daily readings and yes or no questions related to your situation"
      )

      print("")  #adds a space

      print("2. Past, Present, Future", "-" * 5)
      print("")
      print(
          " ",
          "a deeper understanding of ones journey in the Past, Present, and Future"
      )

      print("")  #adds a space

      print("3. Situation, Action, Outcome", "-" * 5)
      print("")
      print(
          " ",
          "Helps you understand how you can affect in a particular situation")

      print("")  #adds a space

      print("4. Three Options", "-" * 5)
      print("")
      print(" ", "To help you think through three choices")

      user_input = int(input("enter an option: "))  #user input

      if user_input == 1:

        print("")
        print("This is the result of your single daily reading card")

        window = tk.Tk()
        window.title("Your_Reading")  # naming the pop up window
        window.geometry(window_size)  # window size

        random_tarot_card = random.choice(tarot_cards)

        # to load image
        image = Image.open(random_tarot_card)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=photo)
        label.pack()
        window.mainloop()

      elif user_input == 2:
        print("")
        print(
            "This is the result of your Past, Present, And Future reading card"
        )

        for _ in range(3):

          window_names = ["Your_Past", "Your_Present", "Your_Future"]
          window = tk.Tk()
          window.title(window_names[_])  # looping the window

          window.geometry(window_size)  # window size

          random_tarot_card = random.choice(tarot_cards)

          # to load image
          image = Image.open(random_tarot_card)
          photo = ImageTk.PhotoImage(image)
          label = tk.Label(window, image=photo)
          label.pack()
          window.mainloop()

      elif user_input == 3:
        print("")
        print(
            "This is the result of your Situation, Action, And Outcome reading card"
        )

        for _ in range(3):  # looping the card to shuffle for 3 times

          window_names = ["Your_Situation", "Your_Action", "Your_Outcome"]
          window = tk.Tk()
          window.title(window_names[_]
                       )  # naming the pop up window as how many times it loops

          window.geometry(window_size)  # window size

          random_tarot_card = random.choice(tarot_cards)

          # to load image
          image = Image.open(random_tarot_card)
          photo = ImageTk.PhotoImage(image)
          label = tk.Label(window, image=photo)
          label.pack()
          window.mainloop()

      elif user_input == 4:
        print("")
        print("These are your options")

        for _ in range(3):  # looping the card to shuffle for 3 times

          window_names = ["Option_1", "Option_2", "Option_3"]
          window = tk.Tk()
          window.title(window_names[_]
                       )  # naming the pop up window as how many times it loops

          window.geometry(window_size)  # window size

          random_tarot_card = random.choice(tarot_cards)

          # to load image
          image = Image.open(random_tarot_card)
          photo = ImageTk.PhotoImage(image)
          label = tk.Label(window, image=photo)
          label.pack()
          window.mainloop()

      else:
        print("Please input a number available from the option ")

    elif user_input == 2:
      print("There are two ways to read a spiritual tarot card:")

      print("")
      print("1. Mind, Body, Spirit")
      print("")
      print("", "an overall reflection of your current self")
      print("", "depending on your situation")

      print("")
      print("2. Dream Interpretation")
      print("")
      print("", "After waking up from a powerful dream,")
      print(
          "",
          "these cards will help you understand the subconscious meaing behind it all"
      )

      print("")
      user_input = int(input("Enter an Option here:"))

      if user_input == 1:  # if user input 'Mind, Body, Spirit'
        print("")
        print("These cards represent your mind, body, and spirit")

        for _ in range(3):  # looping the card to shuffle for 3 times

          window_names = ["Your_Mind", "Your_Body", "Your_Spirit"]
          window = tk.Tk()
          window.title(window_names[_]
                       )  # naming the pop up window as how many times it loops

          window.geometry(window_size)  # window size

          random_tarot_card = random.choice(tarot_cards)

          # to load image
          image = Image.open(random_tarot_card)
          photo = ImageTk.PhotoImage(image)
          label = tk.Label(window, image=photo)
          label.pack()
          window.mainloop()

      elif user_input == 2:  # if user input 'Dream interpertation'
        print("")
        print("These cards represents on how you interpret your dreams")
        for _ in range(3):  # looping the card to shuffle for 3 times

          window_names = [
              "Dream_Origin", "Dream_Message", "Dream_interpertation"
          ]
          window = tk.Tk()
          window.title(window_names[_]
                       )  # naming the pop up window as how many times it loops

          window.geometry(window_size)  # window size

          random_tarot_card = random.choice(tarot_cards)

          # to load image
          image = Image.open(random_tarot_card)
          photo = ImageTk.PhotoImage(image)
          label = tk.Label(window, image=photo)
          label.pack()
          window.mainloop()
      else:
        print("Please input a number available from the option ")

    elif user_input == 3:  #if user inputs Growth

      print("")
      print("Self Assessment and Advice")
      print("")
      print("", "How you should approach a problem")
      print("", "given the level of weakness and strenghts you have")

      print("")
      print("These cards shows your weaknesses, strenghts, and advices")

      for _ in range(3):  # looping the card to shuffle for 3 times

        window_names = ["Your_weaknesses", "Your_Strengths", "Advices"]
        window = tk.Tk()
        window.title(window_names[_]
        
                     )  # naming the pop up window as how many times it loops

        window.geometry(window_size)  # window size

        random_tarot_card = random.choice(tarot_cards)

        # to load image
        image = Image.open(random_tarot_card)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=photo)
        label.pack()
        window.mainloop()
   
    elif user_input == 4:  # user inputs Love
      print("")
      print("When talking about love,")
      print("surely you are curious on how your relationship will go")
      print("")
      print("this is a short reading to know your relationship dynamics")
      print("with your significant other")
      print("")
      print("These cards represents Yourself, The Dynamics, and Your Partner")

      for _ in range(3):  # looping the card to shuffle for 3 times

        window_names = ["You_yourself", "Relationship_Dynamic", "Your_Partner"]
        window = tk.Tk()
        window.title(window_names[_]
                     )  # naming the pop up window as how many times it loops

        window.geometry(window_size)  # window size

        random_tarot_card = random.choice(tarot_cards)

        # to load image
        image = Image.open(random_tarot_card)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=photo)
        label.pack()
        window.mainloop()

    elif user_input == 5:  # user inputs career

      print("")
      print("These cards represents:")
      print("Card 1 = Will money be coming into my life very soon?")
      print(
          "Card 2 = What career opportunities do i need to consider more closely?"
      )
      print(
          "Card 3 = What allies or obsticles will i face along the way to financial statisfication?"
      )

      for _ in range(3):  # looping the card to shuffle for 3 times

        window_names = ["Possible_Income", "career_opportunities", "Obsticles"]
        window = tk.Tk()
        window.title(window_names[_]
                     )  # naming the pop up window as how many times it loops

        window.geometry(window_size)  # window size

        random_tarot_card = random.choice(tarot_cards)

        # to load image
        image = Image.open(random_tarot_card)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=photo)
        label.pack()
        window.mainloop()


    elif user_input == 6 :  # rating, cause why not

      print("")
      print(
          "What do you think of this tarot reading program ?, Rate it from 1-5 pls ( > 3 <333 ) "
      )
      print("")
      print(
          "1. WOWWW AMAZING JNCIAHCJ \n2. pretty coollll-- \n3. Its Okelah *thumbs up*"
      )
      print("4. ehm Mid -_- \n5. no comment....")
      user_input = int(input("please enter rating: "))

      if user_input == 1:
        print("OMG SLAYYY PURR THANK YEWW ")

      elif user_input == 2:
        print("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧ ")

      elif user_input == 3:
        print(" <⁠(⁠￣⁠︶⁠￣⁠)⁠> ")

      elif user_input == 4:
        print(" hshshs i'll do better :⁠'⁠( ")

      elif user_input == 5:
        print(" bruh :-: ")
      else:
        print(" ಠ⁠ ⁠೧⁠ ⁠ಠ wow ")

    elif user_input == 7:
      print(" Thank you for experiencing 'Your Trusty Online Tarot Reading'")
      break

    else:
      print("")
      print(" Please select a valid number available from the option")

  elif user_input == 3: # function
    print("")
    print("Your history has been cleared")
    def clear_screen():
      os.system('cls' if os.name == 'nt' else 'clear')
    clear_screen()

  elif user_input == 4: 
    print("")
    print("Thank you for experiencing 'Your Trusty Online Tarot Reading'")
    break
  else:
    print("")
    print("Please Input a valid number from the option")

# resources
# wikihow, pinterest ( for art inspo )
# golden thread tarot, astrologyanswers.com, labyrinthos (for tarot theories )
# stack overflow, geeksforgeeks

# addition
# when user exit program, add a function where they can rate the program and put a review [x]
# print the name of the tarot card in the console when the picture shows up in the output page
# add defenitions of each card so users can understand what the cards stands for in given situations


# ADJUSTMENTS 
# CHANGE LILLY TO UDER_NAME 
