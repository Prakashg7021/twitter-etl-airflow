# 🚀 Twitter ETL with Airflow

This repository contains a simple ETL (Extract, Transform, Load) pipeline to collect tweets from a Twitter user, transform them into a structured format, and save them as a CSV file. The entire process is automated using Apache Airflow.

---

## 📄 Overview

This project:

- Connects to the Twitter API using Tweepy.
- Fetches the latest tweets from a specific user (e.g., `@prakashgupta`).
- Extracts and refines important fields (username, text, like count, retweet count, created date).
- Saves the data to an S3 bucket as a CSV file.
- Uses Airflow to schedule and run this ETL process daily.
- Deployed on an AWS EC2 instance for automated and scalable execution.

---

## 🛠️ Files

- `twitter_etl.py`: Contains the main ETL logic for extracting, transforming, and saving tweets to S3.
- `twitter_dag.py`: Defines an Airflow DAG to run the ETL job on a daily schedule.
- `README.md`: Project documentation and setup instructions.

---

## ⚙️ Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Prakashg7021/twitter-etl-airflow.git
cd twitter-etl-airflow

