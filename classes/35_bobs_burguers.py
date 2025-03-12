
class Restaurant:
    name = ''
    category = ''
    rating = 0.0
    delivery = False


bobs_burguers = Restaurant()

bobs_burguers.name = 'Bob\'s Burgers'
bobs_burguers.category = 'American Diner'
bobs_burguers.rating = 4.7
bobs_burguers.delivery = True

mc_donalds = Restaurant()

mc_donalds.name = 'Mc Donalds'
mc_donalds.category = 'Fast Food'
mc_donalds.rating = 5
mc_donalds.delivery = True

print(vars(bobs_burguers))
print(vars(mc_donalds))
