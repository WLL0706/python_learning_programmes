# fn1=lambda a,b:a if a>b else b
# print(fn1(100,500))

students=[
    {'name':'TOM','age':20},
    {'name':'ROSE','age':19},
    {'name':'LL','age':23}
]
students.sort(key=lambda x: x['name'],reverse=True)#降序
print(students)

students.sort(key=lambda x: x['age'])#默认升序
print(students)