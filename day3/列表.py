list = ["顶呱呱","吃什么","真是啥子","真是啥子"]
list.append("so what")# 增加
list.insert(2,"beautiful")# 增加在2的位置
list[1] = "面包"  # 改
# del list[3]
# list.remove("beautiful")#
#list.pop()# 不输入坐标默认删除最后一位

print(list)
# print(list.index("真是啥子"))# 查询位置
print(list.count("真是啥子"))#统计有多少个
#list.clear()# 清空所有
list.reverse()# 反转
list.sort()# 排序，字符、数字、大写、小写
list2 = [1,2,3]
list.extend(list2) #拓展合并

print(list,list2)
del list2  #删除变量
print(list)
#print(list[0:2])
# print(list[-3:])
#print(list[-2:])
