#Fermentation simulator

## 1 Beschrijving
### doel


## 2. uitvoering
1. Ik heb in eerste instantie een class gemaakt met waarin alle berekeningen worden uitgevoerd van de fermentaties. Vervolgens heb ik een eerste simulatie gerund en geplot in plotly. Hieruit kwam de volgende grafiek:
![plot](plots/newplot%20(3).png)

2. Het substraat lijkt nergens op, om te kijken of mijn berekeningen kloppen ga ik een paar unit tests uitvoeren.
```
at: 5 min 
 biomass: 0.5333333333333333
 substrate: 9.964444444444444
at: 10 min 
 biomass: 1.421166221166221
 substrate: 9.869812586177302
at: 15 min 
 biomass: 3.779407822300338
 substrate: 9.618955040551528
at: 20 min 
 biomass: 9.99632856351841
 substrate: 8.96121832300679
at: 25 min 
 biomass: 26.037063801248166
 substrate: 7.289990154985479
at: 30 min 
 biomass: 64.647741349031
 substrate: 3.4553133811777585
at: 35 min 
 biomass: 130.69443757305393
 substrate: -1.8855914278261579
at: 40 min 
 biomass: -67.1250724890925
 substrate: -5.949620226375755
at: 45 min 
 biomass: -1118.5156123216375
 substrate: 694.8297993510527
at: 50 min 
 biomass: -3894.8262924367705
 substrate: 1081.5297332193338
at: 55 min 
 biomass: -13587.083927471163
 substrate: 2433.98561233886
at: 60 min 
 biomass: -47485.15883389941
 substrate: 7172.766883397825
at: 65 min 
 biomass: -166115.36105058296
 substrate: 23772.731467414193
at: 70 min 
 biomass: -581316.4365064069
 substrate: 81892.15115048877
at: 75 min 
 biomass: -2034518.8011762698
 substrate: 285331.6100863494
at: 80 min 
 biomass: -7120726.676104219
 substrate: 997391.7999311703
at: 85 min 
 biomass: -24922454.124968104
 substrate: 3489624.7186771855
at: 90 min 
 biomass: -87228500.16411251
 substrate: 12212462.236842606
at: 95 min 
 biomass: -305299661.2921684
 substrate: 42742415.86655155
```
hieruit blijkt dat er geen rekening is gehouden met het geit dat het substraat op kan raken

3. nu een case toegevoegd waarbij de fermentatie ophoud als het substraat onder de 0 komt
```
at: 0 min 
 biomass: 0.2
 substrate: 10
at: 5 min 
 biomass: 0.5333333333333333
 substrate: 9.964444444444444
at: 10 min 
 biomass: 1.421166221166221
 substrate: 9.869812586177302
at: 15 min 
 biomass: 3.779407822300338
 substrate: 9.618955040551528
at: 20 min 
 biomass: 9.99632856351841
 substrate: 8.96121832300679
at: 25 min 
 biomass: 26.037063801248166
 substrate: 7.289990154985479
at: 30 min 
 biomass: 64.647741349031
 substrate: 3.4553133811777585
```
