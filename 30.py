import os
f = open('test.txt','r',encoding='utf-8')
fd = f.readlines()
step = 30
b = [fd[i:i+step] for i in range(0,len(fd),step)]
for i in range(0,len(b)):
    txt = '{}.txt'.format(str(i))
    with open(txt, 'w', encoding='utf-8') as f:
        for line in b[i]:
            f.write(line )
f.close()