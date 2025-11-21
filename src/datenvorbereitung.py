import pandas as pd
import seaborn as sns

def lade_titanic_daten():
    """Lädt den Titanic-Datensatz von Seaborn und gibt ihn als Pandas DataFrame zurück."""
    df = sns.load_dataset("titanic")
    return df.copy()

def bereinige_daten(df):
    """
    Bereinigt den Titanic-Datensatz:
    - Entfernt unnötige Spalten
    - Füllt fehlende Werte auf
    - Konvertiert kategorische Variablen
    """
    df_bereinigt = df.copy()
    
    # Entferne nicht relevante oder redundante Spalten
    drop_columns = ["embarked", "alive", "deck", "class", "sex", "adult_male", "alone"]
    df_bereinigt = df_bereinigt.drop(columns=drop_columns, errors="ignore")
    
    # Fehlende Werte ersetzen (ohne inplace=True)
    df_bereinigt["age"] = df_bereinigt["age"].fillna(df_bereinigt["age"].median())
    df_bereinigt["fare"] = df_bereinigt["fare"].fillna(df_bereinigt["fare"].median())
    df_bereinigt["embark_town"] = df_bereinigt["embark_town"].fillna(df_bereinigt["embark_town"].mode()[0])
    
    return df_bereinigt

def vergleiche_daten(original, bereinigt):
    """
    Vergleicht Original- und bereinigte Daten und gibt die Unterschiede aus.
    """
    entfernte_spalten = set(original.columns) - set(bereinigt.columns)
    fehlende_vorher = original.isnull().sum()[original.isnull().sum() > 0]
    fehlende_nachher = bereinigt.isnull().sum()[bereinigt.isnull().sum() > 0]

    return {
        "Entfernte Spalten": entfernte_spalten,
        "Fehlende Werte vorher": fehlende_vorher,
        "Fehlende Werte nachher": fehlende_nachher
    }



