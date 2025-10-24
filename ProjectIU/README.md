# Batch-Prozess |  End-to-End Data Engineering Project

## Inhaltsübersicht
- [Einleitung](#Einleitung)
- [Dateninfrastruktur](#Dateninfrastruktur)
- [Beschreibung von Data](#Beschreibung_von_Data)
- [Quelle](#Quelle)
- [Technologien](#Technologien)


## Einleitung

In diesem Projekt wird eine End-to-End-Pipeline für Data Engineering aufgebaut, die auf einem Batch-Prozess basiert. Sie deckt alle Schritte von der Datenaufnahme über die Verarbeitung bis hin zur Speicherung ab und nutzt einen robusten Technologie-Stack, der Python und Docker-compose umfasst. Alles wird mithilfe von Docker containerisiert, um den Einsatz und die Skalierbarkeit zu erleichtern.


## Dateninfrastruktur

![System Architecture](https://github.com/agbamate1/Batch-project/blob/master/Dateninfrastruktur_Batch_.png)


## Beschreibung_von_Data

Dieser Datensatz enthält die Daten von über 11.000 Athleten in 47 Disziplinen und 743 Mannschaften, die an den Olympischen Spielen 2021 (2020) in Tokio teilnehmen. Dieser Datensatz enthält die Angaben zu den teilnehmenden Athleten, Trainern und Mannschaften sowie zu den Einträgen nach Geschlecht. Er enthält die Namen, die vertretenen Länder, die Disziplin, das Geschlecht der Teilnehmer und die Namen der Trainer.

- 1-City: Stadt, in der die Olympischen Spiele stattfanden
- 2-Year: Jahr, in dem die Olympischen Spiele stattgefunden haben
- 3-Sport: Sportkategorie (z. B. Wassersport, Leichtathletik usw.)
- 4-Discipline: Die Disziplin innerhalb der Sportart (z. B. Tauchen, Schwimmen usw.)
- 5-Event: Name des Ereignisses innerhalb der jeweiligen Disziplin (z. B. 3-m-Sprungbrett, 10-m-Plattform usw.)
- 6-Athlete: Name des Siegers in dieser Disziplin
- 7-Gender: Geschlecht
- 8-Country_Code: 3-stelliger Ländercode
- 9-Country: Land, dem der siegreiche Athlet angehört
- 10-Event_gender: Geschlechter, die an der Veranstaltung teilgenommen haben (männlich, weiblich oder gemeinsame Veranstaltung)
- 11-Medal: Medaille (z. B. Bronze, Silber, Gold)


## Quelle

Website der Olympischen Spiele 2020 in Tokio

- Link: https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo

## Technologien

Das Projekt umfasst die folgenden Komponenten:

- **Data Quelle**: Wir haben die Daten aus `www.kaggle.com`, für unser Projekt über den Batch-Prozessor verwendet. 
- **Python**: Programmierungssprache für Pipeline und Datenschutz
- **Docker-compose**: Wo werden die verarbeiteten Daten gespeichert.

## Erste Schritte

1. Klonen Sie das Repository:

    ```bash
    git clone -b master https://github.com/agbamate1/Batch-project.git
    ```

2. Navigieren Sie zum Projektverzeichnis:
    ```bash
    cd Batch-project/code
    ```

3. Führen Sie Dockerfile aus, um die Dienste einzurichten:
    ```bash
    docker-compose up
    ```
