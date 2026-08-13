# 🪨📄✂️ Rock Paper Scissors Game

An interactive **Rock Paper Scissors** game built in **Python**.  
Play against the computer, track scores across multiple rounds, and see who wins!

---

## 🎮 Features
- Play Rock, Paper, Scissor against the computer
- Random computer moves using Python's `random` module
- Multiple rounds with a scoreboard
- Win / Lose / Draw result messages
- Handles invalid user input gracefully
- Fun emojis for better user experience
- Live scoreboard updates after each round

---

## 🛠️ Technologies Used
- Python 3
- `random` module
- Conditional logic (`if/elif/else`)
- Loops
- Formatted output (f-strings)

---

## 📂 Project Structure
rock-paper-scissors/
│── rock_paper_scissors.py   # Main game file
│── README.md                # Project documentation


---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/rock-paper-scissors.git
   cd rock-paper-scissors
   python rock_paper_scissors.py

🖥️ Gameplay Output:
🎮 How many rounds do you want to play? 7

--- Round 1 of 7 ---
Enter your move (Rock, Paper, Scissor): Rock
👉 You chose: Rock, Computer chose: Scissor
🪨 Rock smashes Scissor → You win
📊 Current Score → You: 1 | Computer: 0

--- Round 2 of 7 ---
Enter your move (Rock, Paper, Scissor): Rock
👉 You chose: Rock, Computer chose: Paper
📄 Paper covers Rock → Computer wins
📊 Current Score → You: 1 | Computer: 1

... (game continues)

=== Final Score ===
👤 You: 4 | 💻 Computer: 2
🎉 Congratulations! You are the overall winner!



   📚 What I Learned
Using Python lists to store choices

Handling user input and validation

Applying conditional logic for game rules

Using loops for multiple rounds

Tracking scores with variables

Formatting output for a better user experience
