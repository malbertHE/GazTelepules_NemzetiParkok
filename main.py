import pandas as pan
import matplotlib.pyplot as plot
from matplotlib.pyplot import figure

gazellatas = pan.read_excel('./data/2_3_9i.xls', sheet_name = '2.3.9.', skiprows = [0, 1])
gazellatas = gazellatas.drop(gazellatas.columns[[1, 3, 4, 5, 6]], axis = 1)
gazellatas = gazellatas.rename(index = str, columns = {gazellatas.columns[0]: 'evszam', gazellatas.columns[1]: 'gaz'})