import matplotlib.pyplot as plt
from calculator import *
from utils import *



def plot_dpr_graph(ac_list, dmg_list, user_ac):
    plt.bar(ac_list, dmg_list, color="#FF4747")
    plt.xlabel("КД")
    plt.ylabel("Ожидаемый урон (DPR)")

    for i, dmg in enumerate(dmg_list):
        if ac_list[i] == user_ac:
            plt.text(ac_list[i], dmg, str(dmg), ha="center", va="bottom", fontsize=14, fontweight="bold")
        else:
            plt.text(ac_list[i], dmg, str(dmg), ha="center", va="bottom", fontsize=10)
    plt.show()

def plot_dpr_comparison_graph(ac_list, dmg_list, an_dmg_list, user_ac):
    plt.plot(ac_list, dmg_list, color="#5F5FFF", label="Первое оружие")
    plt.plot(ac_list, an_dmg_list, color="#FF4747", label="Второе оружие")
    plt.xlabel("КД")
    plt.ylabel("Ожидаемый урон (DPR)")
    plt.grid(True)
    plt.legend()
    
    plt.show()





