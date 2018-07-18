import matplotlib.pyplot as plt


def plot(info):
    # Data to plot
    fig = plt.figure()
    labels = info.index
    # Plot
    patches, texts = plt.pie(info)
    plt.legend(patches, labels, loc="best")

    plt.axis('equal')
    plt.tight_layout()
    return fig
