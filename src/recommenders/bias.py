from src.recommenders.recommender import Recommender
from lenskit.algorithms import bias

class Bias(Recommender):
    def __init__(self, parameters: dict) -> None:
        """

        """

        #Se faltar algum parâmetro obrigatório vai levantar uma exceção
        self.process_parameters(parameters)

        self.items = parameters['items']
        self.users = parameters['users']
        self.damping = parameters['damping']
        self.Bias = bias.Bias(
            items=self.items,
            users=self.users,
        )

    def process_parameters(self, parameters: dict) -> dict:
        """

        @param parameters: objeto com os parâmetros da classe
        @return: dicionário atualizado com esses mesmos parâmetros
        """

        default_keys = ['items', 'users', 'damping']
        parameters_keys = parameters.keys()

        for key in default_keys:
            if key not in parameters_keys:
                raise KeyError("A chave obrigatória {} não foi informada no arquivo de configuração".format(key))

        return parameters

    def predict_for_users(self, users, items, ratings):
        """

        @param users:
        @param items:
        @param ratings:
        @return:
        """
        return self.Bias.predict_for_user(users, items, ratings)

    def predict(self, pairs, ratings):
        """

        @param pairs:
        @param ratings:
        @return:
        """
        return self.Bias.predict(pairs, ratings)

    def recommend(self, user, n, candidates, ratings):
        """

        @param user:
        @param n:
        @param candidates:
        @param ratings:
        @return:
        """
        pass

    def get_params(self, deep=True):
        """

        @param deep:
        @return:
        """
        pass

    def fit(self, rating, **kwargs):
        """

        @param rating:
        @param kwargs:
        @return:
        """
        self.Bias.fit(rating)

    def transform(self, rating):
        return self.Bias.transform(rating)