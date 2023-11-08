def mysplit(strng):
    strng = strng.strip()
    if strng == '':
        return []
    else:
        words = []
        word = ''
        for i in range(len(strng)):
            if strng[i] != ' ':
                word += strng[i]
            else:
                words.append(word)
                word = ''
        words.append(word)
        return words
    
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit(""))
print(mysplit("abc"))
print(mysplit("   "))