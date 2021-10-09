"""
test Classe Plotter
"""
import Classi.Plotter

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

p = Classi.Plotter.Plotter()

print("retcode load: ", p.load_axis(x, y))

p.plot_setting(True, True, 'Prova titolo', 'Label X', 'Label Y', 'Linea 1')


x2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("retcode load: ", p.load_axis(x2, y2))

p.plot_setting(False, True, 'Prova titolo2', 'Label X2', 'Label Y2', 'Linea 2')

p.show_graph()
