f = open('yesterday','r',encoding='utf-8')

newf = open('newone','w',encoding='utf-8')


for line in f:
    if "It made" in line:
        line = line.replace("smile","cry")
    newf.write(line)
