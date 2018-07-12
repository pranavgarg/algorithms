from abc import ABCMeta, abstractmethod

class Word:
    __metaclass__ = ABCMeta
    def __init__(self, word):
        self.word = word
        self.vowels = {'a', 'e', 'i', 'o', 'u'}

    @abstractmethod
    def process(self):
        pass

class Vowel(Word):
    def __init__(self, word):
        super(Consonant, self).__init__(word)
        self.word = self.word+"way"

    def process(self):
        return self.word


class Consonant(Word):

    def __init__(self, word):
        super(Consonant, self).__init__(word)
        # string capitalization
        self.is_capitalized = self.word[0].isupper()
        self.rotate()

    def rotate(self):
        for idx, c in enumerate(self.word):
            if c not in self.vowels:
                continue
            else:
                break
        temp = self.word[idx:]+self.word[:idx]
        self.word = temp

    def process(self):
        word = self.word.lower()
        if self.is_capitalized:
            word = word.capitalize()
        return word + 'ay'

class NonAlphabet(Word):
    def __init(self, word):
        super(NonAlphabet, self).__init__(word)

    def process(self):
        return self.word