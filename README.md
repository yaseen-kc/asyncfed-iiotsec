# Enhancing cybersecurity in Edge IIoT networks: An asynchronous federated learning approach with a deep hybrid detection model - Demo

This repository demonstrates a simple toy setup of a federated-like workflow, where multiple clients each have their own dataset (in CSV format), and a server aggregates and plots the round-wise metrics (Accuracy, Precision, Recall, F1-Score).

## Project Structure

```
.
├── create_datasets.py    # Script to generate dummy CSV files for each client
├── client.py             # Simulates multiple clients sending metrics to the server
├── server.py             # Aggregates metrics and plots the round-wise average scores
└── Datasets/
    ├── data1.csv
    ├── data2.csv
    ├── data3.csv
    └── data4.csv
```

1. **`create_datasets.py`**  
   Generates four dummy CSV files (`data1.csv`, `data2.csv`, `data3.csv`, `data4.csv`) in the `Datasets` folder. Each file simulates 20 rounds of training metrics, gradually increasing toward a perfect score (1.0).

2. **`server.py`**  
   Provides functions to receive metrics from clients (`receive_metrics`) and to aggregate and plot them (`aggregate_and_plot`). In a real-world application, this could be replaced with a proper server (e.g., Flask, FastAPI, or a socket-based server) that receives metrics over the network.

3. **`client.py`**  
   Simulates four different “clients.” Each one loads its local CSV file and sends round-wise metrics to the server. Finally, once all clients have reported, the server plots the round-wise average metrics.

4. **`Datasets/`**  
   The folder where the dummy CSV files are stored. Initially empty, it gets populated once you run `create_datasets.py`.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/YourRepoName.git
   cd YourRepoName
   ```

2. **Create a virtual environment (optional)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**:
   This demo only requires `matplotlib` for plotting. You may already have it, but if not:
   ```bash
   pip install matplotlib
   ```

4. **Generate dummy CSV data**:
   ```bash
   python create_datasets.py
   ```
   - This will create four CSV files (`data1.csv`, `data2.csv`, `data3.csv`, `data4.csv`) inside the `Datasets` folder.
   - Each file simulates 20 rounds of metrics (Accuracy, Precision, Recall, F1-Score), starting from roughly 0.7–0.85 and trending toward 0.95–1.0.

5. **Run the client script** (which calls the server to aggregate & plot):
   ```bash
   python client.py
   ```
   - The script reads each CSV file from the `Datasets` folder.
   - Sends round-wise metrics to the server.
   - Finally, the server aggregates and plots the average metrics across all clients, displaying a **matplotlib** chart.

## Usage Notes

- **Real Federated Learning**: This is a simplified demonstration. In a real-world scenario, each client would train locally and send either model updates or performance metrics to a central server. Communication could happen via network sockets or HTTP endpoints, rather than direct function calls.
- **Custom Data**: You can replace the dummy CSV generation with your own data. Just ensure each CSV has the columns:  
  ```
  Round, Accuracy, Precision, Recall, F1-Score
  ```
  and that each client has the same number of rounds.
- **Plot Range**: The script sets the y-axis to range from `0.0` to `1.0`, which matches typical performance metrics in machine learning. If your data falls outside this range, you can adjust the axis limits in `server.py`.

