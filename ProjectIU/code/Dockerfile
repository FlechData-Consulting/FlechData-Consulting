# Utiliser une image Python de base
FROM python:latest

# RUN pip install pandas

# Definiere das Arbeitsverzeichnis innerhalb des Containers
WORKDIR /app

# Kopiere alle Dateien aus dem lokalen Kontext in das Verzeichnis /app/ des Containers.
COPY . /app

# Git installieren
RUN apt-get update && apt-get install -y git

# Benutzerinformationen für Git konfigurieren
RUN git config --global user.email "adinonalfred@gmail.com" && \
    git config --global user.name "Your Name"

# Initialisiere das Git-Repository und mache einen Initial Commit
RUN git init && git add . && git commit -m "Initial commit"

# Installiere die Python-Abhängigkeiten aus der Datei requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Standard-CMD zum Ausführen des Python-Skripts
CMD ["python3", "etl_project.py"]


