from math import log
import matplotlib.pyplot as plt

for numofR in range(2, 16):
    analysisList = eval(f"list({open(f'data_{numofR}', 'r').read()})")

    plt.hist([log(i[1][0]/i[1][1], numofR) for i in analysisList],
             bins=numofR*10, color='blue')
    plt.title(f"Synthetic Resistance (N={numofR}, sample={len(analysisList)})")

    plt.savefig(f"hist{numofR}_log.svg")

    print(f"{numofR} Done.")
