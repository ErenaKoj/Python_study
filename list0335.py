a = int(input('整数a:'))
b = int(input('整数b:'))
c = int(input('整数c:'))
d = int(input('整数d:'))

if     a:print('aはゼロではありません。')
if not b:print('bはゼロです。')
x = a or b or c or d
print('x=',x)

if d%c:
  print('cはdの約数ではありません。')
else:
  print('cはdの約数です。')

print('cは' + ('奇数' if c%2 else '偶数') + 'です。')

print('点数dの評価:',end='')
if d < 0 or d > 100:
  print('不正な値')
elif d >= 60:
  print('合格')
else:
  print('不合格')