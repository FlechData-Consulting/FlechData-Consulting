
import requests
import pandas as pd
from io import StringIO
import seaborn as sns
from matplotlib import pyplot as plt
import os
import git

#GitHub-Zugangsjeton
headers = {'Authorization': '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'}

# GitHub-URL für öffentliche Repositorien
url = 'https://api.github.com/repositories'

response = requests.get(url, headers=headers)
data = response.json()

# Liste der URLs der CSV-Dateien auf GitHub
csv_urls = [
    'https://raw.githubusercontent.com/FlechData-Consulting/FlechData-Consulting/main/ProjectIU/data/Athletes.csv',
    'https://raw.githubusercontent.com/FlechData-Consulting/FlechData-Consulting/main/ProjectIU/data/Coaches.csv',
    'https://raw.githubusercontent.com/FlechData-Consulting/FlechData-Consulting/main/ProjectIU/data/EntriesGender.csv',
    'https://raw.githubusercontent.com/FlechData-Consulting/FlechData-Consulting/main/ProjectIU/data/Medals.csv',
    'https://raw.githubusercontent.com/FlechData-Consulting/FlechData-Consulting/main/ProjectIU/data/Teams.csv'
    # Ajoutez d'autres URL au besoin
]

# Initialisiere ein Dictionary, um die DataFrames zu speichern, die jeder CSV-Datei entsprechen.
data_frames = {}

for csv_url in csv_urls:
    response = requests.get(csv_url)

    if response.status_code == 200:
        file_name = csv_url.split("/")[-1]

        try:
            # Verwenden Sie on_bad_lines=True, um falsch formatierte Zeilen zu überspringen.
            df = pd.read_csv(StringIO(response.text), sep=';', on_bad_lines='skip')
            data_frames[file_name] = df
        except pd.errors.ParserError as e:
            print(f"Erreur lors de la lecture du fichier CSV {file_name}: {e}")
    else:
        print(f"Fehler beim Abrufen der CSV-Datei{csv_url}. Fehlercode: {response.status_code}")

############################################# Athletes###################################################

# DataFrames
if 'Athletes.csv' in data_frames:
    Athletes = data_frames['Athletes.csv']
    print(Athletes.head())

# Benennen Sie beide Spalten gleichzeitig um
nouveaux_noms = {'Name': 'PersonName', 'NOC': 'Country'}
Athletes.rename(columns=nouveaux_noms, inplace=True)

print(Athletes.head(5))

# Erstellen Sie eine Pivot-Tabelle, um die Anzahl der Personen pro Land in jeder Disziplin zu zählen.
pivot_table = pd.pivot_table(Athletes, index=['Country'], columns=['Discipline'], values=['PersonName'], aggfunc='count', fill_value=0)

# Zeige das Ergebnis
print(pivot_table.head(5))

# Berechnen Sie die Summe der Teilnehmer pro Disziplin
discipline_sum = pivot_table.sum(axis=0).sort_values(ascending=False)
# Die 10 besten Disziplinen auswählen
top_10_disciplines = discipline_sum.head(10).index

# Erstellen Sie eine Pivot-Tabelle, die auf den ausgewählten Ländern und Disziplinen basiert.
pivot_table_top_countries = pivot_table[top_10_disciplines].sum(axis=1).sort_values(ascending=False).head(10)
# Die 10 besten Länder aus den 10 besten Disziplinen auswählen
top_10_countries = pivot_table_top_countries.index

# Filtern Sie die Pivot-Tabelle, um nur die Top-10-Länder einzuschließen.
pivot_table_top_countries = pivot_table.loc[top_10_countries, top_10_disciplines]
# Zeige das Ergebnis
print(pivot_table_top_countries.head())
# Zeichnen Sie ein Balkendiagramm für jedes Land, getrennt nach jeder der 10 Disziplinen.
fig, axes = plt.subplots(nrows=len(top_10_countries), ncols=1, figsize=(15, 8 * len(top_10_countries)))

for i, country in enumerate(top_10_countries):
    pivot_table_top_countries.loc[country].T.plot(kind='bar', stacked=True, ax=axes[i])
    axes[i].set_title(f'Anzahl der Teilnehmer pro Disziplin für{country}')
    axes[i].set_xlabel('Discipline')
    axes[i].set_ylabel('Anzahl der Teilnehmer')
    axes[i].legend(title='Discipline', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()

# Zählt die Anzahl der Menschen pro Land
count_by_country = Athletes['Country'].value_counts()
# Zeige das Ergebnis
print(count_by_country)

# Zeichnen Sie ein Balkendiagramm, um die Anzahl der Teilnehmer pro Land zu visualisieren.
count_by_country.plot(kind='bar', figsize=(35, 8))
plt.title('Anzahl der Teilnehmer pro Land')
plt.xlabel('Land')
plt.ylabel('nzahl der Teilnehmer')
plt.show()

# Zählen Sie die Anzahl der Personen pro Disziplin
Athletes_by_Discipline = Athletes['Discipline'].value_counts()
print(Athletes_by_Discipline)

# Zeichnen Sie ein Balkendiagramm, um die Anzahl der Teilnehmer pro Disziplin zu visualisieren.
Athletes_by_Discipline.plot(kind='bar', figsize=(15, 8))
plt.title('Anzahl der Teilnehmer pro Disziplin')
plt.xlabel('Discipline')
plt.ylabel('Nombre de participants')
plt.show()

######################################################Coaches######################################

# Beispiel für die Verwendung von DataFrames
if 'Coaches.csv' in data_frames:
    Coaches = data_frames['Coaches.csv']
    print(Coaches.head())

# Benennen Sie beide Spalten gleichzeitig um
nouveaux_noms = {'NOC': 'Country'}
Coaches.rename(columns=nouveaux_noms, inplace=True)

Coaches.head(5)

# Zählen Sie die Anzahl der Vorkommen für jedes Ereignis.
coaches_by_event = Coaches['Event'].value_counts()

# Zeichnen Sie ein Balkendiagramm, um die Anzahl der Vorkommen pro Ereignis zu visualisieren.
coaches_by_event.plot(kind='bar', figsize=(15, 8))
plt.title('Anzahl von Trainer pro Veranstaltung')
plt.xlabel('Veranstaltung')
plt.ylabel('Anzahl von Trainer')
plt.show()

#############################################EntriesGender#############################################

#EntriesGender
if 'EntriesGender.csv' in data_frames:
    EntriesGender = data_frames['EntriesGender.csv']
    print(EntriesGender.head())

# Angenommen, Ihre Datentabelle "EntriesGender" wird in einer Variablen namens "EntriesGender" gespeichert.
# Stellen Sie sicher, dass die Spaltennamen korrekt sind: 'Disziplin', 'Weiblich', 'Männlich', 'Gesamt'.

# Fügen Sie eine Spalte für den Durchschnitt der männlichen Teilnehmer hinzu.
EntriesGender['Male_Mean'] = EntriesGender['Male'] / EntriesGender['Total']

# Fügen Sie eine Spalte für den Durchschnitt der weiblichen Teilnehmer hinzu.
EntriesGender['Female_Mean'] = EntriesGender['Female'] / EntriesGender['Total']

# Zeige die aktualisierte Tabelle
print(EntriesGender)

#############################################Medals####################################################

if 'Medals.csv' in data_frames:
    Medals = data_frames['Medals.csv']
    print(Medals.head())

nouveaux_noms={'Team/NOC':'Team_by_country'}
Medals.rename(columns=nouveaux_noms, inplace=True)

Medals.head(15)

import pandas as pd
import matplotlib.pyplot as plt

# Angenommen, Ihre Datentabelle "Medals" ist in einer Variablen namens "Medals" gespeichert.
# Stellen Sie sicher, dass die Spaltennamen korrekt sind: 'Team_by_country', 'Gold', 'Silber', 'Bronze', 'Gesamt'.

# Sortieren Sie den DataFrame nach der Anzahl der Goldmedaillen
top_10_gold = Medals.sort_values(by='Gold', ascending=False).head(10)

# Zeige die Tabelle der Top-10-Länder mit den meisten Goldmedaillen.
print("Tabelle der Top-10-Länder mit den meisten Goldmedaillen:")
print(top_10_gold)
# Erstelle ein Balkendiagramm für die ersten 10 Länder mit den meisten Goldmedaillen.
labels = top_10_gold['Team_by_country']
gold_medals = top_10_gold['Gold']

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(labels, gold_medals, color='gold')
ax.set_ylabel('Anzahl der Goldmedaillen')
ax.set_title('Die Top 10 der Länder mit den meisten Goldmedaillen')
plt.xticks(rotation=45, ha='right')  # Rotation der Etiketten für eine bessere Lesbarkeit
plt.show()

################################################Teams###############################################

if 'Teams.csv' in data_frames:
    Teams = data_frames['Teams.csv']
    print(Teams.head())

Teams=Teams.drop(columns='NOC',axis=1)

nouveaux_noms={'Name':'Country'}
Teams.rename(columns=nouveaux_noms,inplace=True)

Teams.head()

import pandas as pd
import matplotlib.pyplot as plt
# Angenommen, Ihre Datentabelle "Teams" wird in einer Variablen namens "Teams" gespeichert.
# Stellen Sie sicher, dass die Spaltennamen korrekt sind: 'Country', 'Discipline', 'Event'.
# Berechnen Sie die Gesamtzahl der Ereignisse für Frauen und Männer.
total_events = Teams.groupby('Event').size().reset_index(name='Total_Events')

# Daten nach Frauen und Männern filtern
total_women = total_events[total_events['Event'] == 'Women']['Total_Events'].values[0]
total_men = total_events[total_events['Event'] == 'Men']['Total_Events'].values[0]

# Prozente berechnen
percentage_women = (total_women / (total_women + total_men)) * 100
percentage_men = (total_men / (total_women + total_men)) * 100
# Erstellen Sie ein Balkendiagramm, um die Gesamtsumme von Frauen und Männern zu vergleichen.
labels = ['Women', 'Men']
values = [total_women, total_men]
percentages = [percentage_women, percentage_men]

fig, ax = plt.subplots()
bars = ax.bar(labels, values, color=['orange', 'blue'])

# Zeige die Prozente über den Balken an
for bar, percentage in zip(bars, percentages):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 0.05, f'{percentage:.2f}%', ha='center', va='bottom')

ax.set_ylabel('Gesamtanzahl der Ereignisse')
ax.set_title('Vergleich der Gesamtzahl der Ereignisse für Frauen und Männer in allen Ländern')

plt.show()

#############################################Data Loaden############################################


# Prüfen Sie, ob der Ordner Data_transformed existiert, wenn nicht, erstellen Sie ihn.
data_transformed_folder = '/app/Data_transformed'
if not os.path.exists(data_transformed_folder):
    os.makedirs(data_transformed_folder)

# Prüfen, ob der Ordner ein Git-Repository ist
git_repo_path = '/app'  # Setze den korrekten Pfad zu deinem Git-Verzeichnis
if not os.path.exists(os.path.join(git_repo_path, '.git')):
   # Der Ordner ist kein Git-Repository, initialisiere das Repository
    repo = git.Repo.init(git_repo_path)
    repo.git.add('.')
    repo.git.commit(m='Initial commit')

# Daten lokal gesichert
Athletes.to_csv(os.path.join(data_transformed_folder, 'Athletes.csv'), index=False)
Coaches.to_csv(os.path.join(data_transformed_folder, 'Coaches.csv'), index=False)
EntriesGender.to_csv(os.path.join(data_transformed_folder,'EntriesGender.csv' ),index=False)
Medals.to_csv(os.path.join(data_transformed_folder,'Medals.csv' ),index=False)
Teams.to_csv(os.path.join(data_transformed_folder,'Teams.csv' ),index=False)

