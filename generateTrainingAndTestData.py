from __future__ import division

import random

def generate_splits_for_all_datasets(
                tuples_file_name = 'all_sts_tuples.semeval2015_features.txt',
                num_training_pairs_per_split = 100,
                training_percentage = 10.0):
    
    all_tuples = {}

    f = open(tuples_file_name, 'r')
    
    for line in f:
        
        line = eval(line)
        
        dataset_name = line[0]

        excluded = ['2012.msrpar-train', '2012.msrvid', \
                    '2012.onwn', '2012.smteuroparl', '2012.smtnews', \
                    '2013.fnwn', '2013.headlines', '2013.onwn', \
                    '2014.headlines', '2014.images', '2014.deft-news']
                    
        exclude_this_pair = False
        for item in excluded:
            if item in dataset_name.lower():
                exclude_this_pair = True
                break
        
        if exclude_this_pair:
            continue

        sentence_pair = line[1]
        gold_score = line[2]
        features = line[3]
        
        if dataset_name in all_tuples:
            all_tuples[dataset_name].append((sentence_pair, 
                                             (features, gold_score)))
        else:
            all_tuples[dataset_name] = [(sentence_pair, 
                                         (features, gold_score))]
                                         

    f.close()

    training_tuples_for_all_datasets = {}
    test_tuples_for_all_datasets = {}

    for dataset in sorted(all_tuples):

        training_tuples_for_all_datasets[dataset] = []
        test_tuples_for_all_datasets[dataset] = []
        
        num_tuples_in_this_dataset = len(all_tuples[dataset])
        
        if num_training_pairs_per_split != None:        
            train_indexes = \
                    sorted(random.sample(range(num_tuples_in_this_dataset),
                                         num_training_pairs_per_split))
        
        else:
            train_indexes = \
                    sorted(random.sample(range(num_tuples_in_this_dataset),
                                         int(num_tuples_in_this_dataset * 
                                             training_percentage / 100)))

        test_indexes = sorted([item for item in \
                                    range(num_tuples_in_this_dataset) \
                                if item not in train_indexes])
    
        for i in xrange(len(all_tuples[dataset])):
            
            if i in train_indexes:
                training_tuples_for_all_datasets[dataset].append(
                                                    all_tuples[dataset][i])
            elif i in test_indexes:
                test_tuples_for_all_datasets[dataset].append(
                                                    all_tuples[dataset][i])
                

    return (training_tuples_for_all_datasets, test_tuples_for_all_datasets)
            

'''
training_tuples_for_all_datasets, test_tuples_for_all_datasets = \
                                            generate_splits_for_all_datasets()

for item in training_tuples_for_all_datasets:
    print item, len(training_tuples_for_all_datasets[item]), \
                len(test_tuples_for_all_datasets[item])
'''
