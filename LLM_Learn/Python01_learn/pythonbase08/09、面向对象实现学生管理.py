class Student(object):
    """
        专门用来造学生
    """
    def __init__(self,id,name,age,gender):
        self.id = id
        self.name = name
        self.__age = age
        self.gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age


class Manager:
    """
        专门用来增删改查学生的
    """
    def __init__(self):
        self.student_list = []


    def add_student(self,student):
        self.student_list.append(student)

    def delete_student(self,id):
        for i,student in enumerate(self.student_list):
            if student.id == id:
                del self.student_list[i]
                print(f"删除{student.name}成功")
                break
        else:
            print("没有找到要删除的学生")

    def update_student(self,id):
        for student in self.student_list:
            if student.id == id:
#                 修改
                name = input("输入学生的姓名")
                age = int(input("输入学生的年龄"))
                gender = input("输入学生的性别")

                student.name = name
                student.age = age
                student.gender = gender
                print("修改学生成功")
                break
        else:
            print("没有找到要修改的学生")

    def show_student(self,id):
        for student in self.student_list:
            if student.id == id:
                return student


    def show_all_student(self):
        return self.student_list


if __name__ == '__main__':
    print("*"*30 + "欢迎来到学生管理系统" + "*"*30)
    manager = Manager() #学生管理的实例对象
    while True:
        num = int(input("请选择您的操作：1、添加学生 2、删除单个学生 3、修改单个学生 4、查询单个学生 5、查询所有学生 6、退出"))
        match num:
            case 1:
                id = int(input("请输入学生id"))
                name = input("请输入学生姓名")
                age = int(input("请输入学生年龄"))
                gender = input("请输入学生性别")
                student = Student(id=id,name=name,age=age,gender=gender)
                manager.add_student(student)

            case 2:
                id = int(input("请输入学生id"))
                manager.delete_student(id)

            case 3:
                id = int(input("请输入学生id"))
                manager.update_student(id)
            case 4:
                id = int(input("请输入学生id"))
                student = manager.show_student(id)
                if student:
                    print(f"{student.id}--{student.name}--{student.age}--{student.gender}")
                else:
                    print("没有找到对应的学生")
            case 5:
                student_list = manager.show_all_student()
                if student_list:
                    for student in student_list:
                        print(f"{student.id}--{student.name}--{student.age}--{student.gender}")
                else:
                    print("请先添加学生，目前没有学生")
            case 6:
                print("欢迎下次再来拜拜")
                break



