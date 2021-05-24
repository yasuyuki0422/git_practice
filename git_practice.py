money = int(input('金額（円）> '))

print('金額: ' + str(money) + '円')

number = money // 10000
money = money % 10000
print('一万円札 = ' + str(number) + '枚')

number = money // 5000
money = money % 5000
print('五千円札 = ' + str(number) + '枚')

number = money // 1000
money = money % 1000
print('千円札 = ' + str(number) + '枚')

number = money // 500
money = money % 500
print('五百円玉 = ' + str(number) + '枚')

number = money // 100
money = money % 100
print('百円玉 = ' + str(number) + '枚')

number = money // 50
money = money % 50
print('五十円玉 = ' + str(number) + '枚')

number = money // 10
money = money % 10
print('十円玉 = ' + str(number) + '枚')

number = money // 5
print('五円玉 = ' + str(number) + '枚')

money = money % 5
print('一円玉 = ' + str(money) + '枚')
