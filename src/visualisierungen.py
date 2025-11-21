# Visualisierungen
import matplotlib.pyplot as plt
import seaborn as sns

def plot_alter_klasse(df_bereinigt):
    """Zeigt die Verteilung von Alter nach Klasse als Boxplot."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='pclass', y='age', data=df_bereinigt, palette='YlGnBu')
    plt.xlabel('Passagierklasse')
    plt.ylabel('Alter')
    plt.title('Alter vs. Klasse')
    plt.savefig(r'C:\Users\Admin\Documents\Woche_16_10.03.25-14.03.25\10.03.25\titanic_analysis\results\age_pclass.png')

def plot_ueberlebensrate(df_bereinigt):
    """Zeigt die Überlebensrate nach Klasse als Balkendiagramm."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='pclass', y='survived', data=df_bereinigt, palette='YlGnBu')
    plt.xlabel('Passagierklasse')
    plt.ylabel('Überlebensrate')
    plt.title('Überlebensrate nach Klasse')
    plt.show()