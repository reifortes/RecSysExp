from abc import abstractmethod
import importlib
from src.preprocessing.preprocessing import PreProcessing, AbstractPreProcessing
from src.preprocessing.encoding import EncodingProcessing
from src.preprocessing.split import SplitProcessing
from src.preprocessing.normalize import NormalizeProcessing
from src.preprocessing.discretize import DiscretizeProcessing

"""
1. Generalizar as fabricas em uma classe
"""


class Creator:

    @abstractmethod
    def create(self) -> AbstractPreProcessing:
        pass


class ProcessingFactory(Creator):
    def __init__(self, parameters: dict):
        self.parameters = self._handle_config_obj(parameters)

    def _handle_config_obj(self, parameters: dict) -> dict:
        """
        Tem como objetivo verificar a validade do arquivo de configuração para a execução
        das etapas de pré-processamento

        @type parameters: object
        @param config_obj:
        @return: object or None
        """

        stages = parameters['stages']

        is_empty = self._is_stages_empty(stages)
        if is_empty:
            raise Exception("Não foram inseridos estágios de pré-processamento, esse array não deve estar vazio")

        return parameters

    def _is_stages_empty(self, stages: list) -> bool:
        """
        Verifica se a lista de estágios de preprocessamento está vazia

        @param stages:
        @return:
        """
        if len(stages) == 0:
            return True

        return False

    @property
    def create(self):
        """
        Cria uma instância de um objeto do tipo PreProcessing

        @return: object
        """
        instances = []
        for stages in self.parameters:
            module = importlib.import_module('src.preprocessing')
            class_ = getattr(module, stages['class_name'])
            instance = class_(stages['parameters'])
            instances.append(instance)

        return instances
