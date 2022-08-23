#string concatenation (aka how to put strings together)
# freeCodeCamp tutorial 
#suppose we want to create a string that says "subscribe to ________"
# youtuber = "Likhaya A. Faku " # some string variable

# # a few ways to do this 
# print("subscribe to " +youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

# from sample_madlibs import hp, code, zombie, hungergames
# import random 
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")
madlib = f"Computer program is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

# if _name_ == "_main_":
#     m = random.choice([hp, code, zombie, hungergames])
#     m.madlib()