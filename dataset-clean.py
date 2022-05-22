import pandas as pd

#ISOT Merging and Adding Labels column

ISOT_dataset_fake = pd.read_csv(".\\Datasets\\Original Downloads\\ISOT\\Fake.csv")
ISOT_dataset_true = pd.read_csv(".\\Datasets\\Original Downloads\\ISOT\\True.csv")

ISOT_dataset_fake['label'] = 0
ISOT_dataset_true['label'] = 1

print(ISOT_dataset_fake.head())
print(ISOT_dataset_true.head())

ISOT_pair = [ISOT_dataset_true,ISOT_dataset_fake]

ISOT_merged = pd.concat(ISOT_pair)

print(ISOT_merged.tail())