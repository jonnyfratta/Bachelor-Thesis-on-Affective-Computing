import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots

def create_histogram(age_ranges, ax, title, ylabel, rotate=False):
    ax.bar(age_ranges.keys(), age_ranges.values())
    ax.set_title(title)
    ax.set_xlabel("Fascia d'età")
    ax.set_ylabel(ylabel)
    if(rotate):
        ax.tick_params(axis='x', rotation=35)
        
def is_age_in_range(age, age_range):
    bound = age_range[1:-1].split(",")
    lower = int(bound[0])
    upper = int(bound[1])
    return lower <= age <= upper

def print_ranges(age_ranges, anni, record):
    print(f"Range da {anni} anni:")
    i = tot = 0
    for age_range, count in age_ranges.items():
        print(f"Range {i+1}: {count}")
        i += 1
        tot += count
    if(record): 
        what = "record"
    else: 
        what = "persone"
        
    print(f"\nTotale {what}: {tot}\n")

# Importa dati da file CSV
df = pd.read_csv('dataset.csv')

age_ranges_5 = {
    "(15, 19)": 0,
    "(20, 24)": 0,
    "(25, 29)": 0,
    "(30, 34)": 0,
    "(35, 39)": 0,
    "(40, 44)": 0,
    "(45, 49)": 0, 
    "(50, 54)": 0, 
    "(55, 59)": 0, 
    "(60, 64)": 0, 
    "(65, 69)": 0, 
    "(70, 74)": 0, 
    "(75, 79)": 0,
}

age_ranges_10 = {
    "(15, 24)": 0, 
    "(25, 34)": 0, 
    "(35, 44)": 0, 
    "(45, 54)": 0, 
    "(55, 64)": 0, 
    "(65, 74)": 0, 
    "(75, 84)": 0,
}

# Calcolo il numero di persone in ogni fascia d'età
for row in df.itertuples():
    age = row.age

    for age_range in age_ranges_5.keys():
        if is_age_in_range(age, age_range):
            age_ranges_5[age_range] += 1

    for age_range in age_ranges_10.keys():
        if is_age_in_range(age, age_range):
            age_ranges_10[age_range] += 1

#creo altri due dictionaries che contengono per ogni fascia, il numero di persone che hanno eseguito il test
age_ranges_5_div20 = {key: value / 20 for key, value in age_ranges_5.items()}
age_ranges_10_div20 = {key: value / 20 for key, value in age_ranges_10.items()}

# Creo i subplot per i due istogrammi
fig, ((ax1, ax2), (ax3, ax4)) = subplots(2, 2, figsize=(10, 7))

#Creo istogrammi con fasce di 5 anni
create_histogram(age_ranges_5, ax1, "Istogramma per fasce d'età (5 anni)", "Numero di record", True)
create_histogram(age_ranges_5_div20, ax2, "Istogramma per fasce d'età (5 anni)", "Numero di persone", True) 

#Creo istogrammi con fasce di 10 anni
create_histogram(age_ranges_10, ax3, "Istogramma per fasce d'età (10 anni)", "Numero di record")
create_histogram(age_ranges_10_div20, ax4, "Istogramma per fasce d'età (10 anni)", "Numero di persone")

#stampo numero record in ogni fascia
print_ranges(age_ranges_5, 5, True)
print_ranges(age_ranges_10, 10, True)

print('\n')

#stampo numero persone in ogni fascia
print_ranges(age_ranges_5_div20, 5, False)
print_ranges(age_ranges_10_div20, 10, False)

plt.show()
