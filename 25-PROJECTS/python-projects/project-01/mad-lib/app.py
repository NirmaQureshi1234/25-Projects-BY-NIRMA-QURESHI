def mad_libs():
    
    story = """
    Today I went to the ___ADJECTIVE___ zoo. I saw a ___ADJECTIVE___ monkey, a ___NOUN___, and a huge ___ANIMAL___.
    The ___ANIMAL___ was very ___ADJECTIVE___ and was eating a ___NOUN___. I also saw a ___ADJECTIVE___ ___NOUN___ that
    looked very ___ADJECTIVE___! It was a ___ADJECTIVE___ day at the zoo!
    """
    
    
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    animal = input("Enter an animal: ")
    adjective3 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    adjective4 = input("Enter another adjective: ")
    noun3 = input("Enter another noun: ")
    adjective5 = input("Enter another adjective: ")
    
    
    story = story.replace("___ADJECTIVE___", adjective1, 1)
    story = story.replace("___ADJECTIVE___", adjective2, 1)
    story = story.replace("___NOUN___", noun1, 1)
    story = story.replace("___ANIMAL___", animal, 1)
    story = story.replace("___ADJECTIVE___", adjective3, 1)
    story = story.replace("___NOUN___", noun2, 1)
    story = story.replace("___ADJECTIVE___", adjective4, 1)
    story = story.replace("___NOUN___", noun3, 1)
    story = story.replace("___ADJECTIVE___", adjective5, 1)
    
    print("\nHere is your Mad Libs story:")
    print(story)


mad_libs()
