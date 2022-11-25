from itertools import combinations
import pandas as pd
import time as time

start = time.time()

def get_benefice(element):
    return element[1]

def get_ratio(element):
    return element[2]

def calculate_price(action_list):
    MAX_COST = 500
    action_sum = 0
    for action in action_list:
        action_sum += action[0]

    return action_sum

def calculate_benefice(action_list):
    benefice_sum = 0
    for action in action_list:
        benefice_sum += (action[0]*action[1])/100

    return benefice_sum
def simple_benefice(price, benefice):
    return (price*benefice)/100

df = pd.read_csv('dataset1.csv', encoding = "ISO-8859-1")
benefice = []
price = []
share_list = []
df.columns = ('action','price','benefice')
df = df[df['price']>0]
print(df)
for x in df['benefice']:
    # x = x.replace("%", "")
    # x = x.replace(",", ".")
    x = float(x)/100
    benefice.append(x)

for x in df['price']:
    price.append(int(100*x))

# for x in range(len(benefice)):
#     share_list.append([price[x], simple_benefice(price[x],benefice[x]), benefice[x]/100])
print(price)
for x in range(len(price)):
    benefice[x] = (price[x]/100)*benefice[x]

share_list = [price,benefice]

def printknapSack(W, wt, val, n):
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]           
    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # stores the result of Knapsack
    res = K[n][W]
    print(res)

    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:

            # This item is included.
            print(wt[i - 1])         

            res = res - val[i - 1]
            w = w - wt[i - 1]

val = share_list[1]
wt = share_list[0]
W = 500
n = len(val)
printknapSack(W, wt, val, n)
end = time.time()

print('Time = ', end-start)
# This code is contributed by Aryan Garg.

