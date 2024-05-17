import pandas as pd
import matplotlib.pyplot as plt

def create_histogram(age_ranges, title, ylabel, ax, rotate=False):
    ax.bar(age_ranges.keys(), age_ranges.values())
    ax.set_title(title)
    ax.set_xlabel("Fascia d'età")
    ax.set_ylabel(ylabel)
    if rotate:
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
    
def inc_range(a_ranges, age):
    for age_range in a_ranges.keys():
        if is_age_in_range(age, age_range):
            a_ranges[age_range] += 1
    
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
age_ranges_6 = {
    "(15, 20)": 0,
    "(21, 26)": 0,
    "(27, 32)": 0,
    "(33, 38)": 0,
    "(39, 44)": 0,
    "(45, 50)": 0, 
    "(51, 56)": 0, 
    "(57, 62)": 0, 
    "(63, 68)": 0, 
    "(69, 74)": 0,  
    "(75, 80)": 0,
}

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

age_ranges_10 = {
    "(15, 24)": 0, 
    "(25, 34)": 0, 
    "(35, 44)": 0, 
    "(45, 54)": 0, 
    "(55, 64)": 0, 
    "(65, 74)": 0, 
    "(75, 84)": 0,
}

age_ranges_11 = {
    "(15, 25)": 0, 
    "(26, 36)": 0, 
    "(37, 47)": 0, 
    "(48, 58)": 0, 
    "(59, 69)": 0, 
    "(70, 80)": 0,
}

age_ranges_12 = {
    "(15, 26)": 0, 
    "(27, 38)": 0, 
    "(39, 50)": 0, 
    "(51, 62)": 0,
    "(63, 74)": 0,
    "(74, 85)": 0,
}

#calcolo il numero di record in ogni fascia d'età
for row in df.itertuples():
    age = row.age
    
    for year_range in [5, 6, 7, 8, 9, 10, 11, 12]:
        inc_range(eval(f"age_ranges_{year_range}"), age)


#creo altri due dictionaries che contengono per ogni fascia, il numero di persone che hanno eseguito il test
age_ranges_5_div20 = {key: value / 20 for key, value in age_ranges_5.items()}
age_ranges_6_div20 = {key: value / 20 for key, value in age_ranges_6.items()}
age_ranges_7_div20 = {key: value / 20 for key, value in age_ranges_7.items()}
age_ranges_8_div20 = {key: value / 20 for key, value in age_ranges_8.items()}
age_ranges_9_div20 = {key: value / 20 for key, value in age_ranges_9.items()}
age_ranges_10_div20 = {key: value / 20 for key, value in age_ranges_10.items()}
age_ranges_11_div20 = {key: value / 20 for key, value in age_ranges_11.items()}
age_ranges_12_div20 = {key: value / 20 for key, value in age_ranges_12.items()}


#ciclo per creare coppie di istogrammi e mostrarli
for year_range in [5, 6, 7, 8, 9, 10, 11, 12]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    create_histogram(eval(f"age_ranges_{year_range}"),
                      f"Istogramma per fasce d'età ({year_range} anni)",
                      "Numero di record", ax1, rotate=True)
    create_histogram(eval(f"age_ranges_{year_range}_div20"),
                      f"Istogramma per fasce d'età ({year_range} anni)",
                      "Numero di persone", ax2, rotate=True)

    #stampo numero record e di persone in ogni fascia
    print_ranges(eval(f"age_ranges_{year_range}"), year_range, True)
    print_ranges(eval(f"age_ranges_{year_range}_div20"), year_range, False)
    print('\n')
    plt.show()