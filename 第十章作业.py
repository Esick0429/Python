# import copy
# class Car:
#     pass
# car1 = Car()
# car1.wheels = 4
# car2 = car1
# car2.wheels = 3
# print(car1.wheels)
# car3 = copy.copy(car1)
# car3.wheels = 6
# print(car1.wheels)

import pickle
favorites = ['游戏', '打游戏', '打游戏就完事了', '喜欢玩游戏']
f = open('favorites.dat', 'wb')
pickle.dump(favorites, f)
f.close()
import pickle
f = open('favorites.dat', 'rb')
favorites = pickle.load(f)
print(favorites)