import os
from DataWorker import ReadData
from DataWorker import DataPrinter
import json



def main():
    # setup the path to the task database. Here is where tasks will be saved.


    print('Welcome the Task Manager.')
    pathToDatabase = ReadData.read_Data()

    print('Here is a list of the task types.')
    ReadData.get_types(pathToDatabase)

    



    # print(TaskData)


if __name__=="__main__":
    main()
