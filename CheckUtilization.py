def checkUtilization(a, b, target):
    a = sorted(a, key=lambda x:x[1])
    b = sorted(b, key=lambda x:x[1])
    diff = float("inf")
    lo = 0
    hi = len(b)-1
    res = []
    while lo<len(a) and hi>=0:
        idx1, num1 = a[lo]
        idx2, num2 = b[hi]
        if target-num1-num2==diff:
            res.append([idx1,idx2])
        elif num1+num2<=target and target-num1-num2<diff:
            res.clear()
            res.append([idx1,idx2])
            diff = target-num1-num2
        if num1+num2<target:
            lo+=1
        else:
            hi-=1
    return res


a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

print(checkUtilization(a,b,target))