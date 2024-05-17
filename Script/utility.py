import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#suddivisione età in intervalli di 8 anni
bins_age = list(range(15, 80, 8)) #creo intervalli di 8 anni da 15 a 79
labels_age = ['{}-{}'.format(i, i + 7) for i in range(15, 72, 8)] #creo etichette intervalli da 15 a 72 (devono essere una in meno rispetto ai bins)

#funzione che confronta valore assegnato nella colonna emotion con quello corretto
def em_check_correct_values(row, corr):
    video = row['video']
    emotion = row['Emotion']
    right_em = correct_emotion[video]['Emotion']
    if corr:
        if emotion == right_em:
            return True
    else:
        if emotion != right_em:
            return True
    return False

#funzione che confronta valori assegnato nelle colonne Valence e Arousal del test desiderato, con il range corretto di valori
def check_correct_values(row, column1, column2, corr):
    video = row['video']
    valence = row[column1]
    arousal = row[column2]
    emotion = row['Emotion']
    level = row['Level']
    target = (emotion, level)
    
    valence_range = correct_intervals[target][column1]
    arousal_range = correct_intervals[target][column2]
    
    if corr:
        if valence_range[0] <= valence <= valence_range[1] and arousal_range[0] <= arousal <= arousal_range[1]:
            return True
    else:
        if valence_range[0] > valence or valence > valence_range[1] or arousal_range[0] > arousal or arousal > arousal_range[1]:
            return True
    return False

#funzione che crea colonne correct_values e incorrect_values
def apply_checks(data, check_func):
    if check_func == 'EM':
        data['correct_values'] = data.apply(em_check_correct_values, args=(True,), axis=1)
        data['incorrect_values'] = data.apply(em_check_correct_values, args=(False,), axis=1)
    elif check_func == 'AS':
        data['correct_values'] = data.apply(check_correct_values, args=('AS-Valence', 'AS-Arousal', True), axis=1)
        data['incorrect_values'] = data.apply(check_correct_values, args=('AS-Valence', 'AS-Arousal', False), axis=1)
    elif check_func == 'SAM':
        data['correct_values'] = data.apply(check_correct_values, args=('SAM-Valence', 'SAM-Arousal', True), axis=1)
        data['incorrect_values'] = data.apply(check_correct_values, args=('SAM-Valence', 'SAM-Arousal', False), axis=1)
    return data


#funzione che applica algoritmo apriori
def find_association_rules(data, min_support=0.01, min_confidence=0.98, min_lift=1.01):
    frequent_itemsets = apriori(data, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_lift)
    return rules[rules['confidence'] >= min_confidence]

#funzione di stampa
def print_association_rules(video, rules):
    #opzione per visualizzare tutte le colonne senza andare a capo
    pd.set_option('display.expand_frame_repr', False)
    print(video + ':')
    print(rules)
    print('\n')
    
    
correct_emotion = {
    #Happiness
    'Laereo_piu_pazzo_del_mondo'      : {'Emotion': 'happiness'},
    'Harry_ti_presento_Sally-Orgasmo' : {'Emotion': 'happiness'},
    'Lassu_qualcuno_e_impazzito'      : {'Emotion': 'happiness'},
    
    #Sadness
    'Papa_ho_trovato_un_amico'        : {'Emotion': 'sadness'},
    'Il_sapore_della_vittoria'        : {'Emotion': 'sadness'},
    'The_Prestige-Morte_di_Julia'     : {'Emotion': 'sadness'},
    'La_sottile_linea_rossa'          : {'Emotion': 'sadness'},
    
    #Anger
    'Gandhi'                          : {'Emotion': 'anger'},
    'La_mia_guardia_del_corpo'        : {'Emotion': 'anger'},
    'Crash-Contatto_fisico'           : {'Emotion': 'anger'},
    
    #Fear
    'Il_cigno_nero'                   : {'Emotion': 'fear'},
    'Mulholland_Drive'                : {'Emotion': 'fear'},
    'Silent_Hill'                     : {'Emotion': 'fear'},
    
    #Anxiety
    'IT_1-Trailer'                    : {'Emotion': 'anxiety'},
    'IT_2-Trailer'                    : {'Emotion': 'anxiety'},
    'Gli_Intoccabili-Stazione'        : {'Emotion': 'anxiety'},
    'The_blair_witch_project'         : {'Emotion': 'anxiety'},
    
    #Disgust
    'Lesorcista'                      : {'Emotion': 'disgust'},
    'The_Hannibal'                    : {'Emotion': 'disgust'},
    'OldBoy'                          : {'Emotion': 'disgust'},
}

correct_intervals = {
    #anger
    ('anger', 1) : {'AS-Valence':[0.1, 0.3], 'AS-Arousal':[0.6, 0.80], 'SAM-Valence':[1, 3], 'SAM-Arousal':[6, 8]},
    ('anger', 2) : {'AS-Valence':[0.1, 0.3], 'AS-Arousal':[0.7, 0.85], 'SAM-Valence':[1, 3], 'SAM-Arousal':[7, 8]},
    ('anger', 3) : {'AS-Valence':[0.1, 0.3], 'AS-Arousal':[0.8, 0.90], 'SAM-Valence':[1, 3], 'SAM-Arousal':[8, 9]}, 
    
    #anxiety
    ('anxiety', 1) : {'AS-Valence':[0.1, 0.30], 'AS-Arousal':[0.5, 0.7], 'SAM-Valence':[1, 3], 'SAM-Arousal':[5, 7]},
    ('anxiety', 2) : {'AS-Valence':[0.2, 0.45], 'AS-Arousal':[0.6, 0.8], 'SAM-Valence':[2, 4], 'SAM-Arousal':[6, 8]},
    ('anxiety', 3) : {'AS-Valence':[0.35, 0.6], 'AS-Arousal':[0.7, 0.9], 'SAM-Valence':[3, 6], 'SAM-Arousal':[7, 9]}, 
    
    #boredom
    ('boredom', 1) : {'AS-Valence':[0.6, 0.8], 'AS-Arousal':[0.1, 0.3], 'SAM-Valence':[6, 8], 'SAM-Arousal':[1, 3]}, 
    ('boredom', 2) : {'AS-Valence':[0.3, 0.6], 'AS-Arousal':[0.1, 0.3], 'SAM-Valence':[3, 6], 'SAM-Arousal':[1, 3]},
    ('boredom', 3) : {'AS-Valence':[0.1, 0.3], 'AS-Arousal':[0.1, 0.3], 'SAM-Valence':[1, 3], 'SAM-Arousal':[1, 3]},
    
    #disgust
    ('disgust', 1) : {'AS-Valence':[0.20, 0.40], 'AS-Arousal':[0.5, 0.6], 'SAM-Valence':[2, 4], 'SAM-Arousal':[5, 6]},
    ('disgust', 2) : {'AS-Valence':[0.15, 0.30], 'AS-Arousal':[0.5, 0.6], 'SAM-Valence':[2, 3], 'SAM-Arousal':[5, 6]},
    ('disgust', 3) : {'AS-Valence':[0.10, 0.20], 'AS-Arousal':[0.5, 0.6], 'SAM-Valence':[1, 2], 'SAM-Arousal':[5, 6]}, 
    
    #fear
    ('fear', 1) : {'AS-Valence':[0.3, 0.5], 'AS-Arousal':[0.60, 0.80], 'SAM-Valence':[3, 5], 'SAM-Arousal':[6, 8]},
    ('fear', 2) : {'AS-Valence':[0.3, 0.5], 'AS-Arousal':[0.70, 0.85], 'SAM-Valence':[3, 5], 'SAM-Arousal':[7, 8]},
    ('fear', 3) : {'AS-Valence':[0.3, 0.5], 'AS-Arousal':[0.80, 0.90], 'SAM-Valence':[3, 5], 'SAM-Arousal':[8, 9]}, 
    
    #happiness
    ('happiness', 1) : {'AS-Valence':[0.7, 0.9], 'AS-Arousal':[0.3, 0.5], 'SAM-Valence':[7, 9], 'SAM-Arousal':[3, 5]},
    ('happiness', 2) : {'AS-Valence':[0.7, 0.9], 'AS-Arousal':[0.5, 0.7], 'SAM-Valence':[7, 9], 'SAM-Arousal':[5, 7]},
    ('happiness', 3) : {'AS-Valence':[0.7, 0.9], 'AS-Arousal':[0.7, 0.9], 'SAM-Valence':[7, 9], 'SAM-Arousal':[7, 9]},
    
    #sadness
    ('sadness', 1) : {'AS-Valence':[0.1, 0.3], 'AS-Arousal':[0.4, 0.6], 'SAM-Valence':[1, 3], 'SAM-Arousal':[4, 6]},
    ('sadness', 2) : {'AS-Valence':[0.1, 0.3], 'AS-Arousal':[0.3, 0.5], 'SAM-Valence':[1, 3], 'SAM-Arousal':[3, 5]},
    ('sadness', 3) : {'AS-Valence':[0.1, 0.3], 'AS-Arousal':[0.1, 0.3], 'SAM-Valence':[1, 3], 'SAM-Arousal':[1, 3]}, 
}