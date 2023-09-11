from abc import ABC, abstractmethod
import requests


class APIWorker(ABC):
    @abstractmethod
    def get_company_list(self, text):
        """
        method returns list of 10 companies
        """
        pass


class HeadHunterAPI(APIWorker):
    HH_VACANCIES = 'https://api.hh.ru/vacancies'

    def get_company_list(self, text: str) -> list:
        vac_data = requests.get(self.HH_VACANCIES + f"?text={text.lower()}").json()
        primary_info = vac_data["items"]
        companies_list = [vacancy["employer"]["name"] for vacancy in primary_info]

        return list(set(companies_list))[:10]
