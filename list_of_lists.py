# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()
students = []
score_list = []
for i in range(N):
    name = raw_input()
    score = raw_input()
    students.append([name, float(score)])
  
second_lowest = sorted(list(set([score for name, score in students])),reverse = True)[-2]

name_list = []
for student in students:
    if student[1] == second_lowest:
        name_list.append(student[0])

name_list.sort()

for name in name_list:
    print name