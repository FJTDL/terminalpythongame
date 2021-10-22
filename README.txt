First of all, thanks for looking into my blackjack project.

19/10/2021.
Started the project. First I set up a kanban board on Trello.com and added
the cards representing the different components I knew I'd need.

Then, started working on the RNG aspect. Imported the random module for the
choices and radint functions. I created ten lists comprising of each and every
card in the deck. A dictionary was then created where the value of each card 
served as they key and then using the random.choices() function it randomly
selects one and the removes it from the list (deck).

Upon reflection, I believe that I have over engineered this aspect and it would
be far easier if I created either a cards class and then create a list of all
cards and then randomly generate then pop them one at a time, or I could create
a single dictionary where every card is a key and they have their value initialised
there and once called they are removed.

20/10/2021.
Today saw a major overhaul to the current RNG system. My reflections from yesterday
led me to redevelop the system in favour of a more eloquent dictionary based system
similar to the one already in use, but by reversing key and value pairs and removing
the lists all together. The new system does not yet have the ability to remove values
from the dictionary once they have been called, but that is the plan for the next
stage in the developement of the application. Once this aspect is completed then the
RNG is done and another card can be added to the done column of the kanban board hosted
on Trello.com.

The major issue today came from the assignment of ace values. In blackjack, aces can be
either 11 or 2 depending on the players choice, so the value of any of the aces was indeffinite.
To combat this, I created a function that was used as the value of the aces. However, as
it turned out this proved to be a major flaw in the design of the program, as whenever the 
script ran the result was that the value of each ace was trying to be initialised whenever
it was run and this meant that when an ace actually appeared it got stuck in an infinite
loop where it never accepted a value. To combat this, aces have a value of None and a
seperate statement now checks if the generated card is in a list of the aces. If it is,
then it calls the function to determine the value of the card.

Furthermore, all runnings of the program currently return both the value of the card and
which card it was. This was done to add another layer of normalcy to the game.

21/10/2021.
Added the players as their own objects. Their class is not complex, but it did not need to be
and I chose to make them unique classes as it was just easier for me, as it leaves the coding
to be easier and I can store numerous attributes, functions and variables in the objects, even
unique aspects for each player if necessary. I moved more code into functions as well, such as
the random card generator (RCG) which means I can now call it as need be insetad of it running
weirdly as it has done previously.

That's it for today, the project is progressing well and to schedule.

22/10/2021.
Today, I finished the project. A lot changed and only two commits were made so a lot of potentially
important versions arenow lost, but the final product works as intended. It's not my best work, but
it is the most complex program I have ever written. I have never used classes or dictionaries prior
and have mostly made simple calculators, chatbots or quizzes. None have used advanced features before
so this project was my first exposure. I'm please and satisified with the outcome with my only qualm
being that that I had to completely overhaul how drawing cards worked due to a number of bugs, with the
final product having four seperate functions that are not called all that much. All of the code is not as
DRY as it could be, nor is it as compact either. However, for a first serious attempt using advanced
features, I am proud of my work and look forward to more opportunities to learn and grow with excitement.

If you have read this file and taken an interest in my project, thank you for your time and consideration in supporting a 17 year old guy  Auckland New Zealand in his efforts to grow as an effective programmer.

22/10/2021
I FOUND A BUG WITH WHEN YOU SCORE 21 POINTS AND I FIXED.
