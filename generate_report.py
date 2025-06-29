import pandas as pd
from fpdf import FPDF
import os

# Check if the CSV file exists
file_path = r"C:\Users\Piyush Ranjan\internship task\TASK_2\sample_data.csv"

if os.path.exists(file_path):
    print("CSV file found. Reading data...")

    # Read data
    file_data = pd.read_csv(file_path)

    # Check if the DataFrame is not empty
    if not file_data.empty:
        print("Data read successfully. Performing analysis...")

        # Perform analysis
        mean_values = file_data.mean(numeric_only=True)
        max_values = file_data.max(numeric_only=True)
        min_values = file_data.min(numeric_only=True)

        # Generate PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align='C')
        pdf.ln(10)

        pdf.multi_cell(0, 10, txt=f"Mean Values:\n{mean_values.to_string()}")
        pdf.ln(5)
        pdf.multi_cell(0, 10, txt=f"Max Values:\n{max_values.to_string()}")
        pdf.ln(5)
        pdf.multi_cell(0, 10, txt=f"Min Values:\n{min_values.to_string()}")

        # Save the PDF
        pdf.output("report.pdf")
        print("PDF report generated successfully!")

    else:
        print("The CSV file is empty. Please check the contents.")

else:
    print(f"Error: File '{file_path}' not found. Please make sure it's in the same directory.")
