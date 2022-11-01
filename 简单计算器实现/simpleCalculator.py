import re


def calculate(n1, n2, operator):
    # 对两数进行操作
    if operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    elif operator == "/":
        return n1 / n2


def is_operator(e):
    # 操作符号判断
    opers = ['+', '-', '*', '/']
    return True if e in opers else False


# 将算式处理成列表，解决 - 号是负数还是减号
def formula_format(formula):
    # 去掉算式中的空格
    '''
        此处re的作用是把一个字符串替换为另一个字符串。
        第一个参数是要替换的字符串，若是re的形式则作为正则表达式
        第二个是目标字符串。此处是把所有空格 '' 替换成 ''，即完全去掉现有的空格
        第三是输入的目标字符串。
    '''
    formula = re.sub('', '', formula)
    # 以'横杠数字'分隔，其中正则表达式为:(\-\d+\.?\d*)
    # 以\-表示匹配横杠开头；\d+表示匹配数字一个或者多个；\.表示匹配小数点0个或1个；\d*表示匹配数字1个或多个
    formula_list = [i for i in re.split('(\-\d+\.?\d*)', formula) if i]  # 这里的if i表示去掉空字符串
    final_formula = []
    for item in formula_list:
        # 第一个是以横杠开头的数字(包括小数)final_formula
        # 即第一个是负数，横杠就不是减号
        if len(final_formula) == 0 and re.search('^\-\d+\.?\d*$', item):
            final_formula.append(item)
            continue

        if len(final_formula) > 0:
            # 如果 final_formula最后一个元素是运算符['+', '-', '*', '/', '(']
                # 则横杠数字不是负数
            if re.search('[\+\-\*\/\(]]$', final_formula[-1]):
                final_formula.append(item)
                continue
        # 按照运算符分割开
        item_spilt = [i for i in re.split('([\+\-\*\/\(]])', item) if i]
        final_formula += item_spilt
    return final_formula
