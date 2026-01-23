# Predictive Maintenance Dashboard
### Foundations of Machine Learning Frameworks - Workshop

## 👥 Team: Group 2
*   **Ali (ID: 9091405)**
*   **Lohith (ID: 9054407)**
*   **Roshan Bartaula (ID: 8951614)**

---

## 📝 Use Case: Manufacturing Robot Predictive Maintenance
In this hands-on workshop, our team built a **Predictive Maintenance Dashboard** application. This tool provides visibility for an Anomaly Detection and response management workflow in a manufacturing facility.

### \u2705 Grading Criteria Met (Level 5)
1.  **Remote Database**: Uses a live **Neon.tech PostgreSQL** database for data persistence.
2.  **Data Collection**: Streams data from the CSV one record at a time with a **2-second interval** simulated delay.
3.  **Dynamic Dashboard**: Visualizes real-time performance to detect anomalies, configured to highlight thresholds (Value > 6).

## 🔧 Project Files
*   `DataStreamVisualization_Workshop.ipynb`: The main Jupyter Notebook containing:
    *   Step 1: Simulation Setup & Remote DB Connection
    *   Step 2: Live Data Streaming & Dashboard Visualization
    *   Step 3: Analytical Overview
*   `StreamingSimulator.py`: Helper class for streaming CSV operations.
*   `Submission_Group2.pdf`: Official PDF submission including team details.
*   `requirements.txt`: Dependencies required to run the project.
*   `data/`: Contains the specific robot dataset (`RMBR4-2_export_test.csv`).

## 🚀 How to Run
1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/alicih4n/DataStreamVisualization_Workshop.git
    cd DataStreamVisualization_Workshop
    ```
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Notebook**:
    Open `DataStreamVisualization_Workshop.ipynb` in Jupyter Lab or VS Code and click "Run All".
    *   *Note: The notebook is pre-configured to connect to our Neon Database.*

## 📊 Dataset
The dataset represents sensor readings from robot axes, focused on identifying Torque Tube Failures before they lead to downtime.
*   **Source**: Provided by Workshop Instructor
