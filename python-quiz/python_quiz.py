#Python quiz
questions = [
    "1. What is the output of print(10 % 3)?",
    "2. What is the first index of a Python list?",
    "3. What is the output of print('Python'[2])?",
    "4. What is the output of numbers=[10,20,30,40]; print(numbers[2])?",
    "5. Which method adds an item to the end of a list?",
    "6. What is the output of for i in range(3): print(i)?",
    "7. What is the output of x=10; if x>5: print('Yes') else: print('No')?",
    "8. Which of the following is immutable?",
    "9. What is the output of summing [1,2,3,4,5]?",
    "10. Which brackets are used to create a dictionary?",
    "11. What is the output of student={'name':'Ram','age':20}; print(student['name'])?",
    "12. How do you add 'city':'Kathmandu' to student={'name':'Ram'}?",
    "13. What is the output of data={'a':10,'b':20,'c':30}; print(data['b'])?",
    "14. What is the output of scores={'Ram':80,'Sita':90}; for name in scores: print(name)?",
    "15. What is the output of fruits={'apple':3,'banana':5,'orange':2}; total=0; for f in fruits: total+=fruits[f]; print(total)?"
]

options = [
    ["A. 1", "B. 3", "C. 3.33", "D. 0"],
    ["A. 0", "B. 1", "C. -1", "D. None"],
    ["A. P", "B. y", "C. t", "D. h"],
    ["A. 10", "B. 20", "C. 30", "D. 40"],
    ["A. add()", "B. append()", "C. insert()", "D. push()"],
    ["A. 1 2 3", "B. 0 1 2", "C. 0 1 2 3", "D. 3"],
    ["A. Yes", "B. No", "C. 10", "D. Error"],
    ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
    ["A. 10", "B. 15", "C. 20", "D. 5"],
    ["A. []", "B. ()", "C. {}", "D. <>"],
    ["A. name", "B. Ram", "C. age", "D. 20"],
    ["A. student.add(...)", "B. student['city']='Kathmandu'", "C. student.insert(...)", "D. student.city='Kathmandu'"],
    ["A. 10", "B. 20", "C. 30", "D. b"],
    ["A. 80 and 90", "B. Ram and Sita", "C. scores", "D. Error"],
    ["A. 5", "B. 8", "C. 10", "D. 3"]
]

answers = ["A","A","C","C","B","B","A","C","B","C","B","B","B","B","C"]


score = 0
wrong = 0


for i in range(len(questions)):
    print("\n" + questions[i])
    for opt in options[i]:
        print(opt)

    
    while True:
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        if user_answer in ["A","B","C","D"]:
            break
        else:
            print("Invalid input! Please enter A, B, C, or D.")

    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is:", answers[i])
        wrong += 1

print("\n================= RESULT =================")
print("Total Correct:", score)
print("Total Wrong:", wrong)
print("Final Score:", score, "out of", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", round(percentage, 2), "%")


if percentage >= 90:
    print("Result: Excellent")
elif percentage >= 70:
    print("Result: Very Good")
elif percentage >= 50:
    print("Result: Good")A
else:
    print("Result: Needs Improvement")
