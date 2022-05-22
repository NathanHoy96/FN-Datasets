import pandas as pd

#ISOT Merging and Adding Labels column

ISOT_dataset_fake = pd.read_csv(".\\Datasets\\Original Downloads\\ISOT\\Fake.csv")
ISOT_dataset_true = pd.read_csv(".\\Datasets\\Original Downloads\\ISOT\\True.csv")

ISOT_dataset_fake['label'] = 0
ISOT_dataset_true['label'] = 1

ISOT_pair = [ISOT_dataset_fake,ISOT_dataset_true]
ISOT_merged = pd.concat(ISOT_pair)

print(ISOT_merged.head())

#Fake and Real News Kaggle Dataset

Kaggle_dataset_fake = pd.read_csv(".\\Datasets\\Original Downloads\\Fake and real news dataset (Kaggle)\\Fake.csv")
Kaggle_dataset_true = pd.read_csv(".\\Datasets\\Original Downloads\\Fake and real news dataset (Kaggle)\\True.csv")

Kaggle_dataset_fake['label'] = 0
Kaggle_dataset_true['label'] = 1

Kaggle_merged = pd.concat([Kaggle_dataset_fake,Kaggle_dataset_true])
print(Kaggle_merged.head())