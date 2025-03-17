import random

def main():
    """Generate and print multiple sentences."""
    for _ in range(5):  # Generate 5 sentences
        print(make_sentence())

def make_sentence():
    """Construct a sentence with determiner, noun, verb, and prepositional phrase."""
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    prepositional_phrase = get_prepositional_phrase()
    
    return f"{determiner} {noun} {verb} {prepositional_phrase}."

def get_determiner():
    """Return a randomly chosen determiner."""
    determiners = ["A", "The", "One", "Some"]
    return random.choice(determiners)

def get_noun():
    """Return a randomly chosen noun."""
    nouns = ["child", "girl", "boy", "dog", "cat", "rabbit", "bird", "car", "tree"]
    return random.choice(nouns)

def get_verb():
    """Return a randomly chosen verb."""
    verbs = ["runs", "jumps", "talks", "drinks", "laughs", "sleeps", "sings", "will run", "will talk"]
    return random.choice(verbs)

def get_preposition():
    """Return a randomly chosen preposition."""
    prepositions = ["above", "on", "below", "beside", "with", "for", "about"]
    return random.choice(prepositions)

def get_prepositional_phrase():
    """Construct and return a prepositional phrase."""
    preposition = get_preposition()
    determiner = get_determiner().lower()  # Convert to lowercase for proper grammar
    noun = get_noun()
    return f"{preposition} {determiner} {noun}"

# Run the program
if __name__ == "__main__":
    main()

