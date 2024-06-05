# create a dictionary to store information about fruits
fruit_info = {'apple': {'color': 'red', 'price': 0.50},
              'banana': {'color': 'yellow', 'price': 0.25},
              'orange': {'color': 'orange', 'price': 0.30}}

# add a new fruit to the dictionary
fruit_info['pear'] = {'color': 'green', 'price': 0.40}

# access information about a specific fruit
print(fruit_info['apple']['color'])  # output: red
print(fruit_info['banana']['price'])  # output: 0.25

# loop over all the keys in the dictionary
for fruit in fruit_info.keys():
    print(fruit, fruit_info[fruit]['price'])

# output:
# apple 0.5
# banana 0.25
# orange 0.3
# pear 0.4