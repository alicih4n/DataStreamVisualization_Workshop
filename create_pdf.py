from fpdf import FPDF

# --- CONFIGURATION (Edit these details) ---
COURSE_CODE = "CSCN8010"
WORKSHOP_TITLE = "Data Streaming and Visualization Workshop"
GROUP_NAME = "Group 2"
REPO_LINK = "https://github.com/alicih4n/DataStreamVisualization_Workshop"

TEAM_MEMBERS = [
    {"name": "Ali", "id": "9091405"},
    {"name": "Lohith", "id": "9054407"},
    {"name": "Roshan", "id": "8951614"}
]

# --- PDF GENERATION ---
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Workshop Submission', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf(filename="Submission_Group2.pdf"):
    pdf = PDF()
    pdf.add_page()
    
    # Title Section
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"{COURSE_CODE}: {WORKSHOP_TITLE}", ln=True, align='C')
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(0, 10, GROUP_NAME, ln=True, align='C')
    pdf.ln(10)
    
    # Team Members Section
    pdf.set_font("Arial", 'B', 12)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(0, 10, "Team Members", ln=True, fill=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", size=12)
    for member in TEAM_MEMBERS:
        pdf.cell(60, 10, f"Name: {member['name']}", border=0)
        pdf.cell(0, 10, f"ID: {member['id']}", ln=True)
    pdf.ln(10)
    
    # Repository Link Section
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "GitHub Repository", ln=True, fill=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, REPO_LINK)
    
    # Clickable Link
    pdf.set_xy(10, pdf.get_y() - 10) # Go back up to overlay link
    pdf.set_text_color(0, 0, 255)
    pdf.set_font("Arial", 'U', 11)
    # pdf.cell(0, 10, REPO_LINK, link=REPO_LINK) # Simple link
    
    pdf.ln(20)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", 'I', 10)
    pdf.multi_cell(0, 5, "This document confirms our active participation in the workshop and submission of the required artifacts.")

    pdf.output(filename)
    print(f"✅ Successfully created {filename}")

if __name__ == "__main__":
    create_pdf()
