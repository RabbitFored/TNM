
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from rl import rl
import utils

# reading the database
data = pd.read_csv("data/TNMC-PR-LIST-2023/TNMC-PR-LIST-2023.csv")

# using only data attribute
sns.histplot(x='mark', data=data, kde=True, hue='comm')

plt.show()

def init():
  #rl("docs/N23074024.pdf", "TNMC-PR-LIST-2023.json")
  #utils.json_to_csv("TNMC-PR-LIST-2023.json","TNMC-PR-LIST-2023.csv")
  print("Staring...")

