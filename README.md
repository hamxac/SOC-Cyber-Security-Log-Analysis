# SOC Cyber Security Log Analysis

**Author:** Hamza

## 📌 Project Overview
This project simulates a Security Operations Center (SOC) environment by ingesting, cleaning, and analyzing 40,000 synthetic network traffic logs. The goal is to identify threat patterns, highlight severe vulnerabilities, and map the geographic distribution of attacks to provide actionable threat intelligence.

## 🛠️ Tools & Technologies Used
* **Python (Pandas):** Data ingestion, auditing, and cleaning.
* **SQLite:** Writing queries to extract high-severity threats and aggregate attack vectors.
* **Tableau:** Designing an interactive, dark-mode dashboard for visual threat analysis.

## 📊 Live Dashboard
You can interact with the final Threat Intelligence Dashboard here: 
[**[PASTE YOUR TABLEAU LINK HERE]**](https://public.tableau.com/views/SOC-Incident-Analysis-Dashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## 💻 Code Structure
* `day7_bigdata.py` - Ingests and processes large log files.
* `day8_explore.py` - Audits the dataset for anomalies.
* `day9_cleaner.py` - Cleans and formats the data for SQL integration.
* `analyze.py` - Performs statistical analysis on the network logs.
* `threat_hunting.sql` - Extracts top attack types, severe threats, and geographic locations.
