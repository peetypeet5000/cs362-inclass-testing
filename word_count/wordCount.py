def wordCount(word):
    i = 0

    #ensures 1 word is counted
    if(len(word) > 0):
        i = 1

    #for each space, another word
    for ele in word:
        if ele == " ":
            i = i + 1

    return i