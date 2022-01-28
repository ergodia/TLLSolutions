# TLL Solutions

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


## Beschrijving baseline
Dit algoritme kiest eerst een random startpunt (startstaion). Vanuit dit station zal het algoritme gaan zoeken naar de kortste verbindingsmogelijkheid en daar naartoe gaan, tenzij deze al is bezocht. Dit zal het algoritme doen totdat er geen mogelijkheden meer zijn. Het probleem met dit algoritme is dat niet alle stations worden bezocht, omdat soms een station 'vast' komt te zitten tussen al bereden stations. Dit resulteert in een lage kwaliteit.

FIGUUR TOEVOEGEN VAN BASELINE RESULTAAT?

## Beschrijving 1e algoritme
Het eerste algoritme zal beginnen bij een station met maar 1 verbinding. Daarna zal het eerste algoritme, net als bij de baseline, gaan zoeken naar de kortste verbindingsmogelijkheid en daar naartoe gaan, tenzij deze al is bezocht. Allee stations meer dan 1 mogelijke verbinding mogen meerdere keren bezocht worden. Dit om te voorkomen dat sommige verbindingen niet worden bereden. Het algoritme geeft een correcte oplossing waarin alle verbindingen zijn bereden binnen het tijdframe van 3 uur en maximale aantal trajecten.

FIGUUR TOEVOEGEN VAN EERSTE ALGORITME RESULTAAT?

## Beschrijving 2e algoritme



## Gebruiksaanwijzing



