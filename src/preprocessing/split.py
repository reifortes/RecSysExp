from sklearn.model_selection import train_test_split
from src.preprocessing.preprocessing import AbstractPreProcessing


"""
Estrategias de Fold:

K-Fold
StratifiedKFold
GroupKFold
ShuffleSplit
StratifiedShuffleSplit
GroupShuffleSplit
LeaveOneOut
LeavePOut

"""

class SplitProcessing(AbstractPreProcessing):
    def __init__(self, parameters: dict):
        """
        
        """
        super().__init__()
        print(parameters)
        self.test_size = parameters['test_size']
        self.train_size = parameters['train_size']
        self.random_state = parameters['random_state']
        self.shuffle = parameters['shuffle']
        self.stratify = parameters['stratify']


    def pre_processing(self, data, **kwargs):
        """

        @param **kwargs:
        @param data:
        @return:
        """
        y = data['rating']
        X = data.drop(columns = ['rating'], axis=1)

        print(data)
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            train_size=self.train_size,
            test_size=self.test_size,
            random_state=self.random_state,
            shuffle=self.shuffle,
            stratify=None)

        return X_train, X_test, y_train, y_test
