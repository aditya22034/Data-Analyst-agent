import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai
import fitz 
import streamlit as st

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-pro-latest") 

# this is the function to ask quesion 
def ask_gemini(question, context=""):

    response = model.generate_content(f"Context: {context}\nQuestion: {question}")
    return response.text 

# function for reading text files
def read_text_file(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Function for reading PDF files
def read_pdf_file(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

# Function to process uploaded files
def process_file(file):
    file_ext = file.name.split(".")[-1].lower()
    
    if file_ext == "txt":
        return file.read().decode("utf-8")
    
    elif file_ext == "pdf":
        with open("temp.pdf", "wb") as f:
            f.write(file.read())
        return read_pdf_file("temp.pdf")
    
    elif file_ext == "csv":
        return pd.read_csv(file)
    
    elif file_ext == "xlsx":
        return pd.read_excel(file)
    
    else:
        return "Unsupported file format"

# Function to create visualization of the data 
def generate_visualization(data):
    if isinstance(data, pd.DataFrame):

        st.write(" Sample Data")
        st.write(data.head())  

        # Create  bar chart if numerical data is present
        num_cols = data.select_dtypes(include=["number"]).columns

        if len(num_cols) > 0:
            st.write(" Data Visualization")
            fig, ax = plt.subplots()

            data[num_cols[0]].value_counts().plot(kind="bar", ax=ax)
            st.pyplot(fig)

        else:
            st.write("No numerical data has beeen found for visualization.")
    else:
        st.write("Uploaded file is not a structured dataset.")


def main():
    st.title(" Data Analyst Agent")
    st.write("Upload a file, ask questions, and generate insights!")

    uploaded_file = st.file_uploader("Upload a document (.txt, .pdf, .csv, .xlsx)", type=["txt", "pdf", "csv", "xlsx"])

    if uploaded_file is not None:
        data = process_file(uploaded_file)

        if isinstance(data, str):
            st.write(" File Content")
            st.write(data)
            context = data

        else:
            generate_visualization(data)
            context = "Data file uploaded successfully."

        question = st.text_input("Ask a question about the file")

        if st.button("Get Answer"):
            answer = ask_gemini(question, context)
            st.write(" Answer:")
            st.write(answer)

if __name__ == "__main__":
    main()  
