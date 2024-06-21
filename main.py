
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#from rl import rl
#import utils

# reading the database


data = pd.read_csv("data/TNMC-PR-LIST/2023/TNMC-PR-LIST-2023.csv")

 #using only data attribute
sns.histplot(x='mark', data=data, kde=True, hue='comm')

plt.show() #rlist, file_name,vec


#def init():
    # print("Staring...")
    # rl(vec="assets/docs/rl-vec/TNMC-PR-LIST-2023.json" , rlist="assets/docs/TNMC-PR-LIST-2023.pdf", file_name="data/TNMC-PR-LIST/2023/TNMC-PR-LIST-2023.json")
    # utils.json_to_csv("data/TNMC-PR-LIST/2023/TNMC-PR-LIST-2023.json","data/TNMC-PR-LIST/2023/TNMC-PR-LIST-2023.csv")
  #utils.json_to_csv("TNMC-PR-LIST-2023.json","TNMC-PR-LIST-2023.csv")
  

