from itertools import combinations

sentence = sorted(input().split())  # apple is a fruit
length = len(sentence)
for i in range(1,length+1):
    words = set(sorted(combinations(sentence,i)))
    #print(words)
    for j in list(sorted(words)):
        print(*j)
        
# a
#apple
#fruit
#is
#a apple
#a fruit
#a is
#apple fruit
#apple is
#fruit is
#a apple fruit
#a apple is
#a fruit is
#apple fruit is
#a apple fruit is