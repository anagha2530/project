def generate_name(full_name):
    words = full_name.split()
    acronym = ' '.join(word[0].upper() for word in words)
    return acronym

def main():
    print("NAME ACRONYM GENERATOR")
    while True:
        full_name = input("enter your full name: ")
        if full_name.lower() == 'exit':
            break

        acronym = generate_name(full_name)
        print(f"The acronym for {full_name} is {acronym}")

if __name__ == "__main__":
    main()