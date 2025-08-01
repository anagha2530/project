def word_counter(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def main():
    sentence = input("enter the sentence: ")
    word_count = word_counter(sentence)
    print("word occurances: ")
    for word,count in sorted(word_count.items()):
        print(""+word+":" +str(count))
    
if __name__ == "__main__":
    main()




    