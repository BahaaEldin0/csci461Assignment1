import matplotlib.pyplot as plt
import model
import pandas

def plot(df):
    transaction_counts = df['transaction_type'].value_counts()

    plt.figure(figsize=(8,6))
    plt.bar(transaction_counts.index, transaction_counts.values)
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.title('Distribution of Transaction Types')
    plt.savefig('vis.png')

    model.cluster(df)