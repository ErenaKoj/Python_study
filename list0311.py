n=int(input('整数値:'))

if n==0:
  print('その値はゼロです。')
elif n>=-9 and n<=9:
  print('その値は1桁です。')
else:
  print('その値は2桁以上です。')