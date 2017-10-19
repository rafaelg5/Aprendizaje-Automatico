money = float(input())

bills = [100, 50, 20, 10, 5, 2]
coins = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

used_bills = [0] * 6
used_coins = [0] * 6

for i, item in enumerate(bills):

 if item > money:
  continue

 quot = money // item
 used_bills[i] = int(quot)
 money = money - item * quot

for i, item in enumerate(coins):

 if item > money:
  continue

 quot = money // item
 used_coins[i] = int(quot)
 money = money - item * quot

print('\nNOTAS:')
for i, j in zip(used_bills, bills):
 print('{0} nota(s) de R$ {1:.2f}'.format(i, j))

print('\nMOEDAS:')
for i, j in zip(used_coins, coins):
 print('{0} moeda(s) de R$ {1:.2f}'.format(i, j))
