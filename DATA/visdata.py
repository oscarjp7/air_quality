import matplotlib.colors as colors
import numpy as np
import matplotlib.pyplot as plt

def plot_year_data(ax, data, boroughs, year_column, cmap, norm, pollutant):
    boroughs.plot(ax=ax, color='white', edgecolor='black')
    data.plot(column=year_column, ax=ax, legend=True, cmap=cmap, markersize=5, norm=norm)
    ax.set_title(f'{pollutant}(µg/m3) Concentration in London - {year_column.split("_")[0]}')

def plot_pollutant_borough(joined_data, boroughs, pollutant):
    fig, axs = plt.subplots(1, 3, figsize=(20, 10), sharex=True, sharey=True)
    cmap = plt.cm.OrRd
    norm = colors.BoundaryNorm(boundaries=np.arange(joined_data[['2013_data', '2016_data', '2019_data']].min().min(),45, 0.5).tolist()
                        + np.arange(50, joined_data[['2013_data', '2016_data', '2019_data']].max().max(), 10).tolist(), ncolors=cmap.N, clip=True)
    plot_year_data(axs[0], joined_data, boroughs, '2013_data', cmap, norm, pollutant)
    plot_year_data(axs[1], joined_data, boroughs, '2016_data', cmap, norm, pollutant)
    plot_year_data(axs[2], joined_data, boroughs, '2019_data', cmap, norm, pollutant)
    plt.tight_layout()
    plt.show()

def plot_year_data_2(ax, data, year_column, cmap, norm, pollutant):
    data.plot(column=year_column, ax=ax, legend=True, cmap=cmap, markersize=2, norm=norm)
    ax.set_title(f'{pollutant}(µg/m3) Concentration in London - {year_column.split("_")[0]}')
    ax.set_axis_off()

def plot_pollutant_data(joined_data, pollutant):
    fig, axs = plt.subplots(1, 3, figsize=(20, 10), sharex=True, sharey=True)
    cmap = plt.cm.OrRd
    norm = colors.Normalize(
        vmin=joined_data[['2013_data', '2016_data', '2019_data']].min().min(),
        vmax=joined_data[['2013_data', '2016_data', '2019_data']].max().max()
    )
    plot_year_data_2(axs[0], joined_data, '2013_data', cmap, norm, pollutant)
    plot_year_data_2(axs[1], joined_data, '2016_data', cmap, norm, pollutant)
    plot_year_data_2(axs[2], joined_data, '2019_data', cmap, norm, pollutant)
    plt.tight_layout()
    plt.show()
