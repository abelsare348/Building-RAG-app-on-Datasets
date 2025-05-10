import os
import csv
import pandas as pd
from PyPDF2 import PdfReader
from docx import Document
import json
from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
def load_documents(data_path):
    documents=[]
    # document_loader = PyPDFDirectoryLoader(data_path)
    # return document_loader.load()

    

    document_loader = CSVLoader(data_path)
    documents.extend(document_loader.load())
    return documents


    # loader = CSVLoader(data_path)
    # return loader.load()
    #documents = []
    
    # Loop through each file in the directory
    # for filename in os.listdir(data_path):
    #     file_path = os.path.join(data_path, filename)
        
    #     if os.path.isfile(file_path):
    #         # Check the file extension
    #         file_extension = filename.split('.')[-1].lower()
            
    #         # Load PDF files
    #         if file_extension == 'pdf':
    #             documents = load_pdf(file_path)
            
            # Load Word files
            # elif file_extension == 'docx':
            #     documents.extend(load_docx(file_path))
            
            # # Load plain text files
            # elif file_extension == 'txt':
            #     documents.extend(load_txt(file_path))
            
            # # Load CSV files
            # elif file_extension == 'csv':
            #     documents.extend(load_csv(file_path))
            
            # # Load Excel files
            # elif file_extension in ['xls', 'xlsx']:
            #     documents.extend(load_excel(file_path))
            
            # # Load JSON files
            # elif file_extension == 'json':
            #     documents.extend(load_json(file_path))
            
            # You can add more file types here if necessary
    
    #return documents

def load_pdf(file_path):
    # Function to read PDF files
    document_loader = PyPDFDirectoryLoader(file_path)
    return document_loader.load()

# def load_docx(file_path):
#     # Function to read Word files
#     documents = []
#     doc = Document(file_path)
#     for para in doc.paragraphs:
#         documents.append(para.text)
#     return documents

# def load_txt(file_path):
#     # Function to read Text files
#     with open(file_path, 'r') as file:
#         return file.readlines()

# def load_csv(file_path):
#     # Function to read CSV files
#     documents = []
#     with open(file_path, newline='', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             documents.append(row)
#     return documents

# def load_excel(file_path):
#     # Function to read Excel files (both .xls and .xlsx)
#     documents = []
#     df = pd.read_excel(file_path, sheet_name=None)  # Read all sheets
#     for sheet_name, sheet_data in df.items():
#         documents.append(sheet_data.to_dict(orient='records'))  # Convert each sheet to a list of dicts
#     return documents

# def load_json(file_path):
#     # Function to read JSON files
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return json.load(file)

# Example usage
# data_path = "myenv/data"
# documents = load_documents(data_path)
