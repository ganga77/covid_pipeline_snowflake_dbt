Project Title: COVID-19 Data Engineering and Analysis Pipeline
Objective:
To create an automated data engineering pipeline for downloading COVID-19 data from Kaggle, uploading it to Amazon S3, integrating it with Snowflake, and performing data analysis using dbt, SQL, and Tableau.

Problem Solved:

The project addresses the need for automation in data engineering processes, specifically for downloading datasets from external sources like Kaggle, uploading them to cloud storage (Amazon S3), and integrating them with a data warehouse (Snowflake). This automation significantly reduces manual effort and ensures timely updates of the dataset for analysis.

Steps and Outcomes:
Data Download from Kaggle:
Problem: Manual downloading of datasets is time-consuming and prone to delays.
Solution: A Python script was written to automate the download of the COVID-19 dataset from Kaggle.
Outcome: The dataset is automatically downloaded from Kaggle, ensuring the latest data is always available.
Uploading Data to Amazon S3:
Problem: Storing large datasets locally is inefficient and poses accessibility issues.
Solution: A Python script was created to upload the downloaded CSV files to an Amazon S3 bucket.
Outcome: The dataset is securely stored in the cloud, making it accessible for further processing and analysis.
Snowflake Integration:
Problem: Efficient data warehousing and querying require a robust integration with cloud storage.
Solution: An Amazon S3 integration model was created in Snowflake, along with a staging area to load data before transferring it to final tables.
Outcome: Data is loaded from S3 into Snowflake efficiently, ready for data modeling and analysis.
Data Modeling with dbt:
Problem: Raw datasets often contain extraneous information that can complicate analysis.
Solution: dbt was used for data modeling, focusing on filtering out important columns relevant to the analysis.
Outcome: Clean and structured datasets are prepared, highlighting crucial information for data analysis.
Data Unloading from Snowflake to S3:
Problem: Analysis tools may require data to be in a specific format or location.
Solution: A Python script was written to unload data from Snowflake back to the S3 bucket.
Outcome: Processed data is available in S3, ready for analysis using various tools.
Data Analysis with Tableau:
Problem: Understanding the impact of COVID-19 requires visual and comparative analysis.

Summary:
This project successfully automated the end-to-end process of downloading, storing, processing, and analyzing COVID-19 data. By leveraging Python, Amazon S3, Snowflake, dbt, and Tableau, the pipeline ensures that the data is always up-to-date, structured, and ready for insightful analysis.
