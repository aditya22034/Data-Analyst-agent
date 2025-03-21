# import requests
# import streamlit as st
# import pandas as pd
# import fitz  # PyMuPDF for PDFs

# # OpenRouter API Key (replace with your actual key)
# API_KEY = "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"

# # Function to send user question and file content to OpenRouter API
# def ask_openrouter(question, context=""):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "mistralai/mistral-7b-instruct",
#         "messages": [{"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}],
#         "max_tokens": 300,
#         "temperature": 0.28
#     }

#     response = requests.post(url, json=payload, headers=headers)
    
#     if response.status_code == 200:
#         return response.json()["choices"][0]["message"]["content"]
#     else:
#         return f"Error: {response.json()}"

# # Function to process uploaded files
# def process_file(file):
#     file_ext = file.name.split(".")[-1].lower()

#     if file_ext == "txt":
#         return file.read().decode("utf-8", errors="replace")  

#     elif file_ext == "pdf":
#         with open("temp.pdf", "wb") as f:
#             f.write(file.read())
#         doc = fitz.open("temp.pdf")
#         return "\n".join([page.get_text("text") for page in doc])

#     elif file_ext == "csv":
#         try:
#             df = pd.read_csv(file, encoding="utf-8")
#             return df.head(20).to_string()  # Convert first 20 rows to string for AI processing
#         except Exception as e:
#             return f"Error reading CSV: {str(e)}"

#     elif file_ext == "xlsx":
#         try:
#             df = pd.read_excel(file, engine="openpyxl")
#             return df.head(20).to_string()  
#         except Exception as e:
#             return f"Error reading Excel: {str(e)}"

#     else:
#         return "Unsupported file format"

# # Streamlit App
# def main():
#     st.title("OpenRouter AI File Analyzer")

#     uploaded_file = st.file_uploader("Upload a file (.txt, .pdf, .csv, .xlsx)", type=["txt", "pdf", "csv", "xlsx"])

#     if uploaded_file is not None:
#         file_content = process_file(uploaded_file)

#         if isinstance(file_content, str):
#             st.subheader("File Preview")
#             st.write(file_content[:1000])  # Show first 1000 characters

#         question = st.text_input("Ask a question about the file:")

#         if st.button("Get Answer"):
#             answer = ask_openrouter(question, file_content)
#             st.subheader("AI Answer")
#             st.write(answer)

# if __name__ == "__main__":
#     main()


# import requests
# import streamlit as st
# import pandas as pd
# import fitz  # PyMuPDF for PDF processing
# import matplotlib.pyplot as plt

# API_KEY = "your-api-key-here"  # Replace with your actual API key

# # Function to call OpenRouter API
# def ask_openrouter(question, context=""):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "mistralai/mistral-7b-instruct",
#         "messages": [{"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}],
#         "max_tokens": 300,
#         "temperature": 0.28
#     }

#     response = requests.post(url, json=payload, headers=headers)
    
#     if response.status_code == 200:
#         return response.json()["choices"][0]["message"]["content"]
#     else:
#         return f"Error: {response.json()}"

# # Function to process uploaded files
# def process_file(file):
#     file_ext = file.name.split(".")[-1].lower()

#     if file_ext == "txt":
#         return file.read().decode("utf-8", errors="replace")

#     elif file_ext == "pdf":
#         with open("temp.pdf", "wb") as f:
#             f.write(file.read())
#         doc = fitz.open("temp.pdf")
#         return "\n".join([page.get_text("text") for page in doc])

#     elif file_ext == "csv":
#         try:
#             df = pd.read_csv(file, encoding="utf-8")
#             return df
#         except Exception as e:
#             return f"Error reading CSV: {str(e)}"

#     elif file_ext == "xlsx":
#         try:
#             df = pd.read_excel(file, engine="openpyxl")
#             return df
#         except Exception as e:
#             return f"Error reading Excel: {str(e)}"

#     else:
#         return "Unsupported file format"

# # Function to generate visualization
# def generate_visualization(data):
#     if isinstance(data, pd.DataFrame):
#         st.write("Data Table Preview:")
#         st.write(data.head(10))  # Display first 10 rows
        
#         num_cols = data.select_dtypes(include=["number"]).columns
#         if len(num_cols) > 0:
#             st.write("Data Visualization:")
#             fig, ax = plt.subplots()
#             data[num_cols[0]].hist(bins=20, ax=ax)  # Generate histogram for first numeric column
#             st.pyplot(fig)
#         else:
#             st.write("No numerical columns found for visualization.")

# # Streamlit App
# def main():
#     st.title("OpenRouter AI - File Data Analyst")

#     uploaded_file = st.file_uploader("Upload a document (.txt, .pdf, .csv, .xlsx)", type=["txt", "pdf", "csv", "xlsx"])

#     if uploaded_file is not None:
#         file_content = process_file(uploaded_file)

#         if isinstance(file_content, str):  # Text file or PDF
#             st.write("File Content Preview:")
#             st.write(file_content[:1000])  # Show first 1000 characters
#             context = file_content

#         elif isinstance(file_content, pd.DataFrame):  # CSV or Excel
#             generate_visualization(file_content)
#             context = "Data file uploaded successfully."

#         else:
#             context = "Unsupported file format."

#         question = st.text_input("Ask a question about the file:")

#         if st.button("Get Answer"):
#             answer = ask_openrouter(question, context)
#             st.write("AI Answer:")
#             st.write(answer)

# if __name__ == "__main__":
#     main()

import requests
import streamlit as st
import pandas as pd
import fitz  

# OpenRouter API Key (replace with your actual key)
API_KEY = "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"

# Function to send user question and file content to OpenRouter API
def ask_openrouter(question, context=""):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}],
        "max_tokens": 300,
        "temperature": 0.28
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.json()}"

# Function to process uploaded files
def process_file(file):
    file_ext = file.name.split(".")[-1].lower()

    if file_ext == "txt":
        return file.read().decode("utf-8", errors="replace")  

    elif file_ext == "pdf":
        with open("temp.pdf", "wb") as f:
            f.write(file.read())
        doc = fitz.open("temp.pdf")
        return "\n".join([page.get_text("text") for page in doc])

    elif file_ext == "csv":
        try:
            df = pd.read_csv(file, encoding="utf-8")
            return df
        except Exception as e:
            return f"Error reading CSV: {str(e)}"

    elif file_ext == "xlsx":
        try:
            df = pd.read_excel(file, engine="openpyxl")
            return df  
        except Exception as e:
            return f"Error reading Excel: {str(e)}"

    else:
        return "Unsupported file format"

# Function to visualize data (Only for CSV & Excel)
def visualize_data(df):
    if isinstance(df, pd.DataFrame):
        st.subheader("Data Table (First 20 Rows)")
        st.write(df.head(20))

        # Select only numeric columns with actual values
        numeric_cols = df.select_dtypes(include=['number']).columns
        valid_cols = [col for col in numeric_cols if df[col].dropna().sum() != 0]  

        if valid_cols:
            st.subheader(f"Bar Chart ({valid_cols[0]})")
            st.bar_chart(df[valid_cols[0]])
        else:
            st.write("No valid numeric columns found for visualization.")


def main():
    st.title("OpenRouter AI File Analyzer")

    uploaded_file = st.file_uploader("Upload a file (.txt, .pdf, .csv, .xlsx)", type=["txt", "pdf", "csv", "xlsx"])

    if uploaded_file is not None:
        file_content = process_file(uploaded_file)

        # Show visualization if CSV/Excel
        if isinstance(file_content, pd.DataFrame):
            visualize_data(file_content)
            file_content = file_content.head(20).to_string()  

        elif isinstance(file_content, str):
            st.subheader("File Preview")
            st.write(file_content[:1000])  

        question = st.text_input("Ask a question about the file:")

        if st.button("Get Answer"):
            answer = ask_openrouter(question, file_content)
            st.subheader("AI Answer")
            st.write(answer)

if __name__ == "__main__":
    main()
