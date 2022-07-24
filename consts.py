def removeVowels(s):
      s = s.replace("A","")
      s = s.replace("E","")
      s = s.replace("I","")
      s = s.replace("O","")
      s = s.replace("U","")
      return s

def loadDictionary():
    dictionaryFile = open('D:/triangle graph game/dictionary.txt')

    englishWords = {}

    dicList= dictionaryFile.readlines()
    for i in range(len(dicList)):
        dicList[i] = dicList[i].replace("\n", "")
    for word in dicList:
        word=removeVowels(word)
        length = len(word)
        if(length==0):
            continue
        if(length in englishWords.keys()):
            englishWords[length].append(word)
        else:
            englishWords.update({length: [word]})
    dictionaryFile.close()
    return englishWords



ENGLISH_WORDS = loadDictionary()
print(ENGLISH_WORDS)
for i in sorted(ENGLISH_WORDS.keys()):
    seen = set()
    for j in range(len(ENGLISH_WORDS[i])):
        if ENGLISH_WORDS[i][j] in seen:
            print("{} does not work because of {}".format(i, ENGLISH_WORDS[i][j]))
            break
        if(j==len(ENGLISH_WORDS[i])-1):
            print("The smallest number of consonants is {}".format(i))
            quit()
        seen.add(ENGLISH_WORDS[i][j])
