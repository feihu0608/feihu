# 导入类型支持：Optional 表示字段可以为空（None）
from typing import Optional
# 导入日期时间类型
import datetime

# 导入SQLAlchemy核心工具：
# Date: 日期类型 (年-月-日)
# DateTime: 时间日期类型 (年-月-日 时:分:秒)
# ForeignKeyConstraint: 外键约束（高级配置）
# Index: 索引（加速查询）
# Integer, String: 字段数据类型
# text: 执行SQL原生语句
from sqlalchemy import Date, DateTime, ForeignKeyConstraint, Index, Integer, String, text

# 导入ORM新语法：
# DeclarativeBase: 所有模型的基类
# Mapped: 定义字段类型（SQLAlchemy2.0新写法）
# mapped_column: 定义列属性（约束、类型、默认值等）
# relationship: 定义表关系（一对多、多对一）
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# ==============================================
# 1. 定义ORM模型基类
# 所有数据库表模型都必须继承这个 Base
# ==============================================
class Base(DeclarativeBase):
    pass


# ==============================================
# 2. 部门表模型（departments）
# 功能：存储部门信息
# 关系：一个部门 对应 多个员工（一对多）
# ==============================================
class Departments(Base):
    __tablename__ = 'departments'  # 对应数据库表名

    # 表配置：
    # 给 name 字段创建唯一索引 → 部门名称不能重复
    __table_args__ = (
        Index('name', 'name', unique=True),
    )

    # 部门ID：主键，自增整数
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # 部门名称：字符串，最长50，不允许为空
    # comment 是字段注释，会同步到数据库
    name: Mapped[str] = mapped_column(String(50), nullable=False, comment='部门名称')

    # 部门位置：字符串，最长100，允许为空（Optional）
    location: Mapped[Optional[str]] = mapped_column(String(100), comment='部门位置')

    # 创建时间：日期时间类型
    # server_default=text('CURRENT_TIMESTAMP') → 插入数据时，数据库自动填充当前时间
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    # ==================== 核心：一对多关系 ====================
    # 一个部门包含多个员工
    # back_populates 与 Employees 里的 department 双向绑定
    employees: Mapped[list['Employees']] = relationship('Employees', back_populates='department')


# ==============================================
# 3. 员工表模型（employees）
# 功能：存储员工信息
# 关系：多个员工 对应 一个部门（多对一）
# ==============================================
class Employees(Base):
    __tablename__ = 'employees'  # 对应数据库表名

    # 表配置：
    # 1. ForeignKeyConstraint: 外键约束
    #    department_id 关联 departments.id
    #    ondelete='SET NULL': 部门删除时，员工的 department_id 自动设为 NULL
    # 2. Index: 给 department_id 创建普通索引，加速查询
    __table_args__ = (
        ForeignKeyConstraint(['department_id'], ['departments.id'], ondelete='SET NULL', name='employees_ibfk_1'),
        Index('idx_dept', 'department_id')
    )

    # 员工ID：主键
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # 员工姓名：不允许为空
    name: Mapped[str] = mapped_column(String(50), nullable=False, comment='员工姓名')

    # 年龄：整数，允许为空
    age: Mapped[Optional[int]] = mapped_column(Integer, comment='年龄')

    # 入职日期：日期类型（只有年月日）
    hire_date: Mapped[Optional[datetime.date]] = mapped_column(Date, comment='入职日期')

    # 部门ID：外键，关联部门表
    department_id: Mapped[Optional[int]] = mapped_column(Integer, comment='所属部门ID')

    # ==================== 核心：多对一关系 ====================
    # 一个员工属于一个部门
    # Optional 表示员工可以没有部门（department_id 可为 NULL）
    department: Mapped[Optional['Departments']] = relationship('Departments', back_populates='employees')