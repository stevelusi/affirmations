import random


affirmations = ["You are enough",
                "You are deeply loved by GOD",
                "You are doing your best and that is okay", 
                "Everyday is a fresh start",
                "You can do all things through Christ who strangthens you",
                "I appreciate you",
                "You are fearfully and wonderfully made (Ps. 139:14)",
                "I am proud of you",
                "I feel safe with you"]

def get_random_affirmations():
    return random.choice(affirmations)
