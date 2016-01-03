import argparse
import csv
import pickle
import os

_parser = argparse.ArgumentParser(description='Processes training set.')
_parser.add_argument('--file', type=str, required=True,
                     help='filename containing training set or pickled file')
_parser.add_argument('--save', action='store_true',
                     help='save the pickled data to particular file')
_parser.add_argument('--load', action='store_true',
                     help='load the pickled data from particular file')


def load(filename):
    """Loads elements from Pickle file

       Args:
       - Filename - str of location

       Return:
        Tuple with:
         - Lists of Activity Names
         - Lists of Activity Types
    """
    assert type(filename) == str, 'Filename must be a str'
    with open(filename, 'rb') as f:
        elements = pickle.load(f)

    assert type(elements) == tuple, 'Element is not valid!'
    assert len(elements) == 2, 'Element is not valid!'
    assert len(elements[0]) == len(elements[1]), 'Element is not valid!'
    assert type(elements[0]) == list, 'Element is not valid!'
    assert type(elements[1]) == list, 'Element is not valid!'

    return elements


def save(elements, filename):
    """Pickles elements to a particular filename

       Args:
       - elements: tuple(list, list)
       - filename: str of location to save serialization

       Return:
        None
    """
    assert type(filename) == str, 'Filename must be a str'
    assert filename.endswith('.pkl'), 'File must be pkl!'
    assert type(elements) == tuple, 'Element must be a tuple!'
    assert len(elements) == 2, 'Tuple must be of length 2!'
    assert len(elements[0]) == len(elements[1]), 'Elements do not have same length!'
    assert type(elements[0]) == list, 'First element must be a list!'
    assert type(elements[1]) == list, 'Second element must be a list!'
    with open(filename, 'wb') as f:
        pickle.dump(elements, f)
    return


def extractor(filename):
    """Return a tuple containing two lists of the Activity title and
       Activity type(s)

       Args:
       - filename: string of the filename

       Returns:
        Tuple with:
         - Lists of Activity Names
         - Lists of Activity Types
    """
    assert filename.endswith('.csv'), 'File must be a csv file!'

    activity_names = []
    activity_types = []
    with open(filename, 'r') as cas_file:
        cas_reader = csv.reader(cas_file, delimiter=',')
        for row in cas_reader:
            activity_names.append(row[0])
            activity_types.append([tp for tp in row[1:] if tp])
    return (activity_names, activity_types)


if __name__ == '__main__':
    parse_args = _parser.parse_args()
    if parse_args.save:
        csv_file = parse_args.file
        data = extractor(csv_file)
        save(data, os.path.realpath(
             os.path.join(os.path.dirname(csv_file), 'data.pkl')))
    elif parse_args.load:
        pkl_file = parse_args.file
        data = load(pkl_file)
    else:
        print('Nothing happened')
