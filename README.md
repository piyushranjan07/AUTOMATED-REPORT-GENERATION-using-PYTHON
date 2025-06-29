# AUTOMATED-REPORT-GENERATION-using-PYTHON
this is the second task of my first summer internship in python programming 

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: PIYUSH RANJAN

*INTERN ID*: CT04DN870

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION OF PROJECT*:This internship project titled Automated Report Generation, the primary objective was to automate the analysis of structured data using Python and generate a formatted PDF report that presents meaningful statistical insights. This task focused on real-world data handling skills using libraries like pandas and fpdf, providing a solid introduction to data analysis and document automation with Python. It allowed me to explore not just how to read and process data, but also how to present it effectively in a professional format. The task began with a CSV file containing the academic performance of various students. Each row in the file represented a student, including their name and scores in subjects such as Math, Physics, English, PPS, and AI. The use of the CSV format made it easier to simulate real-world tabular data, which is commonly used in data science and software applications. The script first checked whether the file sample_data.csv was available in the working directory using the os.path.exists() function. This step was crucial for ensuring the program did not break due to missing files. If the file was found, the data was loaded using the pandas library, which allowed for efficient manipulation and computation on the dataset. After loading the data, I used pandas functions such as .mean(), .max(), and .min() to compute the average, highest, and lowest values for each numeric column. These operations were performed only on numeric data, excluding text fields like student names, to ensure accuracy. This analysis provided quick statistical insights into the overall performance trends across all students and subjects. Following the analysis, the next major step was generating a PDF report. For this, the fpdf library was used, which enables the creation of PDF documents with custom formatting. A new PDF file was initiated, and the title "Data Analysis Report" was added at the top, centered for emphasis. The mean, maximum, and minimum values were then added to the report using multi_cell() to allow for multi-line text formatting. This method ensured that long blocks of text were wrapped properly and displayed cleanly in the final document. To improve the script's reliability and user experience, if-else conditions were incorporated. These handled situations such as the file being missing or the dataset being empty. Appropriate messages were printed to the console to inform the user of any issues. This helped avoid unexpected crashes and made the script more robust and user-friendly. The final output of the task was a neatly formatted PDF file named report.pdf. This document effectively summarized the key statistical metrics and served as an example of how automation can simplify reporting processes. The use of Python for both analysis and reporting showcases the language's versatility and power for real-world tasks. Through this task, I gained practical experience in data reading, statistical computation, file validation, and report generation. It also helped reinforce concepts related to conditional programming and code organization. Overall, Task 2 was not only technically informative but also very relevant to real-world applications. It laid the foundation for future work in data analysis, automation, and presentation — essential skills for any aspiring data professional or software developer.

*OUTPUT*: ![Image](https://github.com/user-attachments/assets/d4a9a8f6-933b-459a-b150-7fc5dd8f1954)

*SAMPLE FILE*:[sample_data.csv](https://github.com/user-attachments/files/20967466/sample_data.csv)

*REPORT FILE*:[report_task_02.pdf](https://github.com/user-attachments/files/20967469/report_task_02.pdf)
