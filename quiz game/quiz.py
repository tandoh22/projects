# python quiz game
questions = (
    "What year did Ghana gain their independence? ",
    "What is the main memory of the computer? ",
    "Which of the following operating systems is open-source? ",
    "What does OS stands for? ",
    "The brain of the computer system is called? ")

options = (("A. 1958", "B. 1800", "C. 1957", "D. 1902"), 
           ("A. Hard disk drive", "B. floppy disk", "C. RAM", "D. ROM"), 
           ("A. Windows", "B. macOS", "C. Linux", "D. Chrome OS"), 
           ("A. Optical session", "B. Operating Systems", "C. Operating section", "D. Output system"), 
           ("A. RAM", "B. ROM", "C. Hard drive", "D. CPU"))

answers = ("C", "A", "C", "B", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter (A, B, C, D): ")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 5
        print("correct")
    else:
        print("incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print()
if score >= 20:
    print(f"GREAT JOB! Your total score is {score}")
else:
    print(f"your total score is {score}, better luck next time.")

