fruit_info = {'apple': {'color': 'red', 'price': 0.50},
              'banana': {'color': 'yellow', 'price': 0.25},
              'orange': {'color': 'orange', 'price': 0.30}}

# add a new fruit to the dictionary
fruit_info['pear'] = {'color': 'green', 'price': 0.40}


print(fruit_info['apple']['color']) 
print(fruit_info['banana']['price']) 


for fruit in fruit_info.keys():
    print(fruit, fruit_info[fruit]['price'])


