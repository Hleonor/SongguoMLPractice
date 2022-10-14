import os
"""
通过给定目录，统计所有的不同子文件类型及占用内存
"""
size_dict = {}  # 记录各类型数据占用存储空间的大小
type_dict = {}  # 各类型数据的数量


def get_size_type(path):
    files = os.listdir(path)  # 获取所有子目录
    for filename in files:
        temp_path = os.path.join(path, filename)  # 将路径拼接成所需的格式
        if os.path.isdir(temp_path):  # 判断取出的是不是一个文件夹
            # 递归调用函数，实现深度文件名解析
            get_size_type(temp_path)
        elif os.path.isfile(temp_path):  # 如果不是文件夹则判断是不是一个文件
            type_name = os.path.splitext(temp_path)[1]  # 该函数会返回文件名称和后缀，此处获得第二个参数
            if not type_name: # 如果没有后缀名
                type_dict.setdefault("None", 0)  # 改键不存在于字典当中，则为其添加一个默认键
                type_dict["None"] += 1  # 键为None的值个数加1
                size_dict.setdefault("None", 0)
                size_dict["None"] += os.path.getsize(temp_path)  # 统计空间大小
            else:  # 真正开始处理有后缀名的文件
                type_dict.setdefault(type_name, 0)
                type_dict[type_name] += 1  # 键为None的值个数加1
                size_dict.setdefault(type_name, 0)
                size_dict[type_name] += os.path.getsize(temp_path)  # 统计空间大小


path = "F:/scope"
get_size_type(path)
for each_type in type_dict.keys():  # 遍历类型字典
    print("%5s 下共有 [%5s] 的文件 [%5d] 个 , 占用内存[%7.2f]MB"%
          (path, each_type, type_dict[each_type], size_dict[each_type] / (1024 * 1024)))

print("总文件数：[%d]" % (sum(type_dict.values())))
print("总内存大小： [%.2f]GB" % (sum(size_dict.values()) / 1024 ** 3))  # **的作用是幂运算，开3次方是因为是GB
