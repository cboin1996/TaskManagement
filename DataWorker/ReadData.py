import os
import json
from DataWorker import DataPrinter

def read_Data(firstType={}):
    pathToDirectory= os.path.dirname(os.path.realpath(__file__))
    pathToDatabase = os.path.join(pathToDirectory, 'TaskDatabase.json')

    with open(pathToDatabase, "r") as read_file:

        try:
            TaskData = json.load(read_file)

        except:
            print('Database is empty.')
            dataType = input('Enter a Data Type: ')
            firstType.update({'type':dataType})

            with open(pathToDatabase, 'w') as out_file:
                json.dump(firstType, out_file)

            TaskData = json.load(read_file)

    return pathToDatabase

def get_types(pathToDatabase):

    with open(pathToDatabase, 'r') as read_file:
        TaskData = json.load(read_file)

        DataPrinter.PrintDictionaryKeysAndValues(TaskData)
