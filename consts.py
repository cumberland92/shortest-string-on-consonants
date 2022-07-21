def removeVowels(s):
      s = s.replace("a","")
      s = s.replace("e","")
      s = s.replace("i","")
      s = s.replace("o","")
      s = s.replace("u","")
      return s

def loadDictionary():
    dictionaryFile = open('D:/triangle graph game/dictionary.txt')

    englishWords = {}

    dicList= dictionaryFile.readlines()
    for i in range(len(dicList)):
        dicList[i] = dicList[i].replace("\n", "")
    for word in dicList:
        print("Before removing, word={}".format(word))
        word=removeVowels(word)
        print("after removing, word={}".format(word))
    #     length = len(word)
    #     if(length==0):
    #         continue
    #     if(length in englishWords.keys()):
    #         englishWords[length].append(word)
    #     else:
    #         englishWords.update({length: [word]})
    # dictionaryFile.close()
    return englishWords



ENGLISH_WORDS = loadDictionary()
print(ENGLISH_WORDS)
# for i in sorted(ENGLISH_WORDS.keys()):
#     seen = set()
#     containsDuplicates = False
#     for j in range(len(ENGLISH_WORDS[i])):
#         if ENGLISH_WORDS[i][j] in seen:
#             containsDuplicates = True
#             print("{} does not work because of {}".format(i, ENGLISH_WORDS[i][j]))
#             break
#         if(j==len(ENGLISH_WORDS[i])-1):
#             print("The smallest number of consonants is {}".format(i))
#             quit()
