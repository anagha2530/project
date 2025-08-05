class SpanishTranslator:
    def __init__(self):
        self.dictionary = {
            'hello': 'hola' ,
            'goodbye': 'adiós',
            'please':'por favor',
            'thank you':'gracias',
            'yes':'sí',
            'friend':'amigo', 
            'family':'familia',
            'love':'amor'
        }

    def translate(self,text):
        words = text.split()
        translated_words = [self.dictionary.get(word.lower(),word) for word in words]
        return ' '.join(translated_words)
    
def main():
    translator = SpanishTranslator()
    while True:
        print("SPANISH TRANSLATOR")
        print("1.TRANSLATED TEXT")
        print("2.EXIT")
        ch = int(input("enter the choice(1,2): "))

        if ch == 1:
            text = input("enter the text to translate: ")
            translated_text = translator.translate(text)
            print(f"Translated text is {translated_text}")

        elif ch == 2:
            print("exiting............")
            break

        else:
            print("invalid choice")

if __name__ == '__main__':
    main()