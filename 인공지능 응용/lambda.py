# sequences = [10,2,8,7,5,4,3,11,0, 1]
# filtered_result = filter (lambda x: x > 4, sequences) 
# print(list(filtered_result))

sequences = [[1, 2],[3, 4], [5,6]]

filtered_result = list(filter(lambda x: sequences[x]%2==0,sequences))
print(filtered_result)

