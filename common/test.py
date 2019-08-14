def FirstFactorial(num):
    res = 1
    for i in range(2,num+1):
        res = res * i
    print("Output:%d"%res)

if __name__ == '__main__':
    FirstFactorial(3)
