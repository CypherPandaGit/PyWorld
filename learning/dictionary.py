my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(my_cat['size'])

print("My cat has {} fur.".format(my_cat['color']))

keys = {1234: 'password combination', 4322: 'luggage combo'}
print(keys.values())


picnic_items = {'apples': 5, 'cups': 2, 'napkins': 10}
print("I'm bringing {} to the picnic".format(str(picnic_items.get('napkins', 0))))

