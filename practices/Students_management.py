#功能界面函数
def info_print():
    print('请选择功能------------')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示所有学员')
    print('6.退出系统')
    print('-'*20)
# 等待存储所有学员的信息
info=[]
# 添加学员信息的函数
def add_info():
    """添加学员"""
# 用户输入：学号、姓名、手机号
    new_id=input('请输入学号：')
    new_name=input('请输入姓名：')
    new_tel=input('请输入手机号：')
    global info
    for i in info:
        if new_name==i['name']:
            print('此用户已经存在！')
            return
    # 追加字典
    info_dict={}
    info_dict['id']=new_id
    info_dict['name']=new_name
    info_dict['tel']=new_tel
    # print(info_dict)
    info.append(info_dict)
    print(info)

# 删除学员
def del_info():
    """删除学员"""
    del_name=input('请输入要删除的学员的姓名：')
    global info
    for i in info:
        if del_name==i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在')
    print(info)
# 修改函数
def modify_info():
    """修改学员信息"""
    modify_name=input('请输入要修改的学员姓名：')
    global info
    for i in info:
        if modify_name==i['name']:
            i['tel']=input('请输入新的手机号：')
            break
    else:
        print('该学员不存在')
    print(info)
# 查询学员函数
def search_info():
    """查询学员信息"""
    search_name=input('请输入要查询的学员的姓名：')
    global info
    for i in info:
        if search_name==i['name']:
            print('查询到的学员信息如下：————————————')
            print(f"学员的学号是{i['id']},姓名是{i['name']},手机号是{i['tel']}")
            break
    else:
        print('查无此人...')

# 显示所有学员信息
def print_all():
    """显示所有学员信息"""
    print('学号\t姓名\t手机号')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")
#显示功能界面
while True:
    info_print()
    # 用户输入功能序号
    user_num=int(input('请输入功能序号：'))
    # 根据用户选择，执行不同功能
    if user_num==1:
        # print('添加')
        add_info()
    elif user_num==2:
        # print('删除')
        del_info()
    elif user_num==3:
        # print('修改')
        modify_info()
    elif user_num ==4:
        # print('查询')
        search_info()
    elif user_num ==5:
        # print('显示所有')
        print_all()
    elif user_num ==6:
        # print('退出系统')
        exit_flag=input('确定要退出吗？yes or no')
        if exit_flag=='yes':
            break
    else:
        print('输入的功能序号有误')