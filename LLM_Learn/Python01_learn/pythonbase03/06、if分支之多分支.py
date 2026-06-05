# # 分数评价
# """
#     90-100  A
#     80-90  B
#     70-80  C
#     60-70  D
#     60以下不及格
# """
#
# score = float(input("请输入你考试的分数"))
#
# if 90 <= score <= 100:
#     print("A")
# elif score >= 80 and score < 90:
#     print("B")
# elif score >= 70 and score < 80:
#     print("C")
# elif score >= 60 and score < 70:
#     print("D")
# elif score >= 0 and score < 60:
#     print("不及格")
# else:
#     print("请输入正确的分数0到100之间")



# 体重评分
# 骨感  苗条  正常   微胖  该减肥了

weight = float(input("请输入你的体重"))

if weight >= 70 and weight <=80:
    print("骨感")
elif weight > 80 and weight <=110:
    print("苗条")
elif weight > 110 and weight <= 140:
    print("正常")
elif weight > 140 and weight <= 180:
    print("微胖")
elif weight > 180 and weight <= 500:
    print("该减肥了")
else:
    print("请输入成年人正常的体重70到500之间")













