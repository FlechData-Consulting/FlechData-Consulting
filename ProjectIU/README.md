# **Batch Process | End-to-End Data Engineering Project**

## Table of Contents

* [Introduction](#introduction)
* [Data Infrastructure](#data-infrastructure)
* [Data Description](#data-description)
* [Data Source](#data-source)
* [Technologies](#technologies)
* [Getting Started](#getting-started)

---

## **Introduction**

This project builds an **end-to-end data engineering pipeline** based on a **batch processing architecture**.
It covers all stages from data ingestion and transformation to storage using a robust technology stack built with **Python** and **Docker Compose**.
All components are containerized using Docker to ensure **easy deployment, scalability, and consistency** across environments.

---

## **Data Infrastructure**

![System Architecture](https://github.com/FlechData-Consulting/FlechData-Consulting/blob/main/ProjectIU/Datenflussdiagramm%20f%C3%BCr%20Batch-Prozess.png)

---

## **Data Description**

This dataset includes information about **over 11,000 athletes** across **47 disciplines** and **743 teams** who participated in the **Tokyo 2021 (2020) Olympic Games**.
It contains detailed information about athletes, coaches, teams, gender distribution, and performance data.

Each record includes:

* **City** – City where the Olympic Games took place
* **Year** – Year of the Olympic Games
* **Sport** – Sport category (e.g., Aquatics, Athletics, etc.)
* **Discipline** – Sub-discipline within the sport (e.g., Diving, Swimming, etc.)
* **Event** – Specific event name (e.g., 3m Springboard, 10m Platform, etc.)
* **Athlete** – Name of the athlete who won the event
* **Gender** – Gender of the athlete
* **Country_Code** – Three-letter country code
* **Country** – Country represented by the athlete
* **Event_Gender** – Gender category of the event (male, female, or mixed)
* **Medal** – Type of medal won (Bronze, Silver, Gold)

---

## **Data Source**

Official dataset from the **Tokyo 2020 Olympic Games**

📊 **Source:** [Kaggle - 2021 Olympics in Tokyo](https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo)

---

## **Technologies**

This project includes the following key components:

* **Data Source:** Data collected from `www.kaggle.com` and processed through a batch data pipeline.
* **Python:** Programming language for ETL, data processing, and automation.
* **Docker Compose:** Used to orchestrate and store processed data within Docker containers.

---

## **Getting Started**

1. **Clone the repository:**

   ```bash
   git clone -b main https://github.com/FlechData-Consulting/FlechData-Consulting.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd ProjectIU/code
   ```

3. **Run Docker Compose to set up the services:**

   ```bash
   docker-compose up
   ```

