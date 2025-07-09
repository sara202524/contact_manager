import os
import pickle

def check_file(filename):
    return os.path.exists(filename)


def read_from_file(filename):
    if check_file(filename):
        file = open(filename, "rt")
        data_list = pickle.load(file)
        file.close()
        return data_list
    else:
        file = open(filename, "wt")
        file.close()
        return []

def write_to_file(filename, data_list):
    file = open(filename, "wt")
    pickle.dump(data_list, file)
    file.close()
