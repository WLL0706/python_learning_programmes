'''name_list=['TOM','Lily','ROSE']
i=0
while i<len(name_list):
	print(name_list[i])
	i+=1'''

'''name_list=[['a','w','m'],['b','e','r'],['c','d','f']]
print(name_list[0][1])'''

import random
teachers=['A','B','C','D','E','F','G','H']
offices=[[],[],[]]
for name in teachers:
    num=random.randint(0,2)
    offices[num].append(name)
i=1
for office in offices:
    print(f'办公室{i}的人数是{len(office)}.老师分别是：')
    for name in office:
        print(name)
    i+=1