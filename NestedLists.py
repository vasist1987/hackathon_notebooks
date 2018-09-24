

a=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = round(float(input()),2)
        a.append([name,round(score,2)])
        a.sort(key= lambda x:x[1],reverse=True)
b=min([sublist[1] for sublist in a])
c=[sublist[:] for sublist in a if sublist[1]==b]
a=[n for n in a if n not in c]

b=min([sublist[1] for sublist in a])
c=[sublist[:] for sublist in a if sublist[1]==b]
x=[sublist[0] for sublist in c]
x.sort()
for i in x:
    print(i)
