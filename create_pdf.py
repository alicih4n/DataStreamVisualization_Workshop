from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Robot Maintenance Analysis - Submission', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

def create_pdf():
    pdf = PDF()
    pdf.add_page()
    
    # -- Student Details --
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Student Details:', 0, 1)
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 6, 'Name: Ali Cihan Ozdemir (ID: 9091405)', 0, 1)
    pdf.cell(0, 6, 'Teammate: Lohith Reddy (ID: 9054470)', 0, 1)
    pdf.cell(0, 6, 'Group: 2', 0, 1)
    pdf.ln(5)
    
    # -- Project Description --
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Project Overview:', 0, 1)
    pdf.set_font('Arial', '', 11)
    project_desc = (
        "This project analyzes Robot Maintenance Data, specifically focusing on the current consumption "
        "of different robot axes. By applying Data Engineering pipelining and Linear Regression, "
        "we aim to identify correlations between axes (e.g., Axis #1 and Axis #6), which is critical "
        "for anomaly detection and predictive maintenance."
    )
    pdf.multi_cell(0, 6, project_desc)
    pdf.ln(5)

    # -- Architecture --
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'System Architecture & Structure:', 0, 1)
    pdf.set_font('Arial', '', 10)
    structure = (
        "- data/raw/: robot_maintenance_data.csv (RMBR4-2 raw export).\n"
        "- data/processed/: robot_current_clean.csv (Cleaned current data).\n"
        "- notebooks/EDA.ipynb: Data ingestion, time-series plotting, and specific feature correlation.\n"
        "- notebooks/linear_regression.ipynb: Modeling axis relationships using custom gradient descent.\n"
        "- src/: Reusable modules.\n"
        "- experiments/: Results logging."
    )
    pdf.multi_cell(0, 5, structure)
    pdf.ln(5)

    # -- Key Deliverables & Code Logic --
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Core Implementation Details:', 0, 1)
    pdf.set_font('Arial', '', 10)
    logic = (
        "1. Data Pipeline: We ingest raw CSV data, filter for 'current' traits, parse timestamps, and "
        "handle missing values.\n"
        "2. EDA: We visualized Axis #1 current over time and calculated a correlation matrix across all 14 axes.\n"
        "3. custom Linear Regression: We implemented a Scratch Linear Regression model to predict "
        "Axis #6 current based on Axis #1. This relationship helps model normal operating behavior.\n"
        "4. Validation: We benchmarked our model against Scikit-Learn, achieving comparable RMSE."
    )
    pdf.multi_cell(0, 5, logic)
    pdf.ln(5)

    # -- How to Run --
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Execution Instructions:', 0, 1)
    pdf.set_font('Arial', '', 10)
    steps = (
        "1. Install dependencies: pip install -r requirements.txt\n"
        "2. Run EDA: Execute notebooks/EDA.ipynb to process the robot data.\n"
        "3. Run Modeling: Execute notebooks/linear_regression.ipynb.\n"
        "4. View Results: Check experiments/results.csv."
    )
    pdf.multi_cell(0, 5, steps)
    pdf.ln(5)

    # -- GitHub Link --
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Repository:', 0, 1)
    pdf.set_font('Arial', 'U', 10)
    pdf.set_text_color(0, 0, 255)
    pdf.cell(0, 6, 'https://github.com/alicih4n/DataStreamVisualization_Workshop.git', 0, 1, link='https://github.com/alicih4n/DataStreamVisualization_Workshop.git')
    
    pdf.output('Project_Submission_Report.pdf', 'F')
    print("PDF Generated successfully.")

if __name__ == '__main__':
    create_pdf()
