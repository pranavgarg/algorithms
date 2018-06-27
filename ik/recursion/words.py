class Vowel:
    def __init__(self, word):
        self.word = word
        self.word = self.word+"way"


    def __repr__(self):
        return self.word

v = Vowel("apple")
assert  v.word == "appleway"


class Consonant:

    def __init__(self, word):
        self.chars = list(word)   #aeb -> ['a','e','b']
        # string capitalization
        self.is_capitalized = self.chars[0].isupper()
        self.rotate()
        self.vowels = {'a', 'e', 'i', 'o', 'u'}

    def rotate(self):
        temp = self.chars[1:]
        if self.is_capitalized:
            self.chars[0] = self.chars[0].lower()
        temp.append(self.chars[0])
        self.chars = temp

    def translate(self):
        if self.is_capitalized:
            #capitalize it
            if len(self.chars) > 0:
                self.chars[0] = self.chars[0].upper()  #capitalization
        return ''.join(self.chars)+"ay"

c = Consonant('Hello')
assert c.translate() == "Ellohay" #adding ay at the end


class Sentence:
    def __init__(self, s):
        self.sentence = s
        self.words = s.split(' ')
        self.output_words = []

    def is_vowel(self, word):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return word[0].lower() in vowels

    def parser(self):
        for word in self.words:
            if self.is_vowel(word):
                self.output_words.append(Vowel(word).translate())
            elif self.is_consonant(word):
                self.output_words.append(Consonant(word).translate())
            else:
                self.output_words.append(word)
        return ' '.join(self.output_words)

s = raw_input("enter your sentence")
transform_s = Sentence(s)
assert transform_s.parser() == ""