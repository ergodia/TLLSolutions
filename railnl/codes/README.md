# Codes

De folder **codes** is onderverdeeld in algoritmes, analyse, berekeningen, classes en hulp-files.

In onderstaande uitleg wordt een beschrijving van de inhoud per folder gegeven.

*TSP = Traveling Salesman Problem*

*SA = Simulated Annealing*

## algorithms
### Folder met files met algoritmes om een lijnvoering te maken:

- `baseline.py` is file waar een algoritme gebaseerd op het TSP instaat, met als uitgangspunt een random beginpunt.
- `simulated_annealing.py` is een file waarin je het SA algoritme kan runnen.
- `traveling_salesman_rail.py` is een file waarin je een algoritme gebaseerd op het TSP algoritme kan runnen.

## analyze
### Folder met files om de algoritmes te testen:

- `simulated_annealing_dis.py` genereerd een score een x-aantal keer op basis van het SA algoritme, per score wordt er een grafiek gemaakt.
- `traveling_salesman_dis.py` bevat het experiment voor het TSP algoritme, en retourneerd de hoogste score.

## calculations

### Folder met files waarin de state-space en de kwaliteit van de lijnvoerig kan worden berekend:

- `calculations_statespace.py` bevat de verschillende formules om de state-space te berekenen.
- `line_quality.py` berekent de kwaliteit van de lijnvoering.


## help_classes
### Folder met files met classes die stations inladen en knooppunten verbinden:

- `graph.py` is een file om een graaf te maken met alle verbindingen
- `network.py` is een hulp class voor SA (gevulde graaf met trajecten)
- `nodes.py` bevat de knooppunten die zich in de graf bevinden
- `stations.py` laad het station bestand in voor de grafieken

## help_functions
### Folder met files om afstandtabel en visualisatie te maken:

- `distance_table.py` maakt een afstandstabel waarin de connecties goed af te lezen zijn
- `visualize_graph.py` maakt een visualisatie van alle trajecten op de kaart van Nederland
