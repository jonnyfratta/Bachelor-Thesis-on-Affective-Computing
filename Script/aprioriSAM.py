import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import utility

data = pd.read_csv('dataset.csv')

#salvo in una lista l'elenco distinct dei titoli dei video
videos_distinct = data['video'].unique().tolist()

#creo due colonne booleane che contengono esito comparazione tra valore assegnato e valore atteso
data = utility.apply_checks(data, 'SAM')

for video in videos_distinct:
    video_records = data[data['video'] == video].copy()
    
    #creo colonna contenente per ogni record il range d'età di appartenenza
    video_records['age_interval'] = pd.cut(video_records['age'], bins=utility.bins_age, labels=utility.labels_age, right=False)

    #codifica a caldo delle colonne interessate dall'algoritmo
    data_encoded = pd.get_dummies(video_records[['age_interval', 'correct_values', 'incorrect_values']], prefix='', prefix_sep='')

    #applico algorimto Apriori
    rules = utility.find_association_rules(data_encoded)

    #filtro le regole che hanno come antecedente un range di età
    rules_with_age_interval = rules[rules['antecedents'].astype(str).str.contains(r'\d{2}-\d{2}')]

    #stampo regole
    utility.print_association_rules(video, rules_with_age_interval)




# correct_values = ranges.correct_values

# def check_correct_values(row):
#     video = row['video']
#     sam_valence = row['SAM-Valence']
#     sam_arousal = row['SAM-Arousal']
#     if video in correct_values:
#         valence_range = correct_values[video]['SAM-Valence']
#         arousal_range = correct_values[video]['SAM-Arousal']
#         if valence_range[0] <= sam_valence <= valence_range[1] and arousal_range[0] <= sam_arousal <= arousal_range[1]:
#             return True
#     return False

# def check_incorrect_values(row):
#     video = row['video']
#     sam_valence = row['SAM-Valence']
#     sam_arousal = row['SAM-Arousal']
#     if video in correct_values:
#         valence_range = correct_values[video]['SAM-Valence']
#         arousal_range = correct_values[video]['SAM-Arousal']
#         if valence_range[0] > sam_valence or sam_valence > valence_range[1] or arousal_range[0] > sam_arousal or sam_arousal > arousal_range[1]:
#             return True
#     return False

# # Applica la funzione ai record del DataFrame
# data['correct_values'] = data.apply(check_correct_values, axis=1)
# data['incorrect_values'] = data.apply(check_incorrect_values, axis=1)

# #salvo i titoli dei video in una lista
# video_distinti = data['video'].unique().tolist()

# for video in video_distinti:
#     #filtro i record corrispondenti al titolo del video
#     video_records = data[data['video'] == video].copy()
    
#     #suddivisione età in intervalli di 8 anni
#     bins_age = list(range(15, 80, 8)) #creo intervalli di 8 anni da 15 a 79
#     labels_age = ['{}-{}'.format(i, i + 7) for i in range(15, 72, 8)]  #creo etichette intervalli da 15 a 72 (devono essere una in meno rispetto ai bins)
#     video_records.loc[:, 'age_interval'] = pd.cut(video_records['age'], bins=bins_age, labels=labels_age, right=False) #creo nuova colonna contenente per ogni record la fascia  di età di appartenenza

#     #codifica hot per le colonne interessate dall'algoritmo
#     data_encoded = pd.get_dummies(video_records[['age_interval', 'correct_values', 'incorrect_values']], prefix = '', prefix_sep = '')
    
#     #ricerca itemset frequenti
#     frequent_itemsets = apriori(data_encoded, min_support = 0.004, use_colnames = True)

#     #ricerca regole di associazione con confidence maggiore del 98% e lift maggiore di 1.01
#     rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1.01)
#     rules = rules[rules['confidence'] >= 0.98]

#     #filtraggio regole che hanno un intervallo d'età nell'antecedente
#     rules_with_age_interval = rules[rules['antecedents'].astype(str).str.contains(r'\d{2}-\d{2}')]

#     pd.set_option('display.expand_frame_repr', False)   #opzione per visualizzare tutte le colonne senza andare a capo
#     pd.set_option('display.max_colwidth', 40)   #opzione per ridurre lo spazio tra le colonne

#     #stampa di tutte le regole associative
#     with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#         print(video+':')
#         print(rules_with_age_interval)
#         print('\n')
