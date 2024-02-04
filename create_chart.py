import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.patches import FancyBboxPatch


def get_probabilities() -> np.ndarray:
    """
    gets the probabilities of each possible solution when rolling two dice simultaneously
    """
    arr = np.ravel(
        np.array([[i + j for j in range(1, 7)] for i in range(1, 7)])
    )
    counted = Counter(arr)
    data = np.array(
        [round(counted[i] / 36 * 100, 2) for i in list(range(2, 13))]  #
    )
    return data


def rescale(arr: np.ndarray):
    """
    rescaler for any numpy-supported array
    """
    return (arr - arr.min()) / (arr.max() - arr.min())


def plot_data(data: np.ndarray,
              title: list[str]):
    """
    creates a barchart with rounded edges
    """
    # create figure and plot
    _, ax = plt.subplots(
        figsize=(16, 9),
        dpi=200
    )
    bar_plot = ax.bar(
        x=range(2, 13),
        height=data,
        width=.6,
        color=plt.get_cmap('YlOrRd')(rescale(data))  # set bars to different colors depending on their values
    )
    # create annotations
    ax.set_yticks([])
    ax.set_xticks(list(range(2, 13)))
    ax.bar_label(
        container=bar_plot,
        labels=[f'{value}%' for value in data],
        label_type='center'
    )
    ax.bar_label(
        container=bar_plot,
        labels=title,
        label_type='edge',
        padding=17.5,
        fontweight='bold',
        fontsize='x-large'
    )
    for spine in ax.spines:
        ax.spines[spine].set_visible(False)
    # create rounded corners
    new_patches = []
    for patch in reversed(ax.patches):
        bounding_box = patch.get_bbox()
        color = patch.get_facecolor()
        new_patch = FancyBboxPatch(
            xy=(bounding_box.xmin, bounding_box.ymin),
            width=abs(bounding_box.width),
            height=abs(bounding_box.height),
            boxstyle='round, pad=.1, rounding_size=0',
            edgecolor='none',
            facecolor=color,
            mutation_aspect=2
        )
        new_patches.append(new_patch)
    for patch in new_patches:
        ax.add_patch(patch)
    plt.show()


def main():
    title = [
        'the',
        'probability',
        'for',
        'each',
        'possible',
        'result',
        'when',
        'rolling',
        'two',
        'dice',
        'simulta\n-neously'
    ]
    data = get_probabilities()
    plot_data(data, title)


if __name__ == '__main__':
    main()
