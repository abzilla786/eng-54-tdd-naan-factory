# import naan factory functions
# define and run tests


from naan_factory_functions import *

print("calling make_dough with water and flour, expect 'dough' as a result")
print((make_dough('water', 'flour')) == 'dough')
print('got:', make_dough('water', 'flour'))
