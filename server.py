import matplotlib.pyplot as plt
from collections import defaultdict

# A global dictionary to store metrics from clients:
#   metrics_storage[round] = [(acc1, prec1, rec1, f11), (acc2, prec2, rec2, f12), ...]
metrics_storage = defaultdict(list)

def receive_metrics(client_id, round_num, accuracy, precision, recall, f1_score):
    """
    Simulate receiving metrics from a client for a given round.
    We'll store them in the global metrics_storage dictionary.
    """
    metrics_storage[round_num].append((accuracy, precision, recall, f1_score))

def aggregate_and_plot():
    """
    Once all clients have sent their data, we can aggregate
    and plot the round-wise average metrics across all clients.
    """
    # Sort rounds to ensure we process them in ascending order
    sorted_rounds = sorted(metrics_storage.keys())

    avg_accs = []
    avg_precs = []
    avg_recs = []
    avg_f1s = []

    for r in sorted_rounds:
        # Gather all metrics from each client for round r
        round_values = metrics_storage[r]
        count = len(round_values)

        # Sum them up
        sum_acc = sum(m[0] for m in round_values)
        sum_prec = sum(m[1] for m in round_values)
        sum_rec = sum(m[2] for m in round_values)
        sum_f1 = sum(m[3] for m in round_values)

        # Compute averages
        avg_accs.append(sum_acc / count)
        avg_precs.append(sum_prec / count)
        avg_recs.append(sum_rec / count)
        avg_f1s.append(sum_f1 / count)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(sorted_rounds, avg_accs, marker='o', label='Accuracy')
    plt.plot(sorted_rounds, avg_precs, marker='o', label='Precision')
    plt.plot(sorted_rounds, avg_recs, marker='o', label='Recall')
    plt.plot(sorted_rounds, avg_f1s, marker='o', label='F1-Score')

    plt.ylim([0, 1.0])
    plt.xlabel('Round')
    plt.ylabel('Metric Score')
    plt.title('Round-wise Average Metrics Scores Across Clients')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    """
    In a real-world scenario, you'd wait for or collect data from clients
    over the network. Here, we do not do anything in main().
    The aggregation and plotting might be triggered once all data is received.
    """
    print("Server is ready to receive metrics...")

if __name__ == "__main__":
    main()
