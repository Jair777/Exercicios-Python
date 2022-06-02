N = int(input())
v100 = N // 100
v50 = N % 100 // 50
v20 = N % 100 % 50 // 20
v10 = N % 100 % 50 % 20 // 10
v5 = N % 100 % 50 % 20 % 10 // 5
v2 = N % 100 % 50 % 20 % 10 % 5 // 2
v1 = N % 100 % 50 % 20 % 10 % 5 % 2 // 1
print(f'{v100} nota(s) de R$ 100')
print(f'{v50} nota(s) de R$ 50')
print(f'{v20} nota(s) de R$ 20')
print(f'{v10} nota(s) de R$ 10')
print(f'{v5} nota(s) de R$ 5')
print(f'{v2} nota(s) de R$ 2')
print(f'{v1} nota(s) de R$ 1', end='')



