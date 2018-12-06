# Data preparation related functions

import numpy as np
import pandas as pd
import atlas_util

# Additional import
from pathlib import Path
from atlas_util import *

def createDF(path_to_folder:Path, basePath: Path):
    all_files = path_to_folder.ls()
    np.random.shuffle(all_files) # Ensure no bias from ordering
    filename = list(map(extractFileName, all_files))
    protein = list(map(extractProtein, filename))
    filt = list(map(extractFilt, filename))
    all_files = list(map(lambda x: removeBasePathAndConvertToString(basePath,x),all_files))
    src = pd.DataFrame({
        'path': all_files, 
         #'filename': filename,
        'protein': protein,
        'filt': filt
    })
    ret = src.pivot_table(index='protein', columns='filt', values='path', aggfunc='sum')
    ret = ret.reset_index()
    return ret

def prepareJoinedDataFrame(path):
    '''
    Import data and create dataframe.
    '''
    # Do the import
    train_df = createDF(path/'train', path)
    train_df.head(3)

    test_df = createDF(path/'test', path)
    test_df.head(3)

    labels_df = pd.read_csv(path/'train.csv')
    labels_df.head(2)

    # Convert Target to array
    labels_df['labels']=labels_df.Target.apply(classesStrToArray)
    # Drop original one
    labels_df = labels_df.drop(['Target'],axis=1)


    #Show result
    #display(labels_df.head(3))
    print('warinig: labels column is an array of strings...')
    print(labels_df.head(3).values)


    labels_df = labels_df.rename(columns={"Id": "protein"})
    labels_df.head()

    # Let's join!
    # NB: remember to drop the duplicate join column

    train_data_and_labels_df = train_df.join(labels_df,rsuffix='_lab')
    train_data_and_labels_df = train_data_and_labels_df.drop(['protein_lab'],axis=1)
    train_data_and_labels_df.head(3)


    #Take a look at joined columns
    train_data_and_labels_df.columns

    return (train_data_and_labels_df,train_df.columns,labels_df.columns,test_df)


def prepareClasses(train_data_and_labels_df: pd.DataFrame):
    classes = list(set(flat_list(train_data_and_labels_df.labels))) # flat and unique
    classes = sorted(classes,key=int) # sort as int
    classes

    #Create dictionary from class->idx
    classes_to_idx_dict = {x: i for i,x in enumerate(classes)}
    idx_to_classes_dict = {i: x for i,x in enumerate(classes)}

    return (classes, classes_to_idx_dict, idx_to_classes_dict)


def prepareDataset(train_data_and_labels_df,cols):
    # ### Create domain 
    train_and_valid_x = train_data_and_labels_df[cols].values
    print('train_and_valid_x: ', train_and_valid_x[:3])
    print('train_and_valid_x len: ', len(train_and_valid_x))

    # Delete 4th column - for test purpose...
    train_and_valid_x=np.delete(train_and_valid_x, 4, 1)
    train_and_valid_x.shape
    # WARNING: Y should be array of list of string labels

    train_and_valid_y = train_data_and_labels_df.labels.values
    train_and_valid_y[:3]

    type(train_and_valid_y[0][0])

    from sklearn.model_selection import train_test_split
    x_train, x_valid, y_train, y_valid = train_test_split(
        train_and_valid_x, 
        train_and_valid_y, 
        test_size=0.2, random_state=42)

    return (x_train, x_valid, y_train, y_valid)

