def valid_words(words, map):
    matches = []
    for word in words:
        ismatch = True
        for c in word:
            if c not in map:
                ismatch = False
                break
        if ismatch:
            matches.append(word)
    return matches

print valid_words(["go","bat","me","eat","goal",
                                "boy", "run"],{'e','o','b', 'a','m','g', 'l'})

print valid_words(["abacus","deltoid", "gaff", "giraffe","microphone"],{"a","e","f","f","g","i","r","q"})