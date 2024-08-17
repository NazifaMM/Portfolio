# Adding or removing prefix/suffixes.

# Define adding prefixed to a word
def add_prefix_un(word):
    return "un" + word

# Define how to word groups
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    return prefix + " :: " + " :: ".join(prefixed_words)

#Define how to remove suffixes
def remove_suffix_ness(word):
    if word.endswith("ness"):
        root_word = word[:-4]
        if root_word.endswith("i"):
            root_word += "y"
        return root_word
    return word

# Define how to adjective a verb 
def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index]
    if adjective.endswith('.'):
        adjective = adjective[:-1]
    return adjective + "en"

# Test the functions using examples 
print(add_prefix_un("happy"))  
print(add_prefix_un("manageable")) 

print(make_word_groups(['en', 'close', 'joy', 'lighten']))  
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))  
print(make_word_groups(['auto', 'didactic', 'graph', 'mate'])) 
print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))  

print(remove_suffix_ness("heaviness"))  
print(remove_suffix_ness("sadness"))  

print(adjective_to_verb('I need to make that bright.', -1))  
print(adjective_to_verb('It got dark as the sun set.', 2))  
