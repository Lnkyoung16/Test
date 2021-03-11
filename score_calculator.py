
def score_calculator(student):
    score = []
    for s in range(0, len(student)):
        if student[s] <= 100 and student[s] >= 90:
            ss = "A"
            score.append(ss)
        elif student[s] < 90 and student[s] >= 80:
            ss = "B"
            score.append(ss)
        elif student[s] < 80 and student[s] >= 70:
            ss = "C"
            score.append(ss)
        elif student[s] < 70 and student[s] >= 60:
            ss = "D"
            score.append(ss)
        else:
            ss = "F"
            score.append(ss)
    return score

def message(score):
    for m in range(0, len(score)):
        if score[m] == "A":
            print("Congratulation.")
        elif score[m] == "F":
            print("You failed the test.")
        else:
            print(score[m])


def message_calculator(student_score):
    result = score_calculator(student_score)
    message(result)

new_student = [65, 78, 16, 51, 99]

message_calculator(new_student)