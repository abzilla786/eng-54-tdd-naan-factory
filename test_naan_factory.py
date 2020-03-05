# import naan factory functions
# define and run tests
import run_naan_factory
from naan_factory_functions import *

#1
# as a user, i can use the make_dough with water and flour to make dough

print("calling make_dough with water and flour, expect 'dough' as a result")
print((make_dough('water', 'flour')) == 'dough')
print('got:', make_dough('water', 'flour'))

#2
# as a user, i can use the bake_dough with dough to get naan.
print("calling bake_dough with dough, expect 'naan' as a result")
print((bake_dough(make_dough, 'oven')) == 'naan')
print('got:', bake_dough(make_dough, 'oven'))

#3
# as a user, i can use the run_factory with water and flour and get naan
print("calling make dough with water and flour, calling bake_dough with make_dough and oven. expecting naan as a result")
print(run_naan_factory.naan_factory(make_dough('water', 'flour'), bake_dough(make_dough, 'oven') == 'naan'))
print('got', run_naan_factory.naan_factory(make_dough, bake_dough))
