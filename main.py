from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde")
sns.displot(random.binomial(n=10, p=0.5, size=1000))
sns.displot(random.poisson(lam=2, size=1000))

plt.show()
