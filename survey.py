class Survey:
    def __init__(self,questions):
        self.questions = questions
        self.responses = {}

    def conductsurvey(self):
        print("STARTING THE SURVEY")
        for question in self.questions:
            response = input(question+" ")
            self.responses[question] = response
        print("Survey Completed")

    def display_result(self):
        print("SURVEY RESULT")
        for i in self.responses.keys():
            print(f"{i} : {self.responses[i]}")

def main():
    questions = [
                 "1.Whats your name?",
                 "2.whats your age?",
                 "3.where are you from?"
                ]
    
    survey = Survey(questions)

    while True:
        print("\nSURVEY MENU")
        print("""
              1.Conduct Survey
              2.View Survey Result
              3.Exit""")
        
        ch = int(input("enter the choice(1,2,3): "))
        if ch == 1:
            survey.conductsurvey()
        elif ch == 2:
            survey.display_result()
        elif ch == 3:
            print("exit..")
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()
    