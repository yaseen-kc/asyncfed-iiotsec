import os
import csv
import random

# def generate_dummy_data(num_rounds=20, start_min=0.70, start_max=0.85, end_min=0.95, end_max=1.0):
def generate_dummy_data(num_rounds=20, start_min=0.00, start_max=0.10, end_min=0.95, end_max=1.0):

    """
    Generate a list of (round, accuracy, precision, recall, f1_score) tuples.
    The values gradually increase to simulate learning progress.
    """
    data = []
    for r in range(1, num_rounds + 1):
        # fraction: how far along we are in the rounds (0 to 1)
        fraction = (r - 1) / float(num_rounds - 1)

        # Random start plus fraction of the difference to the 'end' range
        accuracy = random.uniform(start_min, start_max) + fraction * (end_min - start_min)
        precision = random.uniform(start_min, start_max) + fraction * (end_min - start_min)
        recall = random.uniform(start_min, start_max) + fraction * (end_min - start_min)
        f1_score = random.uniform(start_min, start_max) + fraction * (end_min - start_min)

        # Clamp values at 1.0 (just in case random overshoot)
        accuracy = min(accuracy, 1.0)
        precision = min(precision, 1.0)
        recall = min(recall, 1.0)
        f1_score = min(f1_score, 1.0)

        data.append((r, accuracy, precision, recall, f1_score))
    return data

def write_csv(file_path, data):
    """Write the round-wise metrics data to a CSV file."""
    with open(file_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Round", "Accuracy", "Precision", "Recall", "F1-Score"])
        for row in data:
            writer.writerow(row)

def main():
    # Ensure the 'Datasets' folder exists
    os.makedirs("Datasets", exist_ok=True)

    # Generate and save data for each client
    for i in range(1, 5):
        file_name = f"data{i}.csv"
        file_path = os.path.join("Datasets", file_name)

        # Generate dummy data for 20 rounds
        dummy_data = generate_dummy_data(num_rounds=20)

        # Write to CSV
        write_csv(file_path, dummy_data)

    print("Dummy CSV files created successfully in the 'Datasets' folder.")

if __name__ == "__main__":
    main()
