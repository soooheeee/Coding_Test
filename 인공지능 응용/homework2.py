score_legend = ['name', 'Math', 'Eng', 'History']
score = {'John': [70,80,90], 'Tom':[90,95,98], 'Mary':[95,85,99]}
print(score_legend)

a=[]
sum=0

print(score_legend)


for k,v in score.items():
    for i in range(3):
        a.append(v[i])
        print(v[i])

        sum+=v[i]

    print('sum:',sum,'mean:',sum/3)
    sum=0
    mean=0

for v in range(0, 3):
    max_score = max(score, key=(lambda x: score[x]))
    print(score_legend[v+1] + ':', max_score)


# score_legend = ["Name","Math","ENG","History"]
# score = {"John":[70,80,90],"Tom":[90,95,98],"Mary":[95,85,99]}
# max_student = {"Math:","ENG:","History:"}

# max_li=[]
# a=[]
# _max = 0
# sum=0

# print(score_legend)


# for k,v in score.items():
#     for i in range(3):
#         a.append(v[i])
#         print(v[i])

#         sum+=v[i]
    

#     print('sum:',sum,'mean:',sum/3)
#     sum=0
#     mean=0
#     # max_li.append(v[i])
#     # print('v:',max_li)
#     max_li.append(v)
#     print('v:',max_li)

# for j in range(3):
#     for k in range(3):
#         if max_li[k][j] > _max:
#             _max = max_li[k][j]
#     print(_max)

    




# for k,v in score.items():
#         print('0',v[0])
#         # max_li.append(v[i])
#         max_li.append(v)
#         print('v:',max_li)
# print(max_li)


# print(max(max_li))

# for k,v in score.items():
#     if max_li[j] == v[j]:
#         print(k)



# score_legend = ["Name","Math","ENG","History"]
# score = {"John":[70,80,90],"Tom":[90,95,98],"Mary":[95,85,99]}
# max_student = {"Math:","ENG:","History:"}

# max_li=[]
# a=[]
# max = 0

# print(score_legend)


# for k,v in score.items():
#     for i in range(3):
#         a.append(v[i])
#         print(v[i])
#         if max < v[i]:
#             max = v[i]
#             name=k
#     #   print('name',name)
#     max_li.append(max)

#     print('max',max)
#     max_student[]
# #   print(name)

# print(max_li)


# for k,v in score.items():
#     if max_li[j] == v[j]:
#         print(k)














# Legends and scores as provided
# score_legend = ["Name", "Math", "ENG", "History"]
# scores = {"John": [70, 80, 90], "Tom": [90, 95, 98], "Mary": [95, 85, 99]}

# # Dictionary to hold the max student name for each subject
# max_student = {"Math": "", "ENG": "", "History": ""}

# # Print the score legend
# print(score_legend)

# # Iterate over each subject (excluding 'Name')
# for i in range(1, len(score_legend)):  # Starting from 1 to skip 'Name'
#     subject = score_legend[i]
#     # Iterate over each student and their scores
#     for name, scores_list in scores.items():
#         # If current score is greater than the max score found so far for the subject
#         if scores_list[i - 1] > max_student.get(subject, (None, 0))[1]:
#             # Update the max score and the student's name
#             max_student[subject] = (name, scores_list[i - 1])

# # Print out the max scores and the students who achieved them
# for subject in max_student:
#     name, score = max_student[subject]
#     print(f"{subject}: {name}")

# # This will display the highest scoring student for each subject
