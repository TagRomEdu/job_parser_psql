from abc import ABC, abstractmethod
import requests


class APIWorker(ABC):
    @abstractmethod
    def get_vacancies(self, text):
        """
        method returns list of vacancies
        """
        pass


class HeadHunterAPI(APIWorker):
    HH_VACANCIES = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, text: str) -> dict:
        request = requests.get(self.HH_VACANCIES + f"?text={text.lower()}").json()
        return request
