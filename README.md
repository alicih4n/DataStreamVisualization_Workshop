# Predictive Maintenance Dashboard
### Foundations of Machine Learning Frameworks - Workshop

## 👥 Team Members
*   **Member 1:** Ali (ID: 9091405)
*   **Member 2:** Lohith (ID: 9054407)
*   **Member 3:** Roshan (ID: 8951614)

---

## 📝 Use Case: Robot Predictive Maintenance
In this manufacturing facility, we are monitoring **Material Handling Robots** to prevent downtime caused by Torque Tube Failures.
The goal of this project is to build a **Predictive Maintenance Dashboard** that:
1.  **Streams** live data from robot controllers (simulated).
2.  **Persists** this data into a database for historical analysis.
3.  **Visualizes** real-time performance to detect anomalies.
4.  **Predicts** potential failures before they cause 480+ minutes of downtime.

## 🔧 Project Structure
*   `DataStreamVisualization_Workshop.ipynb`: The main notebook containing the simulation, database logic, and visualization.
*   `StreamingSimulator.py`: Custom Python module developed to handle the CSV data streaming and SQLite database interactions.
*   `data/`: Contains the robot dataset (`RMBR4-2_export_test.csv`).
*   `documents/`: Documentation and ER diagrams.
*   `Submission_Group2.pdf`: Official submission document.

## 🚀 How to Run
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Open `DataStreamVisualization_Workshop.ipynb` in Jupyter Notebook or VS Code.
3.  Run all cells to see the real-time dashboard and analysis.

## 📊 Dataset
The dataset represents sensor readings from the robot's axes, specifically focusing on current load and torque data.
*   **Source**: Provided by Workshop Instructor
*   **License**: Educational Use Only
