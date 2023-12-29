import random

def play_round():
    print("Welcome to Rock, Paper, Scissors game!")
    user = input("Choose your weapon: ")
    user = user.lower()
    
    while user not in ["rock", "paper", "scissors"]:
        print("Invalid Input!")
        user = input("Choose your weapon: ")
        user = user.lower()
    
    print("Your weapon is: " + user)
    computer = random.choice(["rock", "paper", "scissors"])
    print("Computer's weapon is: " + computer)
    
    if user == computer:
        return "It's a tie!", "tie"
    elif user == "rock":
        return "You win!" if computer == "scissors" else "You lose!", "win" if computer == "scissors" else "lose"
    elif user == "paper":
        return "You win!" if computer == "rock" else "You lose!", "win" if computer == "rock" else "lose"
    elif user == "scissors":
        return "You win!" if computer == "paper" else "You lose!", "win" if computer == "paper" else "lose"

def main():
    rounds_played = 0
    wins = 0
    
    while True:
        result, outcome = play_round()
        print(result)
        
        if outcome == "win":
            wins += 1
        
        rounds_played += 1
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    
    print("\nGame Over!")
    print("Rounds played:", rounds_played)
    print("Wins:", wins)

if __name__ == "__main__":
    main()