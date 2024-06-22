import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from rl import rl

yrs = ["2021", "2022", "2023"]


def show_plot(yr):
    data = pd.read_json(f"data/TNMC-PR-LIST/{yr}/TNMC-PR-LIST-{yr}.json")
    sns.histplot(x='mark', data=data, kde=True, hue='comm')
    plt.title(f"TN RANKLIST - {yr}")
    plt.show()


def gen_data(yr):
    rl(map=f"assets/docs/rl-maps/TNMC-PR-LIST-{yr}.map.json",
       rlist=f"assets/docs/TNMC-PR-LIST-{yr}.pdf",
       file_name=f"data/TNMC-PR-LIST/{yr}/TNMC-PR-LIST-{yr}.json")


def gen_show_plot(yr):
    gen_data(yr)
    show_plot(yr)
    
