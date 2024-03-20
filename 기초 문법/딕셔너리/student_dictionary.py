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
    max_score = max(score, key=(lambda x: score[x][v]))
    print(score_legend[v+1] + ':', max_score)
