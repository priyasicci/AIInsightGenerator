# A Guided Live Project – Automated Data Insights Generator# 
This project is Text-to-SQL Insights Generator, a hands-on project developed to learn about AI. This application empowers non-technical users to interact with datasets and generate visual and textual insights using natural language — without writing a single line of SQL or code.

## Project Overview ##

This project demonstrates how to:

Process natural language inputs to generate automated insights from a structured SQL database.

Build a data pipeline that loads CSV files into a MySQL database.

Leverage LangChain for SQL querying and Streamlit for an interactive chat-based dashboard.

Enable real-time data analysis and visualization using plain English queries.

## Learning Objectives ##

Build an LLM-powered tool that turns natural language into SQL and generates real-time insights.

Load and store CSV data in MySQL using a Python-based pipeline.

Use LangChain to translate natural language into structured SQL queries.

Build an interactive Streamlit UI for intuitive data exploration.

Understand the design principles behind scalable, user-friendly insight platforms.

### Technologies Used ###
Python – Application and pipeline development

SQL – Querying and data storage

MySQL – Relational database backend

LangChain – NLP orchestration and SQL agent

Streamlit – Web-based chat UI for interactive data analysis

## Running the Project ##
1. Configure Your Environment
   Set up your API key and SQL password in the constants.py
2. Install all required packages:
   pip install -r requirements.txt
3. Run the Jupyter Notebook
   Language_to_Dashboard.ipynb
   Explore CSV data
   Create database and tables
   Insert data into MySQL
   Integrate LangChain for SQL generation
   Use SQLQueryEngine and PythonDashboardEngine
   Run insight queries (Query 1 to Query 7)

## Modular Chat App with Streamlit ##
To launch the Streamlit app:
    streamlit run src/app.py






