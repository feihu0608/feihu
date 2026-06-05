"""
    给定一个只包括“(”，“)”，“[”，“]”，“{”，“}”的字符串s，判断字符串是否有效。
    有效字符串需满足：
    - 左括号必须用相同类型的右括号闭合。
    - 左括号必须以正确的顺序闭合。
    - 每个右括号都有一个对应的相同类型的左括号。

    举例：
    s1 = "{[()]}"  True
    s2 = "{}[]()"  True
    s3 = "{[}"  False
    s4 = ""  False
    s4 = "123"  False

"""


def is_valid(s:str)->bool:
    if len(s) == 0:
        return False
    stack = []  # 维护一个空列表 用于存储左半部分的括号
    bracket_dict = {")":"(","]":"[","}":"{"}
    for char in s:
        # 表示判断是否属于字典中的键 是则为True
        if char in bracket_dict:
            # 逻辑
            top = stack.pop() if stack else None
            if top != bracket_dict[char]:
                return False
        else:
            stack.append(char)
    return  len(stack) == 0

if __name__ == "__main__":
    s = "{[(])]}"
    print(is_valid(s))