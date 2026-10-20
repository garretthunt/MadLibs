#There was merchant named {name} who lived in a small town. He was very {adjective_one} and did a lot of {verb1}. He heard a legend of a {adjective_two} princess who was taken by an {main_evil_animal} and held captive in a castle and that whoever saved the princess gained millions of {objects}. He decided to embark on his {time} long journey and save the priness. On his journey, he encountered many strange creatures and traversed through {adjective_three} terrain. During his quest, he came in contact with a very {adjective_4} {minor_animal_foe}. In order to continue to the priness, he had to fight this animal. He {adverb_one} {verb_two} at the animal and finally defeted it, claiming it's {noun_one} as a token of his victory. He finally made it to the castle, but had to find a way to get over the {number_one} foot tall wall. Once he made it in the castle, he needed to climb up {number_two} flights of stairs and complete {number_three} challenges. One challenge even involved needing to {verb_three} across the entire floor of the castle. He had then come face to face with the {main_evil_animal} holding the princess captive. The princess screamed {princess_scream_word} in distress. The merchant took out his {weapon} and readied it for battle. He began fighing the {main_evil_animal} and contunined to do so for {time_two}. After much struggle and even more determination, the {adjective_one} merchant finally slayed the {main_evil_animal} and saved the princess. As a thank you, she gave him the promised reward. Finally finished with his quest, he started to head home. Sadly, he was unable to use his rewards, for he was offed by a {stupid_animal} on his way back home. The end.



import time 

print("Welcome to MadLibs")
time.sleep(2)
print("Please enter the following blanks")
time.sleep(2)
name = input("Enter a name: ")
adjective_one = input("Enter an adjective for the merchant: ")
verb_one = input("Enter a verb to descirbe what the prince does a lot of (ending in ing): ")
adjective_two = input("Enter an adjective for the princess: ")
main_evil_animal= input("Enter an animal that took the princess: ")
objects = input("Enter an insentive that the merchant gets millions of: ")
time_one = input("Enter an amount of time (number, units): ")
adjective_three = input("Enter an adjective to descibe the terrain the merchant travered: ")
minor_animal_foe = input("Enter a animal foe found on the jorney: ")
adjective_four = input("Enter an adjective descibing the minor animal foe on the journey: ")
verb_two = input("Enter a verb to describe what merchant did to the animal (ending in ed and followed by at): ")
adverb_one = input("Enter an adverb to descibe what the merchant did to the animal foe: ")
noun_one = input("Enter a noun claimed from the animal foe as a trophy of the merchant's victory: ")
number_one = input("Enter a number to describe how mant feet tall the castle wall is: ")
number_two = input("Enter a number to decribe how many flights of stairs the merhcant when up: ")
number_three = input("Enter a number to explain how many challenges the merchant had to complete: ")
verb_three = input("Enter a verb describing what the merchant did to traverse the floor of the castle: ")
princess_scream_word = input("Enter a word the princess screamed in fright: ")
weapon = input("Enter a weapon that the merchant could use: ")
time_two = input("How long did the merchant battle against the villian holding the princes captive (number, units)?: ") 
stupid_animal = input("Enter an animal that ended up being the merchants demise: ")

print("Here is your finsihed MadLib story:")
time.sleep(1)
for i in range(3,0,-1):
    print(i)
    time.sleep(1)

print(f"There was merchant named {name} who lived in a small town. He was very {adjective_one} and did a lot of {verb_one}. He heard a legend of a {adjective_two} princess who was taken by a(n) {main_evil_animal} and held captive in a castle and that whoever saved the princess would gain millions of {objects}. He decided to embark on his {time_one} long journey and save the priness. On his journey, he encountered many strange creatures and traversed through {adjective_three} terrain. During his quest, he came in contact with a very {adjective_four} {minor_animal_foe}. In order to continue to the priness, he had to fight this animal. He {adverb_one} {verb_two} at the animal and finally defeted it, claiming it's {noun_one} as a token of his victory. He finally made it to the castle, but had to find a way to get over the {number_one} foot tall wall. Once he made it in the castle, he needed to climb up {number_two} flights of stairs and complete {number_three} challenges. One challenge even involved needing to {verb_three} across the entire floor of the castle. He had then come face to face with the {main_evil_animal} holding the princess captive. The princess screamed {princess_scream_word} in distress. The merchant took out his {weapon} and readied it for battle. He began fighing the {main_evil_animal} and contunined to do so for {time_two}. After much struggle and even more determination, the {adjective_one} merchant finally slayed the {main_evil_animal} and saved the princess. As a thank you, she gave him the promised reward. Finally finished with his quest, he started to head home. Sadly, he was unable to use his rewards, for he was offed by a {stupid_animal} on his way back home. The end.")