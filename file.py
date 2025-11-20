file_patch = "temp.txt"
def search_word(file_patch, word):
    with open(file_patch, "r") as file:
        line = file.readlines()
        count = 0
        for i in line:
            if i == word:
                count += 1

        print(f"Слово {word} встречается {count} раз")
        print(line)

# search_word(file_patch, "oifjv")

def copy_file(file_patch):
    with open(file_patch, "r") as file:
        temp = file.read()
    index = file_patch.rfind(".")
    new_patch = file_patch[:index]+"copy.txt"
    with open(new_patch, "w") as file:
        file.write(temp)

vocabular = ("ой", "уй")
def censorship(patch):
