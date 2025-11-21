## Projekt: Titanic Analyse

### Beschreibung
Dieses Projekt führt eine **explorative Analyse der Passagierdaten der Titanic** durch.  
Der Fokus liegt auf der **Untersuchung der Überlebenswahrscheinlichkeiten** basierend auf verschiedenen demografischen Faktoren.  

Unsere Schwerpunkte sind:
- **Datenanalyse**: Untersuchung der Datenqualität und relevanter Merkmale  
- **Aggregation**: Zusammenführung und Berechnung relevanter Statistiken  
- **Visualisierung**: Darstellung der Ergebnisse durch Diagramme  

---

Das Projekt besteht aus mehreren Notebooks.  
**Mein eigener Schwerpunkt liegt auf dem Notebook `hafen_analyse_sammy.ipynb`.**

---

## Mein Beitrag (Notebook: `hafen_analyse_sammy.ipynb`)

Ich habe eine umfassende Analyse zu **Einstiegshäfen (Embarked)** durchgeführt und **12 Visualisierungen** erstellt.  
Diese untersuchen folgende Fragestellungen:

### **Datenanalysen & Visualisierungen**
- Überlebende nach Einstiegshafen  
- Überlebensrate nach Einstiegshafen und Geschlecht  
- Überlebensrate nach Geschlecht in *Cherbourg, Queenstown und Southampton*  
- Überlebende nach Einstiegshafen und Geschlecht  
- Überlebende nach Einstiegshafen (Mann, Frau, Kind)  
- Überlebensrate nach Passagieren in *Cherbourg, Queenstown und Southampton*  
- Überlebende nach Einstiegshafen und Klasse  
- Überlebensrate nach Klasse in *Cherbourg, Queenstown und Southampton*  
- Überlebende nach Einstiegshafen und Altersgruppen  
- Überlebensrate nach Einstiegshafen und Altersgruppen  
- Überlebensrate nach Altersgruppe in *Cherbourg, Queenstown und Southampton*

### **Verwendete Diagrammtypen**
- Säulendiagramme  
- Balkendiagramme  
- Kreisdiagramme  
- Scatterplots  

---

### **Ordnerstruktur**

```
Titanic_Analysis/
├── README.md                                     # Projektbeschreibung mit einer Übersicht über das Projekt
│
├── main.ipynb                                    # Haupt-Notebook mit der finalen Analyse und Ergebnissen
│                                 
├── data/                                         # Enthält alle Daten für die Analyse  
│    ├── processed/                               # Bereinigte & transformierte Daten   
│    ├── titanic_kaggle                           # Original-Kaggle-Datensätze 
│         ├── gender_submission.csv               # Beispiel-Submission für Kaggle-Wettbewerb
│         ├── test.csv                            # Test-Daten ohne Überlebenslabel  
│         ├── train.csv                           # Trainingsdaten mit Überlebenslabel
│
├── notebooks/                                    # Jupyter Notebooks oder Python-Skripte für Analysen und Exploration
│    ├── hafen_analyse_sammy.ipynb                # Analyse der Überlebensraten nach Einstiegshafen (Embarked) inkl. 12 Visualisierungen
│    ├── titanic_analysis.ipnyb                   # Hauptskript für die Datenanalyse (Team)
│    ├── ticket.ipynb                             # Analyse von Ticket-Daten  
│    ├── korrelation_datenpunkte.ipynb            # Untersuchung der Korrelationen zwischen Features
│
├── results/                                      # Ergebnisse der Analysen, z. B. Diagramme und Berichte  
│    ├── age_pclass.png
│    ├── correlation_heatmap.png
│    ├── family_alone.png
│    ├── family_sibsp.png
│    ├── survival_by_embark_town.png
│    ├── survival_by_embarked_age_group.png
│    ├── survival_passenger_with_family.png
│    ├── survival_rate_by_age.png
│    ├── survival_rate_by_class.png
│    ├── survival_rate_by_gender.png
│    ├── Ueberlebende_nach_Passagierklassen_1_Anzahl.png
│    ├── Ueberlebende_nach_Passagierklassen_2-Anteil.png
│    ├── ticket_summary_filtered.csv
│    ├── ticket_summary.csv
│
├── src/                                          # Quellcode für Datenverarbeitung & Modellierung  
│   ├── __pycache__                               # Zwischengespeicherte kompilierte Python-Dateien 
│   ├── datenvorbereitung.py                      # Laden & Bereinigen der Hauptdaten von Seaborn Datensatz ("titanic")
│   ├── visualisierungen.py                       # Plots & Analysen
│   ├── utils.py                                  # Hilfsfunktionen
│
├── tests/                                        # Test-Skripte zur Validierung der Analysen   
│    ├── maschine_learning_fully_commented.ipynb  # Dokumentierte ML-Analyse 
│    ├── konfusionsmatrix_auswertung.txt          # Bewertung der Konfusionsmatrix 
│
└── requirements.txt                              # Liste der benötigten Python-Bibliotheken für das Projekt 
```

---

## Technologien & Bibliotheken
- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## Verwendung  
- Hauptanalyse: `titanic_analysis.ipynb`  
- Meine Analyse: `notebooks/hafen_analyse_sammy.ipynb`  
- Zusätzliche Funktionen im Ordner `src/`  
- Tests im Ordner `tests/`

---

## Ziel des Projekts  
Datenanalyse üben, Visualisierungen erstellen und Verständnis für Zusammenhänge zwischen  
- Hafen  
- Geschlecht  
- Alter  
- Klasse  
- Überlebenswahrscheinlichkeit  
gewinnen.
