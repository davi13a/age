driving = input('請問你有沒有開過車？')
age = int(input('請問你的年齡？'))
if driving == '有':
    if age >= 18:
        print('你通過測驗了！')
    else:
        print('未成年怎麼開過車！')
elif driving == '無':
    if age >=18:
        print('你可以參加考試')
    else:
        print('你要滿18歲才可以參加考試')
else:
    print('請輸入 有/無')
    raise SystemExit
