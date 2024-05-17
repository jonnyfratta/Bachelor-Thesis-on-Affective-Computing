import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import utility

data = pd.read_csv('dataset.csv')

#salvo in una lista l'elenco distinct dei titoli dei video
videos_distinct = data['video'].unique().tolist()

#creo due colonne booleane che contengono esito comparazione tra valore assegnato e valore atteso
data = utility.apply_checks(data, 'EM')

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
