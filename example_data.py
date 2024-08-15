# examples_data.py

from mean_median_mode import mean, mode, median

# Example datasets
dataset_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dataset_2 = [10, 20, 20, 30, 40, 40, 40, 50, 60]
dataset_3 = [4, 5, 7, 8, 9, 10, 11, 12, 13]

# Calculating Mean, Median, Mode for each dataset
print("Dataset 1:")
print("Mean:", mean(dataset_1))
print("Mode:", mode(dataset_1))
print("Median:", median(dataset_1))

print("\nDataset 2:")
print("Mean:", mean(dataset_2))
print("Mode:", mode(dataset_2))
print("Median:", median(dataset_2))

print("\nDataset 3:")
print("Mean:", mean(dataset_3))
print("Mode:", mode(dataset_3))
print("Median:", median(dataset_3))