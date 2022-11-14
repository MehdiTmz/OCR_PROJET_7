from itertools import combinations
import pandas as pd
import time as time

start = time.time()
def get_benefice(element):
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

df = pd.read_csv('data.csv', encoding = "ISO-8859-1")
benefice = []
price = []
share_list = []
df.columns = ('action','price','benefice')

for x in df['benefice']:
    x = x.replace("%", "")
    x = x.replace(",", ".")
    benefice.append(float(x))

for x in df['price']:
    price.append(float(x))

for x in range(len(benefice)):
    share_list.append([price[x],benefice[x]])

n = 0
list_of_valable_composition = []
for i in range(len(share_list)):
    list_of_combination = combinations(share_list, i +1)
    for j in list_of_combination:
        if calculate_price(j) < 500:
            list_of_valable_composition.append([j, calculate_price(j), calculate_benefice(j)])
        n += 1

# for x in list_of_valable_composition:
#     print(x)
list_of_valable_composition.sort(key=get_benefice, reverse=True)

print(list_of_valable_composition[0])

end = time.time()

print("Le temps d'éxecutuion est de ", end-start)