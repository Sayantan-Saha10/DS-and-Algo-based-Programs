def multiply(i, j):
    e = len(str(i))
    f = len(str(j))
    if (e>1 and e%2 == 0 and e==f):
        a = int(str(i)[:int(e/2)])
        b = int(str(i)[int(e/2):])
        c = int(str(j)[:int(e/2)])
        d = int(str(j)[int(e/2):])
        ac = multiply(a,c)
        bd = multiply(b,d)
        abcd = multiply((a+b),(c+d)) - ac - bd
        return (pow(10,e) * ac) + (pow(10,int(e/2)) * abcd) + bd
    elif (e>1 and (e%2 != 0 or e!=f)):
        sum = 0
        for indexl, l in enumerate(str(j)[::-1]):
            mulvalue = 0
            for indexm, m in enumerate(str(i)[::-1]):
                mulvalue += (multiply(int(l),int(m)) * pow(10, indexm))
            sum += (mulvalue * pow(10, indexl))
        return sum
    else:
        return i*j


value1= 3141592653589793238462643383279502884197169399375105820974944592
value2= 2718281828459045235360287471352662497757247093699959574966967627
print(multiply(value1, value2))

