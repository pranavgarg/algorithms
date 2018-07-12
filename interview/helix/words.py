
from vowel import Vowel, Consonant, NonAlphabet

class WordFactory():
    def make(self, word):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        if word[0] in vowels:
            return Vowel(word)
        elif (ord(word[0]) >= 65 and ord(word[0]) <=90) or (ord(word[0]) >= 97 and ord(word[0]) <=122):
            return Consonant(word)
        else:
            return NonAlphabet(word)



c = Consonant('Hello')
assert c.process() == "Ellohay" #adding ay at the end


class Sentence:
    def __init__(self, s):
        self.sentence = s

    def parser(self):
        out_words = []
        words = self.sentence.split(' ')
        for word in words:
            out_words.append(WordFactory().make(word))

        return ' '.join([word.process() for word in out_words])


transform_s = Sentence("Hello world")
print transform_s.parser()