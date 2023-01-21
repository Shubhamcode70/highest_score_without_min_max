student_score = input("Enter a list of score separated by space : ").split()
for n in range (0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

highest_score = 0
for score in student_score:
    if score > highest_score:
        hightest_score = score
    else:
        print("Error")
        
print(hightest_score)
