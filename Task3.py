
def words():
    text =  input("Enter your text: ").split(" ")
    text.reverse()
    new_text = " ".join(text)
    return new_text

print(words())