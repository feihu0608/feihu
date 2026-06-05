from datetime import date


from database import SessionLocal
from models import Department, Employee

def insert_data():
    # 获取数据库会话
    db = SessionLocal()
    try:
        # =========== 第一步：新增部门 =============
        new_dept = Department(
            name="运行部",  # 部门名称（唯一）
            location="北京总部"  # 部门位置
        )
        db.add(new_dept)  # 将部门对象加入会话
        db.commit()  # 提交到数据库（执行 INSERT 语句）
        db.refresh(new_dept)  # 刷新对象，获取自增的 id 等字段

        # =========== 第二步：新增关联的员工 ===========
        # 员工1：关联上面创建的研发部
        emp1 = Employee(
            name="张三",
            age=30,
            hire_date=date(2023, 1, 1),  # 入职日期（datetime.date 类型）
            department_id=new_dept.id  # 关联部门 ID（外键）
        )
        # 员工2：同部门的另一个员工
        emp2 = Employee(
            name="李四",
            age=28,
            hire_date=date(2023, 3, 15),
            department_id=new_dept.id
        )

        # 批量添加员工（也可逐个 add）
        db.add_all([emp1, emp2])
        db.commit()  # 提交员工数据
        # 刷新员工对象，获取自增 ID
        db.refresh(emp1)
        db.refresh(emp2)

        # ===================== 输出结果 =====================
        print(f"新增部门：ID={new_dept.id}，名称={new_dept.name}，位置={new_dept.location}")
        print(f"新增员工1：ID={emp1.id}，姓名={emp1.name}，所属部门={new_dept.name}")
        print(f"新增员工2：ID={emp2.id}，姓名={emp2.name}，所属部门={new_dept.name}")

        # 验证关联关系（通过 ORM 关联查询）
        print("\n【验证关联关系】")
        # 从员工查部门
        print(f"员工{emp1.name}的部门名称：{emp1.department.name}")
        # 从部门查员工
        dept_employees = new_dept.employees
        print(f"部门{new_dept.name}的员工列表：{[emp.name for emp in dept_employees]}")

    except Exception as e:
        db.rollback()  # 出错时回滚
        print(f"新增失败：{e}")
    finally:
        db.close()  # 关闭会话

