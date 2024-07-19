#This code shows how to visualize the data from 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn import cluster
from sklearn import datasets
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
#from sklearn.cluster import HDBSCAN 
#this one isn't working because this is the recent one and there is no 
# compatability with colab 
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

n_samples = 500

# penguins : this is a real dataset, so we will load it and select a useful set of
#            features.  We will also store the labels.
penguins = sns.load_dataset("penguins").dropna(
    axis=0, subset=["bill_length_mm", "flipper_length_mm"]
)
penguins_encoder = LabelEncoder().fit(penguins["species"].values)
penguins_classes = penguins_encoder.classes_
penguins_labels = penguins_encoder.transform(penguins["species"].values)
penguins = penguins[["bill_length_mm", "flipper_length_mm"]].values
penguins = StandardScaler().fit_transform(penguins)

# moons : two crescent "moon" shapes, with one inverted so that there is no way to
# linearly separate the two groups, but they are visually separate.
moons, moons_labels = datasets.make_moons(n_samples=n_samples, noise=0.065)
moons = StandardScaler().fit_transform(moons)

# circles : two concentric rings, representing noisy values that are in one of two
# groups, assigned by the radius of the ring in which the sample is located.
circles, circles_labels = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.065
)
circles = StandardScaler().fit_transform(circles)

# density blobs : three "blobs" with widely varying density and size characteristics.
# The blobs overlap so that they are not perfectly visually separable.
density_blobs, density_blobs_labels = datasets.make_blobs(
    n_samples=n_samples, cluster_std=[1.9, 0.5, 2.7], random_state=4
)
density_blobs = StandardScaler().fit_transform(density_blobs)

def plot_all(data_list, names=None, label_list=None, style_list=None):
    """
    Plot scatterplots for all the 2-D datasets in `data_list`.
    `names` provide a title for each plot
    `label_list` is a list of label assignments for the samples in the data list.
    `style_list` is a list of marker shape assignments for the samples in the data list.
    """
    nrows = int(round(len(data_list) / 2, 0))
    fig, axs = plt.subplots(nrows=nrows, ncols=2, figsize=(12, 10))
    for r in range(nrows):
        for c in range(2):
            hue = label_list[r * 2 + c] if label_list is not None else None
            style = style_list[r * 2 + c] if style_list is not None else None
            title = names[r * 2 + c] if names is not None else None
            sns.scatterplot(
                x=data_list[r * 2 + c][:, 0],
                y=data_list[r * 2 + c][:, 1],
                hue=hue,
                style=style,
                palette=sns.color_palette(n_colors=len(set(hue))),
                legend=False,
                ax=axs[r, c],
            ).set(title=title)
    plt.subplots_adjust(wspace=0.50)
    plt.show()
    
#plot the all clustering examples. 
plot_all(
    [penguins, moons, circles, density_blobs],
    ["Penguins", "Moons", "Circles", "Density Blobs"],
    [penguins_labels, moons_labels, circles_labels, density_blobs_labels],
)

