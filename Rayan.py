import random

def number_guessing_game():
    print("========================================")
    print("      WELCOME TO ADVANCED GUESS         ")
    print("========================================")
    
    score = 0
    
    while True:
        print("\nSelect Difficulty:")
        print("1. Easy (1 - 50, 10 attempts)")
        print("2. Medium (1 - 100, 7 attempts)")
        print("3. Hard (1 - 200, 5 attempts)")
        print("4. Exit Game")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            upper_limit, max_attempts = 50, 10
        elif choice == '2':
            upper_limit, max_attempts = 100, 7
        elif choice == '3':
            upper_limit, max_attempts = 200, 5
        elif choice == '4':
            print(f"\nThanks for playing! Final Score: {score}")
            break
        else:
            print("Invalid choice. Please select between 1 and 4.")
            continue
            
        secret_number = random.randint(1, upper_limit)
        attempts = 0
        won = False
        
        print(f"\nI have picked a number between 1 and {upper_limit}. You have {max_attempts} attempts.")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            except ValueError:
                print("⚠️ Invalid input! Please enter an integer.")
                continue
                
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Spot on! You guessed it in {attempts} attempts.")
                score += (max_attempts - attempts + 1) * 10
                won = True
                break
            elif guess < secret_number:
                print("📉 Too low!")
            else:
                print("📈 Too high!")
                
            # Provide a dynamic hint on the 3rd failed attempt
            if attempts == 3 and not won:
                parity = "even" if secret_number % 2 == 0 else "odd"
                print(f"💡 Hint: The secret number is an {parity} number.")
                
        if not won:
            print(f"❌ Out of attempts! The correct number was {secret_number}.")
            
        print(f"Current Total Score: {score}")

if __name__ == "__main__":
    number_guessing_game()