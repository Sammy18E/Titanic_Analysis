## Projekt: Titanic Analyse

### Beschreibung
Dieses Projekt führt eine **explorative Analyse der Passagierdaten der Titanic** durch.  
Der Fokus liegt auf der **Untersuchung der Überlebenswahrscheinlichkeiten** basierend auf verschiedenen demografischen Faktoren.  

Unsere Schwerpunkte sind:
- **Datenanalyse**: Untersuchung der Datenqualität und relevanter Merkmale  
- **Aggregation**: Zusammenführung und Berechnung relevanter Statistiken  
- **Visualisierung**: Darstellung der Ergebnisse durch Diagramme  

---

### **Ordnerstruktur**

```
Titanic_Analysis/
├── README.md                               # Projektbeschreibung mit einer Übersicht über das Projekt
│
├── main.ipynb                              # Main-Ausgabe der bereinigten Daten
│                                 
├── data/                                   # Enthält alle Daten für die Analyse  
│    ├── processed/                         # Vorverarbeitete Daten nach Bereinigung und Transformation  
│        ├──  
│    ├── titanic_kaggle
│         ├── gender_submission.csv
│         ├── test.csv
│         ├── train.csv
│
├── notebooks/                              # Jupyter Notebooks oder Python-Skripte für Analysen und Exploration  
│    ├── titanic_analysis.ipnyb             # Hauptskript für die Datenanalyse  
│    ├── ticket.ipynb
│    ├── korrelation_datenpunkte.ipynb
│
├── results/                                # Ergebnisse der Analysen, z. B. Diagramme und Berichte  
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
├── src/                                    # Enthält den eigentlichen Code des Projekts, z. B. Funktionen und Modelle  
│   ├── __pycache__
│         ├── datenvorbereitung.cpython-313.pyc
│         ├── utils.cpython-313.pyc
│         ├── visualisierungen.cpython-313.pyc
│
│   ├── datenvorbereitung.py                # Laden & Bereinigen der Hauptdaten von Seaborn Datensatz ("titanic")
│   ├── visualisierungen.py                 # Plots & Analysen
│   ├── utils.py                            # Hilfsfunktionen
│
├── tests/                                  # Tests für den Code, um sicherzustellen, dass alles korrekt funktioniert  
│    ├── maschine_learning_fully_commented.ipynb
│    ├── konfusionsmatrix_auswertung.txt
│
└── requirements.txt                        # Liste der benötigten Python-Bibliotheken für das Projekt 
```

### Hinweise für Nutzer
```
Die Anwendung wird durch titanic_analysis.py gestartet.
Alle Module befinden sich im src/-Verzeichnis.
Tests befinden sich im tests/-Verzeichnis und können mit pytest ausgeführt werden.
Installiere Abhängigkeiten mit pip install -r requirements.txt.
```
### **Autor**

#### [Titanic Busters]