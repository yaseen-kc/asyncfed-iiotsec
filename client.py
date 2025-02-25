import csv
import os

# We import our server module to call receive_metrics and aggregate_and_plot
import server

def read_csv_metrics(file_path):
    """
    Read a CSV file with columns:
        Round, Accuracy, Precision, Recall, F1-Score
    Return a list of (round_num, accuracy, precision, recall, f1_score).
    """
    data = []
    with open(file_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            round_num = int(row["Round"])
            accuracy = float(row["Accuracy"])
            precision = float(row["Precision"])
            recall = float(row["Recall"])
            f1_score = float(row["F1-Score"])
            data.append((round_num, accuracy, precision, recall, f1_score))
    return data

def run_client(client_id, file_path):
    """
    Simulate a client reading local metrics from a CSV file,
    then sending them to the server.
    """
    metrics = read_csv_metrics(file_path)
    for (round_num, accuracy, precision, recall, f1_score) in metrics:
        # Send each round's metrics to the server
        server.receive_metrics(
            client_id,
            round_num,
            accuracy,
            precision,
            recall,
            f1_score
        )
    print(f"Client {client_id} has sent all metrics to the server.")

def main():
    # Path to the Datasets folder
    folder_path = "Datasets"

    # Simulate 4 clients
    client_files = [
        ("Client1", os.path.join(folder_path, "data1.csv")),
        ("Client2", os.path.join(folder_path, "data2.csv")),
        ("Client3", os.path.join(folder_path, "data3.csv")),
        ("Client4", os.path.join(folder_path, "data4.csv"))
    ]

    # Each client reads its CSV and sends metrics to the server
    for client_id, file_path in client_files:
        run_client(client_id, file_path)

    # After all clients have sent data, instruct server to aggregate & plot
    server.aggregate_and_plot()

if __name__ == "__main__":
    main()
