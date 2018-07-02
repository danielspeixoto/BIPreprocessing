import matplotlib.pyplot as plt


def plot(info):
    # Data to plot
    labels = info.index
    # Plot
    patches, texts = plt.pie(info)
    plt.legend(patches, labels, loc="best")

    plt.axis('equal')
    plt.tight_layout()
    plt.figure()