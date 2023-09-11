from abc import ABC, abstractmethod
import os
import requests


class APIWorker(ABC):
    API_SJ = os.getenv('API_SuperJob')
    HH_VACANCIES = 'https://api.hh.ru/vacancies'
    SJ_VACANCIES = 'https://api.superjob.ru/2.0/vacancies'

    headers_sj = {'X-Api-App-Id': API_SJ}

    @abstractmethod
    def get_vacancies(self, text):
        """
        method returns list of vacancies
        """
        pass


class HeadHunterAPI(APIWorker):

    def get_vacancies(self, text: str) -> dict:
        request = requests.get(self.HH_VACANCIES + f"?text={text.lower()}").json()
        return request


class SuperJobAPI(APIWorker):

    def get_vacancies(self, text: str) -> dict:
        req_str = self.SJ_VACANCIES + f"?keyword={text.lower()}"
        request = requests.get(req_str, headers=self.headers_sj).json()
        return request
