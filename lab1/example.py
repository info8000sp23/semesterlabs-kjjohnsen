import pronouncing

def find_rhyme(word):
    rhymes = pronouncing.rhymes(word)
    if len(rhymes) > 0:
        return rhymes[0]
    else:
        return "No rhyme found."

word = input("Enter a word: ")
word = find_rhyme(word)
print("Rhyme: ", word)
word = find_rhyme(word)
print("Rhyme: ", word)
word = find_rhyme(word)
print("Rhyme: ", word)