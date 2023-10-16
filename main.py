def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

phrase1 = "Listen"
phrase2 = "Silent"

if is_anagram(phrase1, phrase2):
    print(f'"{phrase1}" и "{phrase2}" - анаграммы.')
else:
    print(f'"{phrase1}" и "{phrase2}" - не анаграммы.')
