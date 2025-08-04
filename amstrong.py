def is_armstrong(number):
   
    num_str = str(number)
    num_digits = len(num_str)
    
    
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    
    return digit_sum == number

def main():
    try:
       
        num = int(input("Enter a number to check if it's an Armstrong number: "))
        
        
        if num < 0:
            print("Please enter a non-negative number.")
            return
            
        if is_armstrong(num):
            print(f"{num} is an Armstrong number!")
        else:
            print(f"{num} is not an Armstrong number.")
            
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()