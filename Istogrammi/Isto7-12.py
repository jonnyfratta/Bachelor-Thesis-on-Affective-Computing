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

age_ranges_7 = {
    "(15, 21)": 0,
    "(22, 28)": 0,
    "(29, 35)": 0,
    "(36, 42)": 0,
    "(43, 49)": 0,
    "(50, 56)": 0,
    "(57, 63)": 0, 
    "(64, 70)": 0, 
    "(71, 76)": 0, 
    "(77, 83)": 0,
}

age_ranges_12 = {
    "(15, 26)": 0, 
    "(27, 38)": 0, 
    "(39, 50)": 0, 
    "(51, 62)": 0,
    "(63, 74)": 0,
    "(74, 85)": 0,
}

# Calcolo il numero di persone in ogni fascia d'età
for row in df.itertuples():
    age = row.age

    for age_range in age_ranges_7.keys():
        if is_age_in_range(age, age_range):
            age_ranges_7[age_range] += 1

    for age_range in age_ranges_12.keys():
        if is_age_in_range(age, age_range):
            age_ranges_12[age_range] += 1

#creo altri due dictionaries che contengono per ogni fascia, il numero di persone che hanno eseguito il test
age_ranges_7_div20 = {key: value / 20 for key, value in age_ranges_7.items()}
age_ranges_12_div20 = {key: value / 20 for key, value in age_ranges_12.items()}

# Creo i subplot per i due istogrammi
fig, ((ax1, ax2), (ax3, ax4)) = subplots(2, 2, figsize=(10, 7))

#Creo istogrammi con fasce di 7 anni
create_histogram(age_ranges_7, ax1, "Istogramma per fasce d'età (7 anni)", "Numero di record", True)
create_histogram(age_ranges_7_div20, ax2, "Istogramma per fasce d'età (7 anni)", "Numero di persone", True) 

#Creo istogrammi con fasce di 12 anni
create_histogram(age_ranges_12, ax3, "Istogramma per fasce d'età (12 anni)", "Numero di record")
create_histogram(age_ranges_12_div20, ax4, "Istogramma per fasce d'età (12 anni)", "Numero di persone")

#stampo numero record in ogni fascia
print_ranges(age_ranges_7, 7, True)
print_ranges(age_ranges_12, 12, True)

print('\n')

#stampo numero persone in ogni fascia
print_ranges(age_ranges_7_div20, 7, False)
print_ranges(age_ranges_12_div20, 12, False)

plt.show()

