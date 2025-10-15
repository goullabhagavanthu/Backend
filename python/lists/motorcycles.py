motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
motorcycles.insert(0, 'ducati')
del motorcycles[4]
print(motorcycles)

last_owned = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {last_owned.title()}.")