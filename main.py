import pandas as pan
import matplotlib.pyplot as plot
from matplotlib.pyplot import figure

gazellatas = pan.read_excel('./data/2_3_9i.xls', sheet_name = '2.3.9.', skiprows = [0, 1])
gazellatas = gazellatas.drop(gazellatas.columns[[1, 3, 4, 5, 6]], axis = 1)
gazellatas = gazellatas.rename(index = str, columns = {gazellatas.columns[0]: 'evszam', gazellatas.columns[1]: 'gaz'})

elhagyandoSorok = []
for i in range(0, 20) :
    elhagyandoSorok.append(i)
for i in range(36, 55) :
    elhagyandoSorok.append(i)
nemzetipark = pan.read_excel('./data/5_2_2i.xls', sheet_name = '5.2.2.', skiprows = elhagyandoSorok)
nemzetipark = nemzetipark.drop(nemzetipark.columns[[2, 3, 4, 5, 6, 7]], axis = 1)
nemzetipark = nemzetipark.rename(index = str, columns = {nemzetipark.columns[0]: 'evszam', nemzetipark.columns[1]: 'nemzetiParkTerulet'})

mindenAdat = pan.merge(gazellatas, nemzetipark, on='evszam', how="outer")
mindenAdat = pan.DataFrame({'Gazellatas': mindenAdat['gaz'], 'Nemzeti park terulet': mindenAdat['nemzetiParkTerulet']})

korrelaciosMatrix = mindenAdat.corr()

figure(num = None, figsize = (13, 9), dpi = 80, facecolor = 'w', edgecolor = 'k')
plot.clf()
plot.xlabel('Evszam')
plot.ylabel('Vezetekes gazzal ellatott telepulesek aranya [%]')
plot.plot(gazellatas['evszam'], gazellatas['gaz'])
plot.show()

figure(num = None, figsize = (13, 9), dpi = 80, facecolor = 'w', edgecolor = 'k')
plot.clf()
plot.xlabel('Evszam')
plot.ylabel('Nemzeti parkok terulete [ezer hektarban]')
plot.plot(nemzetipark['evszam'], nemzetipark['nemzetiParkTerulet'])
plot.show()

print(korrelaciosMatrix)
figure(num = None, figsize = (13, 9), dpi = 160, facecolor = 'w', edgecolor = 'k')
plot.clf()
plot.imshow(korrelaciosMatrix)
plot.colorbar()
plot.show()
