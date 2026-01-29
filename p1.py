def main():
    correct_answers = ["A", "C", "B", "D"]

    answers = []
    total_score = 0
    
    for i in range(len(correct_answers)):
        print("Question",i+1)
        f= input(f"what did you get").strip().upper()
        answers.append(f)
        0<=len(answers) <= 4
        if correct_answers(i) == answers(i):
            print("correct")
        else:
           print("wrong")
        total_score = total_score + 1
       
main()
