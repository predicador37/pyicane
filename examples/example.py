# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from pyicane import pyicane


def main():
    census = pyicane.TimeSeries.get('census-series-1900-2001')
    data = census.data_as_dataframe()
    data.set_index(unicode('Año'))
    noja = data[data.index == unicode(' 39047 - Noja')]
    arnuero = data[data.index == unicode(' 39006 - Arnuero')]
    noja_plot = noja.plot()
    arnuero.plot(ax=noja_plot,
                 title='Population evolution in Noja vs Arnuero')
    plt.show()

if __name__ == '__main__':
    main()