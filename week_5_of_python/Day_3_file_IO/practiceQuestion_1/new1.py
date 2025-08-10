####            Now lets check if the word "learning" exits or not

def check_for_word():
    word = "learning"
    with open("practice.txt","r")as file:
        reading = file.read()
        if reading.find(word)!=-1:
            print("learning is present")
        else:
            print("Not here")


check_for_word()