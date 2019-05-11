try:
    ret = int(input("number>>> "))
    print(ret*'*')
except Exception as e:
    print(e)
    print("请输入整数数字")
