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

#KDNuggets Dataset, change FAKE/REAL labels to 0/1

KDNuggets_dataset = pd.read_csv(".\\Datasets\\Original Downloads\\KDNuggets\\fake_or_real_news.csv")
KDNuggets_dataset['label'] = KDNuggets_dataset['label'].str.replace("FAKE","0")
KDNuggets_dataset['label'] = KDNuggets_dataset['label'].str.replace("REAL","1")
print(KDNuggets_dataset.head())

#FakeNewsNet

FakeNewsNet_politifact_fake = pd.read_csv(".\\Datasets\\Original Downloads\\FakeNewsNet\\PolitiFact_fake_news_content.csv")
FakeNewsNet_politifact_true = pd.read_csv(".\\Datasets\\Original Downloads\\FakeNewsNet\\PolitiFact_real_news_content.csv")
FakeNewsNet_buzzfeed_fake = pd.read_csv(".\\Datasets\\Original Downloads\\FakeNewsNet\\BuzzFeed_fake_news_content.csv")
FakeNewsNet_buzzfeed_true = pd.read_csv(".\\Datasets\\Original Downloads\\FakeNewsNet\\BuzzFeed_real_news_content.csv")

FakeNewsNet_politifact_fake = FakeNewsNet_politifact_fake[["title","text"]]
FakeNewsNet_politifact_true = FakeNewsNet_politifact_true[["title","text"]]
FakeNewsNet_buzzfeed_fake = FakeNewsNet_buzzfeed_fake[["title","text"]]
FakeNewsNet_buzzfeed_true = FakeNewsNet_buzzfeed_true[["title","text"]]

FakeNewsNet_politifact_fake['label'] = 0
FakeNewsNet_politifact_true['label'] = 1
FakeNewsNet_buzzfeed_fake['label'] = 0
FakeNewsNet_buzzfeed_true['label'] = 1

FakeNewsNet_politifact_merged = pd.concat([FakeNewsNet_politifact_fake,FakeNewsNet_politifact_true])
FakeNewsNet_buzzfeed_merged = pd.concat([FakeNewsNet_buzzfeed_fake,FakeNewsNet_buzzfeed_true])

print(FakeNewsNet_politifact_merged.tail())

#Kaggle Fake News Competition Dataset

kaggle_comp_dataset = pd.read_csv(".\\Datasets\\Original Downloads\\Fake News (Kaggle Competition)\\train.csv")
print(kaggle_comp_dataset.head()) #Appears fine as is, write to clean folder

ISOT_merged.to_csv(".\\Datasets\\Cleaned\\ISOT.csv",index=False)
Kaggle_merged.to_csv(".\\Datasets\\Cleaned\\Kaggle Fake and Real.csv",index=False)
kaggle_comp_dataset.to_csv(".\\Datasets\\Cleaned\\Kaggle Competition.csv",index=False)
KDNuggets_dataset.to_csv(".\\Datasets\\Cleaned\\KDNuggets.csv",index=False)
FakeNewsNet_politifact_merged.to_csv(".\\Datasets\\Cleaned\\FakeNewsNet Politifact.csv",index=False)
FakeNewsNet_buzzfeed_merged.to_csv(".\\Datasets\\Cleaned\\FakeNewsNet Buzzfeed.csv",index=False)
