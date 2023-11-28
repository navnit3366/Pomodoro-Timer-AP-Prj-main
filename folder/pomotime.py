#############################################################
# pomotime.py
#   The goal is to encourage students and others to start working 
#       by keeping them focused throughout several sessions of 
#       working and breaks while inspiring quotes are displayed to 
#       keep them encouraged.
#############################################################

####### CITATIONS ########
# Import of Random library citation: 
# https://docs.python.org/3/library/random.html © Copyright 2001-2022, Python Software Foundation. 

# Import of Time library citation: 
# https://docs.python.org/3/library/time.html © Copyright 2001-2022, Python Software Foundation. 

# Import of Tkinter library citation:
# https://docs.python.org/3/library/tkinter.html © Copyright 2001-2022, Python Software Foundation. 

# Import of Tkinter Messagebox library citation:
# https://docs.python.org/3/library/tkinter.messagebox.html © Copyright 2001-2022, Python Software Foundation. 

# Import of PIL Tools Image Module citation:
# https://pillow.readthedocs.io/en/stable/reference/Image.html © Copyright 1995-2011 Fredrik Lundh, 2010-2022 Alex Clark and Contributors.

# Import of PIL Tools ImageTK Module citation:
# https://pillow.readthedocs.io/en/stable/reference/ImageTk.html © Copyright 1995-2011 Fredrik Lundh, 2010-2022 Alex Clark and Contributors.

# Import of Textwrap library citation:
# https://docs.python.org/3/library/textwrap.html © Copyright 2001-2022, Python Software Foundation.

# Background Image Citation:
# Created by code creater(me) through canva(canva.com)

# Inspirational quotes data source citation:
# Bright Culture. “202 Motivational Quotes for Students - Get Motivated While Studying.” Bright Culture, 16 Jan. 
#   2021, https://bright-culture.com/exam-tips-for-students/202-motivational-quotes-for-students-studying/. 
##########################

# imports
import random
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox # end session messageboxes
from PIL import Image, ImageTk # used to upload image to tk bg
import textwrap # used for textwrapping the quote in label

# takes random quote from list(quotes.txt) and category from quotes2.txt
def RandomQuote(n):
    mylines = [] 
    category = []
    random_line = random.randint(1,202) # picks random number from 1 to 202            
    # Open quotes.txt and read in quotes
    with open ('quotes.txt', encoding='utf-8') as myfile: 
        for myline in myfile:                
            mylines.append(myline)  
    # Open quotes2.txt and read in categories( 0 and 1 )
    with open ('quotes2.txt', encoding='utf-8') as myfile: 
        for myline in myfile:                
            category.append(myline) # sues same line that is the random quote
    global quote_choice  
    quote_choice = str(mylines[random_line]) # assign random quote variable
    global quote_category
    quote_category = str(category[random_line]) # assign random quote's category to variable
    quote_category = int(quote_category) # set variable to int 
    quote_choice = textwrap.fill(quote_choice, 18) # sets limit of 18 characters for quote
    # call the display function
    displayQuotes(quote_choice, quote_category, n)

# quotes display function
def displayQuotes(quote_choice, quote_category, n):
    if quote_category == 0:
        quote_label.config(bg= "#FFCCDD", fg= "#FF4D6A") # makes pink if motivational
    elif quote_category == 1:
        quote_label.config(bg= "#b6e6a5", fg= "#53bd65") # makes green if philosophical

    for i in range (n): # n is used to limit it from looping more than 1 time(since thats all that is needed)
        Quo.set(quote_choice) # set quote label text variable to tje random quote
        # update screen now
        window.update()
        time.sleep(1) # 1 second delay in display
    
# display timer function
def displayTime(timer):
    # displays minutes and seconds       
    minutes, seconds = divmod(timer, 60)
    Min.set(f"{minutes:02d}") # sets to only 2 decimals places diplayed
    Sec.set(f"{seconds:02d}") # sets to only 2 decimals places diplayed
    # update screen now
    window.update()
    time.sleep(1)
        
# Work function --> 25 minutes
def work():
    timer = 25* 60 # 25 minutes --> seconds
    quote_timer = 25 * 60
    n = 1 # only displays the quote once
    while timer >= 0:
        # call display timer fucntion to update timer while its running
        displayTime(timer)
        if timer == 0:
            messagebox.showinfo("Pomodoro Timer Alert", "Work Done\n------------------------\nGreat job, break time!\nClick Break Button")
        # subtract second from timer while true
        timer -= 1

        while quote_timer >= 0:
            if quote_timer == 25 * 60:
                RandomQuote(n)
            quote_timer -= 1

# short break function --> 5 minutes
def short_break():
    timer = 5*60 # 5 minutes --> seconds
    n = 1 # only displays the quote once
    quote_timer = 5*60 
    while timer >= 0:
        # call display timer fucntion to update timer while its running
        displayTime(timer)
        if timer == 0:
            messagebox.showinfo("Pomodoro Timer Alert", "Short break Done\n--------------------------\nTime to get to work!\nClick Work Button")
        # subtract second from timer while true
        timer -= 1

        while quote_timer >= 0:
            if quote_timer == 5*60:
                RandomQuote(n)
            # subtract second from timer while true
            quote_timer -= 1

# long break function --> 10 minutes
def long_break():
    timer = 10 * 60 # 10 minutes --> seconds
    n = 1 # only displays the quote once
    quote_timer = 10 * 60
    while timer >= 0:
        # call display timer fucntion to update timer while its running
        displayTime(timer)
        if timer == 0:
            messagebox.showinfo("Pomodoro Timer Alert", "Long break done\n------------------------\nTime to get to work!\nClick Work Button")
        # subtract second from timer while true
        timer -= 1

        # display a quote at the beginning of this cycle 
        while quote_timer >= 0:
            if quote_timer == 10 * 60: # when this timer is at 10 minutes... display quote
                RandomQuote(n) # makes new random quote and displays it
            # subtract second from timer while true
            quote_timer -= 1

# display of users name they inputed
name_input = input("Hello! What is your name?")
name = "Welcome " + name_input + "!"

######################################
######################################
# directions printed in console below 
for i in range(4):
    print("-------READ BELOW THIS-------")
print("-------WELCOME TO POMOTIME!-------")
print("Here you can use the pomodoro method for a more focused studying or work session!")
print("-------HOW DOES IT WORK-------")
print("The pomodoro method set up is to do work session then short break and repeat twice and then after one final work session a longer break")
print("-------POMODORO METHOD SCHEDULE-------\n--\nWORK: 25 mins\n--\nBREAK: 5 mins\n--\nWORK:25 mins\n--\nBREAK: 5 mins\n--\nWORK: 25 mins\n--\nBREAK: 10 mins\n--\nREPEAT FROM START(do however many times)")
print("--\nWhen beginning either a work or break session a random quote will be displayed in either pink(motivational) or green(philsophical)")
print("--\nHopefully you find some success or enjoyment in this process :) \nHave fun!!!!")
for i in range(4):
    print("-------READ ABOVE THIS-------")
######################################
######################################

# pomo schedule to be displayed onto tk window
pomo_schedule = "-------POMODORO METHOD SCHEDULE-------\nWORK: 25 mins\n--\nSHORT BREAK: 5 mins\n--\nWORK:25 mins\n--\nSHORT BREAK: 5 mins\n--\nWORK: 25 mins\n--\nLONG BREAK: 10 mins\n--\nREPEAT FROM START"

# GUI using tk/tkinter
# this will be the tkinter set up
window = Tk()
window.geometry("1000x500")
window.resizable(False, False)
window.title("Pomodoro Timer")

# setting up canvas
canvas = tk.Canvas(window)
canvas.pack(expand=True, fill="both")
img = Image.open('blue_bg.png') # setting image as background
bg = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=bg, anchor="nw")

# Variables to keep track and display (setting them to strs so they can be displayed)
Min=StringVar()
Sec=StringVar()
Quo=StringVar()
Name=StringVar()
Schedule=StringVar()

# set default time/ quote/ name/ schedule
Min.set("25")
Sec.set("00")
Quo.set("")
Name.set(name)
Schedule.set(pomo_schedule)

# label to tell user to read terminal with the instructions
canvas.create_text(500, 75, text = "Read your terminal before starting!!!")

# minutes title
canvas.create_text(465, 300, text = "Minutes(s)")

# where minutes will be displayed
min_label = tk.Label(window,textvariable=Min, font=("arial", 22))
min_label.place(x=445,y=240)

# used as divider between mins and secs
divider_label = tk.Label(window,text="::", font=("arial", 22))
divider_label.place(x=490,y=240)

# seconds title
canvas.create_text(545, 300, text = "Second(s)")

# where secs will be displayed
sec_label = tk.Label(window,textvariable=Sec, font=("arial", 22))
sec_label.place(x=520,y=240)

#name title/ where welcome 'your name' will be displayed
name_label = tk.Label(window, textvariable=Name, font=("Fixedsys", 30), width=20, height=1, borderwidth=3, relief="groove")
name_label.place(x=295,y=20)

# where quote will be displayed 
quote_label = tk.Label(window, textvariable=Quo, font=("arial", 16), width=16, height=14, borderwidth=3, relief="ridge")
quote_label.place(x=735,y=80)

# Pomo Schedule display label
pomosch_label = tk.Label(window,textvariable=Schedule, font=("arial", 6), width=30, height=15, borderwidth=3, relief="groove")
pomosch_label.place(x=555,y=335)

# Buttons ###################
# work button
work_button = Button(window, text='Work', font=("Fixedsys", 15),command= work, width=20, height=3, borderwidth=3, relief="ridge")
work_button.place(x = 60, y = 85)

# short break button
shortb_button = Button(window, text='Short Break', font=("Fixedsys", 15), command= short_break, width=20, height=3, borderwidth=3, relief="ridge")
shortb_button.place(x = 60, y = 210)

# long break button
longb_button = Button(window, text='Long Break', font=("Fixedsys", 15),command= long_break, width=20, height=3, borderwidth=3, relief="ridge")
longb_button.place(x = 60, y = 335)

# end window main loop
window.mainloop()

# quotes.txt contents #######################################################
# “The mind is not a vessel to be filled but a fire to be ignited.” – Plutarch
# “Don’t let what you cannot do interfere with what you can do.” — John Wooden
# “A person who never made a mistake never tried anything new.” — Albert Einstein
# “Try not to become a man of success. Rather become a man of value.” —Albert Einstein
# “Excellence is not a skill. It is an attitude.” —Ralph Marston
# “Go into the world and do well. But more importantly, go into the world and do good.” —Minor Myers Jur
# “Rule no.1 is: Don’t sweat the small stuff. Rule no. 2 is:  It’s all small stuff.” —Robert Eliot
# “Quality is not an act, it is a habit.” —Aristotle
# “I think it’s possible for ordinary people to choose to be extraordinary.” — Elon Musk
# “The best way to predict your future is to create it.” —Abraham Lincoln
# “The future belongs to those who believe in the beauty of their dreams.” ― Eleanor Roosevelt
# “Just believe in yourself. Even if you don’t pretend that you do and, at some point, you will.” —Venus Williams
# Do the best you can until you know better. Then when you know better, do better.” —Maya Angelou
# “Doubt kills more dreams than failure ever will.” —Karim Seddiki
# “You are braver than you believe, stronger than you seem and smarter than you think.” — A.A Milne
# “Go confidently in the direction of your dreams. Live the life you have imagined.” —Henry David Thoreau
# “Learn from yesterday. Live for today. Hope for tomorrow.” – Albert Einstein
# “The more that you read, the more things you will know, the more that you learn, the more places you’ll go.” — Dr. Seuss
# “Today a reader. Tomorrow a leader.” – Anonymous
# “In a world where you can be anything, be kind.” — Jennifer Dukes Lee
# He who asks a question is a fool for five minutes; he who does not ask a question remains a fool forever.” — Chinese Proverb
# “It took me fifteen years to discover I had no talent for writing, but I couldn’t give it up because by then I was too famous.” —Robert Benchley
# How wonderful it is that nobody need wait a single moment before starting to improve the world. – Anne Frank
# “I don’t love studying. I hate studying. I like learning. Learning is beautiful.” – Natalie Portman
# “If you work hard enough and assert yourself, and use your mind and imagination, you can shape the world to your desires.” – Malcolm Gladwell
# Work gives you meaning and purpose and life is empty without it. – Stephen Hawking
# You can’t have a better tomorrow if you’re still thinking about yesterday. – Charles F. Kettering
# The whole purpose of education is to turn mirrors into windows. – Sydney J. Harris
# The purpose of our lives is to be happy. – Dalai Lama
# When you dance, your purpose is not to get to a certain place on the floor. It’s to enjoy each step along the way. – Wayne Dyer
# “When one door closes, another opens; but we often look so long and so regretfully upon the closed door that we do not see the one which has opened for us.” —Alexander Graham Bell
# “Education is the most powerful weapon, which you can use to change the world.” —Nelson Mandela
# It always seems impossible until it’s done — Nelson Mandela
# Study the past if you want to intuit the future – Confucius
# You can always be better – Tiger Woods
# “There are far, far better things ahead than any we leave behind.”– C.S. Lewis
# “Hardships often prepare ordinary people for an extraordinary destiny.” —C.S. Lewis
# A dream you dream alone is only a dream. A dream you dream together is reality.” —Yoko Ono
# There is no secret to success. It is the result of preparation, hard work, and learning from failure. – General Colin Powell
# Striving for success without hard work is like trying to harvest where you haven’t planted. – David Bly
# There is no elevator to success. You have to take the stairs. – Zig Ziglar
# It is well to remind ourselves that anxiety signifies a conflict, and so long as a conflict is going on, a constructive solution is possible. – Rollo May
# A successful man is one who can lay a firm foundation with the bricks others have thrown at him. – David Brinkley
# “If you hear a voice within you say ‘you cannot paint,’ then by all means paint, and the voice will be silenced.” —Vincent Van Gogh
# “Great things are done by a series of small things brought together.” —Vincent van Gogh
# “You get the best out of others when you give the best of yourself.” —Harvey S. Firestone
# “The problem is not the problem. The problem is your attitude about the problem. Do you understand?” —Captain Jack Sparrow
# “All our dreams can come true if we have the courage to pursue them.” —Walt Disney
# “There are no shortcuts to any place worth going.” — Beverly Stills
# “I find that the harder I work, the more luck I seem to have.” – Thomas Jefferson
# “Genius is 10% inspiration, 90% perspiration.” — Thomas Edison
# “Motivation is what gets you started. Habit is what keeps you going.” – Jim Ryun
# “Success is the sum of small efforts, repeated.” — R Collier
# “It will not happen cutting corners, taking shortcuts or looking for the easy way! There’s only hard work, late nights, early mornings, practice, repetition, study and discipline.” —nimo_wehearit
# Most of the important things in the world have been accomplished by people who have kept on trying when there seemed to be no help at all. – Dale Carnegie
# You can’t use up creativity. The more you use, the more you have. – Maya Angelou
# “If you don’t build your dreams, someone will hire you to help build theirs.” —Tony Gaskin
# “If opportunity doesn’t knock, build a door.” —Milton Berle
# When your dreams becoming reality, they’re no longer your dreams.” —Hugh Jackman
# “To accomplish great things, we must not only act, but also dream, not only plan, but also believe.” —Anatole France
# “Do not make your goal to be the best. Best is a label. It’s something someone else decides for you. ‘Better’ is more personal.” —Baryshnikov
# If people do not believe that mathematics is simple, it’s only because they do not realize how complicated life is.” —John Von Neumann
# “None of us is as smart as all of us.” — Ken Blanchard
# “Talent is cheaper than table salt. What separates the talented individual from the successful one is a lot of hard work.” – Stephen King, author.
# “An investment in knowledge pays the best interest.”- Benjamin Franklin
# When you get to the end of the rope, tie a knot and hang on. – Franklin D. Roosevelt
# “Follow your passion. It will lead you to your purpose.” —Oprah
# “Turning your passion into your job is easier than finding a job that matches your passion.” —Seth Godin
# “The most successful people are those who are good at plan B.” —James Yorke
# The road to success is always under construction.” —Lily Tomlin
# The price of success is hard work, dedication to the job at hand, and the determination that whether we win or lose, we have applied the best of ourselves to the task at hand.” —Vince Lombardi
# Self-belief and hard work will always earn you success. – Virat Kohli
# Through hard work, perseverance and a faith in God, you can live your dreams. – Ben Carson
# The only place where success comes before work is in the dictionary. – Vidal Sassoon
# There are no traffic jams on the extra mile. – Zig Ziglar
# There are no shortcuts to any place worth going. – Beverly Sills
# “Every accomplishment starts with the decision to try.” —Gail Devers
# Keep your dreams alive. Understand to achieve anything requires faith and belief in yourself, vision, hard work, determination, and dedication. Remember all things are possible for those who believe. – Gail Devers
# “Procrastination makes easy things hard and hard things harder.” — Mason Cooley
# “The capacity to learn is a gift; the ability to learn is a skill; the willingness to learn is a choice.” – Brian Herbert
# Procrastination is the art of keeping up with yesterday. – Don Marquis
# So many of our dreams at first seem impossible, then they seem improbable, and then, when we summon the will, they soon become inevitable. – Christopher Reeve
# Procrastination is like a credit card: it’s a lot of fun until you get the bill. – Christopher Parker
# Procrastination is opportunity’s assassin. – Victor Kiam
# My biggest regret could be summed up in one word, and that’s procrastination. – Ron Cooper
# Procrastination is the thief of time. – Edward Young
# Ninety-nine percent of the failures come from people who have the habit of making excuses. – George Washington Carver
# It had long since come to my attention that people of accomplishment rarely sat back and let things happen to them. They went out and happened to things.” —Leonardo da Vinci
# The real man is one who always finds excuses for others, but never excuses himself. – Henry Ward Beecher
# “You don’t have to be great to start, but you have to start to be great.” – Zig Ziglar
# “The expert in anything was once a beginner — Helen Hayes.”
# “The way to get started is to quit talking and begin doing.” – Walt Disney
# “You have to be odd to be no.1.” — Dr. Seuss
# “You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose.” —Dr. Seuss
# “Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.” – Pelé
# “I do not know anyone who has got to the top without hard work. That is the recipe. It will not always get you to the top, but it should get you pretty near.” – Margaret Thatcher, former British Prime Minister.
# “Learning is the only thing the mind never exhausts, never fears, and never regrets.” – Leonardo da Vinci
# “Study hard, no matter if it seems impossible, no matter if it takes time, no matter if you have to be up all night, just remember that the feeling of success is the best thing in the entire world.” —khangal_wehearit
# “If people knew how hard I worked to achieve my mastery, it wouldn’t seem so wonderful after all.”– Michelangelo
# The man who moves a mountain begins by carrying away small stones.” —Confucius
# “It’s the pain and failure that teaches you the best lesson in life and motivates you to rebuild yourself and stand again with a robust faith.” —Priti Chaubey
# “Don’t limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve.” —Mary Kay Ash
# Use all your efforts, even when the possibilities play against you – Arnold Palmer
# Set tough goals and do not stop until you get there – Bo Jackso
# The man well prepared for the struggle has achieved half a triumph – Miguel de Cervantes
# “You’ve got to get up every morning with determination if you’re going to go to bed with satisfaction.” – George Lorimer
# “You’ve got to get up every morning with determination if you’re going to go to bed with satisfaction.” – George Lorimer
# “In life you make the small decisions with your head and the big decisions with your heart.” —Omid Kordgstani
# “Worry gives a small thing a big shadow.” —Swedish Proverb
# “I learned many great lessons from my father, not the least of which was that you can fail at what you don’t want, so you might as well take a chance on doing what you love.” —Jim Carrey
# “Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will spend its whole life believing that it is stupid.” – Albert Einstein
# “My advice is, never do tomorrow what you can do today. Procrastination is the thief of time.” – Charles Dickens ‘David Copperfield’
# “Help will always be given at Hogwarts to those who ask.” – Albus Dumbledore ‘Harry Potter and the Chamber of Secrets’
# “Happiness can be found even in the darkest of times if one only remembers to turn on the light.” —Albus Dumbledore
# Working hard is important, but there is something that matters even more: Believing in yourself.” —Harry Potter
# “Trust yourself, you know more than you think you do” – Benjamin Spock
# “Life itself is your teacher, and you are in a state of constant learning.” —Bruce Lee
# “Challenges are what make life interesting. Overcoming them is what makes life meaningful.” – Joshua J. Marine
# “Your time is limited, don’t waste it living someone else’s life. Don’t be trapped by dogma, which is living the result of other people’s thinking. Don’t let the noise of other’s opinion drowned your own inner voice. And most important, have the courage to follow your heart and intuition, they somehow already know what you truly want to become. Everything else is secondary.”– Steve Jobs
# Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs
# “Education is not to reform students or amuse them or to make them expert technicians. It is to unsettle their minds, widen their horizons, inflame their intellects, teach them to think straight, if possible.” —Robert M. Hutchins
# “If you don’t go after what you want, you’ll never have it. If you don’t ask, the answer is always no. If you don’t step forward, you’re always in the same place.”– Nora Roberts
# “The man who does not read books has no advantage over the one who cannot read them.” — Mark Twain
# “Education is the passport to the future, for tomorrow belongs to those who prepare for it today.” — Malcolm X
# “The beautiful thing about learning is that no one can take it away from you.” —B.B. King
# “Education is the most powerful weapon you can use to change the world.” — BB King
# “That which we persist in doing becomes easier for us to do; not that the nature of the thing itself is changed, but that our power to do is increased.” – Ralph Waldo Emerson
# “What lies behind us and what lies before us are tiny matters compared to what lies within us.” —Ralph Waldo Emerson
# “Winners embrace hard work. They love the discipline of it, the trade-off they’re making to win. Losers, on the other hand, see it as punishment. And that’s the difference.”– Lou Holtz
# “I follow three rules: Do the right thing, do the best you can, and always show people you care.” —Lou Holtz
# “Successful people begin where failures leave off. Never settle for ‘just getting the job done.’ Excel!” – Tom Hopkins
# “Live as if you were to die tomorrow. Learn as if you were to live forever.” – Mahatma Gandhi
# “The dictionary is the only place that success comes before work. Work is the key to success, and hard work can help you accomplish anything.” – Vince Lombardi
# The day you take complete responsibility for yourself, the day you stop making any excuses, that’s the day you start to the top. – O.J. Simpson
# It’s not the time to look for excuses. – Rafael Nadal
# Don’t say you don’t have enough time. You have exactly the same number of hours per day that were given to Helen Keller, Pasteur, Michelangelo, Mother Teresea, Leonardo da Vinci, Thomas Jefferson, and Albert Einstein. – H. Jackson Brown Jr.
# However difficult life may seem, there is always something you can do and succeed at. – Stephen Hawking
# It is not the mountain we conquer, but ourselves. – Edmund Hillary
# “Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence.” —Helen Keller
# “A positive attitude may not solve all your problems, but it will annoy enough people to make it worth the effort.” —Herm Albright
# “Shoot for the moon. Even if you miss you’ll land among the stars.” —Les Brown
# Start where you are. Use what you have. Do what you can. – Arthur Ashe
# There are two kinds of people in this world: those who want to get things done and those who don’t want to make mistakes. – John Maxwell
# Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.” —Albert Schweitzer
# The difference between ordinary and extraordinary is that little extra.” —Jimmy Johnson
# “Imagination… is the elixir of life, the seed of greatness.” —Melowpark College
# “Productivity is never an accident. It is always the result of a commitment to excellence, intelligent planning, and focused effort,” —Paul J. Meyer
# Efforts and courage are not enough without purpose and direction. – John F. Kennedy
# “College is the best time of your life. When else are your parents going to spend several thousand dollars a year just for you to go to a strange town and get drunk every night?” —David Wood
# Seventy percent of success in life is showing up. – Woody Allen
# “You are capable of more than you know. Choose a goal that seems right for you and strive to be the best, however hard the path. Aim high. Behave honorably. Prepare to be alone at times, and to endure failure. Persist! The world needs all you can give.” —E.O. Wilson
# I’ve failed over and over and over again in my life. And that is why I succeed. – Michael Jordan
# “Learning is never done without errors and defeat.” – Vladimir Lenin
# “Follow your fear.” —Tina Fey
# “Instead of freaking out about these constraints, embrace them. Let them guide you.” —37 Signals
# Instead of looking at the hundred reasons to quit, look at the thousand reasons not to give up.” —Kushanowizoom
# “Never let the fear of striking out stop you from playing the game.” — Babe Ruth
# “The greatest pleasure in life is doing what people say you cannot do.” —Walter Bagehot
# Our greatest fear should not be of failure, but of succeeding at things in life that don’t really matter. – Francis Chan
# Your positive action combined with positive thinking results in success. – Shiv Khera
# Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill
# Don’t wish it were easier; wish you were better. – Jim Rohn
# The secret of success is to do the common things uncommonly well. – John D. Rockefeller
# Successful and unsuccessful people do not vary greatly in their abilities. They vary in their desires to reach their potential. – John Maxwell
# Perseverance is the hard work you do after you get tired of doing the hard work you already did. – Newt Gingrich
# There is no substitute for hard work. – Thomas Edison
# If you’re going through hell, keep going. – Winston Churchill
# Failure is the opportunity to begin again more intelligently. – Henry Ford
# You don’t drown by falling in the water; you drown by staying there. – Ed Cole
# “Believe deep down in your heart that you’re destined to do great things.” —Joe Paterno
# I don’t measure a man’s success by how high he climbs, but how high he bounces when he hits the bottom. – George S. Patton
# Patience and perseverance have a magical effect before which difficulties disappear and obstacles vanish. – John Quincy Adams
# “You never really learn much from hearing yourself speak.” —George Clooney
# By perseverance, the snail reached the ark. – Charles Spurgeon
# “Your biggest risk isn’t failing, it’s getting too comfortable.” —Drew Houston
# Follow your dreams, believe in yourself and don’t give up. – Rachel Corrie
# Believe in yourself, take on your challenges, dig deep within yourself to conquer fears. Never let anyone bring you down. You got to keep going. – Chantal Sutherland
# To excel at the highest level – or any level, really – you need to believe in yourself, and hands down, one of the biggest contributors to my self-confidence has been private coaching. – Stephen Curry
# The purpose of human life is to serve and to show compassion and the will to help others. – Albert Schweitzer
# Perseverance is failing 19 times and succeeding the 20th. – Julie Andrews
# Real difficulties can be overcome; it is only the imaginary ones that are unconquerable. – Theodore N. Vail
# There are those who work all day. Those who dream all day. And those who spend an hour dreaming before setting to work to fulfill those dreams. Go into the third category because there’s virtually no competition. – Steven J. Ross
# Little minds are tamed and subdued by misfortune; but great minds rise above it. – Washington Irving
# All progress takes place outside of your comfort zone. – Michael John Bobak
# “Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.” — Christian D. Larson
# “Teachers can open the door, but you must enter it yourself.” — Chinese proverb
# “When the student is ready, the master appears.” —Buddhist Proverb
# If you have to put someone on a pedestal, put teachers. They are society’s heroes.” —Guy Kawasaki
# Without studying the soul sick – Seneca
# The man who is a teacher of patience is a master of everything else – George Saville
# A book is like a garden that can be carried in your pocket  – Chinese Proverb
# If we did all the things we are capable of, we would be amazed – Thomas Edison
# Quality is never an accident, it is always the result of an effort of intelligence – John Ruskin
# Change your thoughts and you will change your world – Norman Vincent Peale
# Your talents and abilities will improve over time, but for that you have to start – Martin Luther King
# True education is about getting the best out of oneself – Mahatma Gandhi
# Books are dangerous. The best ones should be labeled with “This could change your life” – Helen Exley
# Courage doesn’t always roar. Sometimes courage is the quiet voice at the end of the day saying ‘I will try again tomorrow’. – Mary Anne Radmacher
# Youth is the time to study wisdom; the old age, that of practicing it – Jean Jacques Rousseau
# If you do not go to the end, why start? – Joe Namath
# Learning without thinking is useless. Think without learning, dangerous – Confucius
# “Kindness is the language which the deaf can hear and the blind can see.” —Mark Twain
#############################################################################

# quotes2.txt contents ######################################################
# 1
# 0
# 1
# 1
# 1
# 1
# 0
# 1
# 1
# 0
# 0
# 0
# 0
# 0
# 0
# 1
# 1
# 0
# 1
# 1
# 0
# 1
# 1
# 0
# 0
# 1
# 1
# 1
# 1
# 1
# 0
# 1
# 0
# 0
# 0
# 0
# 1
# 0
# 0
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 1
# 0
# 1
# 1
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 0
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 1
# 1
# 0
# 1
# 1
# 1
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 0
# 1
# 1
# 1
# 1
# 0
# 0
# 1
# 0
# 1
# 1
# 1
# 0
#############################################################################
