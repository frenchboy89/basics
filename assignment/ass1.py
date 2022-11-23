sentence = "Try to remove any o in this sentence using a for loop and print out the outcome"
for word in sentence:
    if word == "o":
        continue
    else:
        print(word)

"""
You want to count the characters in all these titles
and print the results one by one to your screen, in this format:

    "The title [movie_title] is [X] characters long."
"""

movies = ['dragonfly', 'planet of the apes', 'die young', 'prison break', 'I hate you',
          'the hate you give', "Enola Holmes", "The Mechanic"]

for title in movies:
    movie_length = len(title)
    
    if "the" in title:
        continue
    else:
        print(f"The Title {title} is {movie_length} characters long")



                             





