import random

# Available choices
item_list = ["Rock", "Paper", "Scissor"]

# Scores
user_score = 0
comp_score = 0

# Ask how many rounds to play
rounds = int(input("🎮 How many rounds do you want to play? "))

for i in range(rounds):
    print(f"\n--- Round {i+1} of {rounds} ---")

    # User input
    user_choice = input("Enter your move (Rock, Paper, Scissor): ").capitalize()
    comp_choice = random.choice(item_list)

    print(f"👉 You chose: {user_choice}, Computer chose: {comp_choice}")

    # Game logic
    if user_choice == comp_choice:
        print("🤝 It's a tie!")

    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("📄 Paper covers Rock → Computer wins")
            comp_score += 1
        else:
            print("🪨 Rock smashes Scissor → You win")
            user_score += 1

    elif user_choice == "Paper":
        if comp_choice == "Scissor":
            print("✂️ Scissor cuts Paper → Computer wins")
            comp_score += 1
        else:
            print("📄 Paper covers Rock → You win")
            user_score += 1

    elif user_choice == "Scissor":
        if comp_choice == "Rock":
            print("🪨 Rock smashes Scissor → Computer wins")
            comp_score += 1
        else:
            print("✂️ Scissor cuts Paper → You win")
            user_score += 1

    else:
        print("⚠️ Invalid choice! Please enter Rock, Paper, or Scissor.")

# Final results
print("\n=== Final Score ===")
print(f"👤 You: {user_score} | 💻 Computer: {comp_score}")

if user_score > comp_score:
    print("🎉 Congratulations! You are the overall winner!")
elif comp_score > user_score:
    print("💻 Computer wins the game! Better luck next time.")
else:
    print("🤝 It's a tie overall!")
