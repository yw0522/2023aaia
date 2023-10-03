#九九乘法表
#1x1=1 1x2=2
for i in range(1,10):
  for j in range(1,10):
    print(i, 'x', j, '=', i*j,  sep='', end=' ')
  print()