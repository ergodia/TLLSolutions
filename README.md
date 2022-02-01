# TLL Solutions
Datum: 2 februari, 2022

Opleiding: Minor Programmeren

Vak: Programmeertheorie

Studenten: Tim Mulder, Lieneke Floor - Barsukoff Poniatowsky & Luca Nederhorst

Begeleiders: Joos & Charlotte

![Voorbeeld project](data/Images/Graph_Nationaal_eerste_algoritme.png)


**Doel van dit project:** het maken van de lijnvoering van intercitytreinen in Nederland met een hoge kwaliteit. Binnen het gegeven tijdsframe van 3 uur worden er een aantal trajecten uitgezet. Het maximaal toegelaten aantal trajecten is 20. Een traject is een route van sporen en stations waarover treinen heen en weer rijden. Een traject mag niet langer zijn dan het opgegeven tijdsframe.

**Voorbeeld:** Het traject [Castricum , Zaandam , Hoorn , Alkmaar] is een traject met een duur van 59 minuten, en zou dus binnen het tijdsframe passen.

## Belangrijke begrippen
- **Traject**: *Trein X: Amsterdam Centraal -> Amsterdam Sloterdijk -> Haarlem --> Leiden Centraal* 
- **Verbinding**: *treinstation A -> treinstation B*
- **Reistijden** in minuten van de verbindingen: *verbinding van Amsterdam Centraal en Amsterdam Centraal heeft reistijd van 6 minuten*
- **Locaties**: *x -en y-coördinaten van de verschillende stations*
- **Lijnvoering**: *alle trajecten samen*
- **Kwaliteit (K)**: p*10000 - (T*100 + Min). Waarbij p de fractie bereden verbinding is van de totale verbindingen, T het aantal trajecten in de lijnvoering en Min het totaal aantal minuten van de lijnvoering
- **Baseline**: *algoritme implementeren dat willekeurige oplossing genereerd (nog niet de beste oplossing)*


## Beschrijving baseline (codes/algorithms/baseline.py)
Dit algoritme kiest eerst een random startpunt (startstaion). Vanuit dit station zal het algoritme gaan zoeken naar de kortste verbindingsmogelijkheid en daar naartoe gaan, tenzij deze al is bezocht. Dit zal het algoritme doen totdat er geen mogelijkheden meer zijn. Het probleem met dit algoritme is dat niet alle stations worden bezocht, omdat soms een station 'vast' komt te zitten tussen al bereden stations. Dit resulteert in een lage kwaliteit.


## Beschrijving traveling salesman algoritme 
De code van het traveling salesman algoritme is te vinden in codes/algorithms/traveling_salesman_rail.py. Het algoritme zal beginnen bij een station met maar 1 verbinding. Daarna zal het algoritme, net als bij de baseline, gaan zoeken naar de kortste verbindingsmogelijkheid en daar naartoe gaan, tenzij deze al is bezocht. Allee stations meer dan 1 mogelijke verbinding mogen meerdere keren bezocht worden. Dit om te voorkomen dat sommige verbindingen niet worden bereden. Het algoritme geeft een correcte oplossing waarin alle verbindingen zijn bereden binnen het tijdframe van 3 uur en maximale aantal trajecten.

<img src="data/Images/traveling_salesman_flowchart.png" width="750">


## Beschrijving simulated annealing algoritme (codes/algorithms/simulated_annealing.py)
De code van het simulated salesman algoritme is te vinden in codes/algorithms/simulated_annealing.py. In dit algoritme wordt de eindlijnvoering van het 1e algoritme (traveling salesman algoritme) gebruikt als beginpunt. Daarna zal het kortste traject - trajecten korter dan 3 stations - proberen te worden bijgevoegd bij een ander traject. Dit om het aantal (korte) trajecten terug te dringen, en hiermee het totaal aantal trajecten te verminderen. Dit zal moeten resulteren in een hogere kwaliteit lijnvoering.

<img src="data/Images/simulated_annealing_flowchart.png" width="750">


## Gebruiksaanwijzing
TODO


## Projectstructuur
Het programma bestaat uit meerdere folders waarin verschillende aspecten van het project te vinden zijn. De folder 'codes' omvat alle code. Deze folder is ook weer onderverdeeld in verschillende typen code. De 'algorithms' folder omvat de verschillende algoritmes die de lijnvoeringen genereren, 'classes' omvat alle objecten die nodig zijn voor het project (bijv. stations, mogelijke verbindingen en nodes). Verder is er ook nog de trials folder waarin overige code, zoals de berekening van de kwaliteit of of berekening van de state-space, zijn opgeslagen. 
De folder 'data' omvat alle input- en outputfiles die worden gebruikt en worden gegeneert door het programma. 

