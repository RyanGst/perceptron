import matplotlib.pyplot as plt
from sources.iris import X, y, plot_decision_regions, plot_original_data
from entities.perceptron import Perceptron

plot_original_data()

ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)


plt.show(block=False)
plt.pause(1)
plt.close()


plot_decision_regions(X, y, ppn)
