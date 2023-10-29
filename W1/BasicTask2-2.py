# 输出斐波那契数列前20个数

f1 = 1
f2 = 1
f_list = [1,1]
while len(f_list) < 20:
    f_latest = f1 + f2
    f1 = f2
    f2 = f_latest
    f_list.append(f_latest)
print(f_list)




