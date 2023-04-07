import matplotlib.pyplot as plt
from animation import Animation

animation = Animation()

N = 100
X = range(N)
Y = list(map(lambda _: _**2, X))

for i in range(N):
    print('+', end='', flush=True)

    fig, ax = plt.subplots(1, 1, figsize=(4, 4))
    ax.plot(X[:i], Y[:i])
    ax.set_xlim(X[0], X[-1])
    ax.set_ylim(Y[0], Y[-1])
    ax.grid(ls=':')
    
    plt.tight_layout()
    animation.add_figure()
    plt.close()
    plt.clf()

print()
print("Exporting ... ", end='', flush=True)
animation.export("./foo.gif")
print("done.")