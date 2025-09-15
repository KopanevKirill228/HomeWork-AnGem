import numpy
from matplotlib import pyplot as plt
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8)) #полярная система
alpha = numpy.linspace(0, 2 * numpy.pi, 10000) #полный круг вариантов угла
parametr = 6
#кардиоида
r = (1 + numpy.cos(alpha)) * 2 * parametr #все варианты r для кардиоиды
ax.plot(alpha, r, 'b-', linewidth=4) #отрисовка кардиоиды


#лемниската
r1 = numpy.sqrt(2 * numpy.sin(alpha * 2)) * parametr
r2 = numpy.sqrt(2 * numpy.cos(alpha * 2)) * parametr
ax.plot(alpha, r1, 'y-', linewidth=4) #отрисовка лемнискаты повернутой на 45 градусов
ax.plot(alpha, r2, 'r-', linewidth=4) #отрисовка лемнискаты

plt.show()




