score = 50

if score >= 80:
    print("合格")
elif score >= 50:       #上から実行されるので注意
    print("再試験")     #elifは何個でも書ける
else:
    print("不合格")