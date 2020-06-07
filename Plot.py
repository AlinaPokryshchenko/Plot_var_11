import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(9, 9))
# Создаем категории
names = ["Кат 1", "Кат 2", "Кат 3"]
# Генерируем значения столбцов и ошибок
values0 = np.random.randint(1, 10, size=3)
err0 = np.random.sample(3)
values1 = np.random.randint(1, 10, size=3)
err1 = np.random.sample(3)
values2 = np.random.randint(1, 10, size=3)
err2 = np.random.sample(3)
values3 = np.random.randint(1, 10, size=3)
err3 = np.random.sample(3)
# Создаем графики
axs[0][0].bar(names, values0,
              yerr=err0,
              capsize=10,
              linewidth=2)
axs[0][1].bar(names, values1,
              yerr=err1,
              capsize=10,
              linewidth=2)
axs[1][0].bar(names, values2,
              yerr=err2,
              capsize=10,
              linewidth=2)
axs[1][1].bar(names, values3,
              yerr=err3,
              capsize=10,
              linewidth=2)
# Выводим графики
plt.show()
