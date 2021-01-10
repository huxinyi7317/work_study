def jiecheng(a):
    if a == 1:
        return a
    else:
        return a*jiecheng(a-1)
#递归函数

def xiaotuzi(n):
    if n in [1,2]:
        return 1
    else:
        return xiaotuzi(n-1)+xiaotuzi(n-2)

a = int(input('请输入月份'))
b = xiaotuzi(a)
print(b)



