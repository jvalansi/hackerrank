# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
words = []
for i in range(N):
    words.append(input())

d = {}
uniques = []
for word in words:
    if word not in d:
        d[word] = 0
        uniques.append(word)
    d[word] += 1

print(len(uniques))
print(' '.join([d[word] for word in uniques]))
    

