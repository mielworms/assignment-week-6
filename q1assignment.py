inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
#add key 
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
#sort list alphabetically
inventory['backpack'].sort()
#remove dagger
inventory['backpack'].remove('dagger')
#add 50 to 'gold' 
inventory['gold'] += 50
print(inventory)