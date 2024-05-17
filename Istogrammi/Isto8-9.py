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

age_ranges_8 = {
    "(15, 22)": 0,
    "(23, 30)": 0,
    "(31, 38)": 0,
    "(39, 46)": 0,
    "(47, 54)": 0,
    "(55, 62)": 0,
    "(63, 70)": 0,
    "(71, 77)": 0,
}

age_ranges_9 = {
    "(15, 23)": 0, 
    "(24, 32)": 0, 
    "(33, 41)": 0, 
    "(42, 50)": 0,
    "(51, 59)": 0,
    "(60, 68)": 0,
    "(69, 77)": 0,
}

# Calcolo il numero di persone in ogni fascia d'età
for row in df.itertuples():
    age = row.age

    for age_range in age_ranges_8.keys():
        if is_age_in_range(age, age_range):
            age_ranges_8[age_range] += 1

    for age_range in age_ranges_9.keys():
        if is_age_in_range(age, age_range):
            age_ranges_9[age_range] += 1

#creo altri due dictionaries che contengono per ogni fascia, il numero di persone che hanno eseguito il test
age_ranges_8_div20 = {key: value / 20 for key, value in age_ranges_8.items()}
age_ranges_9_div20 = {key: value / 20 for key, value in age_ranges_9.items()}

# Creo i subplot per i due istogrammi
fig, ((ax1, ax2), (ax3, ax4)) = subplots(2, 2, figsize=(10, 7))

#Creo istogrammi con fasce di 8 anni
create_histogram(age_ranges_8, ax1, "Istogramma per fasce d'età (8 anni)", "Numero di record")
create_histogram(age_ranges_8_div20, ax2, "Istogramma per fasce d'età (8 anni)", "Numero di persone") 

#Creo istogrammi con fasce di 9 anni
create_histogram(age_ranges_9, ax3, "Istogramma per fasce d'età (9 anni)", "Numero di record")
create_histogram(age_ranges_9_div20, ax4, "Istogramma per fasce d'età (9 anni)", "Numero di persone")

#stampo numero record in ogni fascia
print_ranges(age_ranges_8, 8, True)
print_ranges(age_ranges_9, 9, True)

print('\n')

#stampo numero persone in ogni fascia
print_ranges(age_ranges_8_div20, 8, False)
print_ranges(age_ranges_9_div20, 9, False)

plt.show()

