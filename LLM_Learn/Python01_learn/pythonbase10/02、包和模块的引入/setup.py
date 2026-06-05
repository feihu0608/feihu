from setuptools import setup
# 这个文件名字不能随便改

# 打包的时候不能同时打包两个
# 否则两个包就会建立依赖关系，真正两个包是没依赖的，后期安装任何一个包都报错，说找不到另外一个包



# 打包第一个独立包

# def package1():
#     setup(
#         name="atguigu_graphic", # 打包后的包名称，必须唯一
#         version="0.1.0",        # 版本说明
#         packages=["mygraphic"],  # 手动指定第一个包的目录
#         python_requires=">=3.7", # python版本要求
#     )

# 打包第二个独立包
# def package2():
#     setup(
#         name="atguigu_math",
#         version="0.1.0",
#         packages=["mymath"],  # 手动指定第二个包的目录
#         python_requires=">=3.7",
#     )

if __name__ == "__main__":
    # 依次执行两个包的打包（必须一个一个来，不能一起打包，一起打包那两个包会互相依赖，后期安装会出问题）
    # package1()
    # package2()

    from setuptools import setup, find_packages

    setup(
        name="atguigu",  # 打包后的包名称，必须唯一
        version="0.1.0",  # 版本号
        packages=find_packages(),  # 自动识别主包下的所有子包
        python_requires=">=3.7",  # 指定python版本
    )