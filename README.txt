First of all, thanks for looking into my blackjack project.

19/10/2020.
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