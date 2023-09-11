from abc import ABC, abstractmethod
import requests


class APIWorker(ABC):
    @abstractmethod
    def get_company_list(self, text):
        """
        method returns list of 10 companies
        """
        pass

    @abstractmethod
    def get_companies_data(self, companies_list):
        """
        method returns info about companies
        """
        pass

    @abstractmethod
    def get_vacancies(self, employer_id):
        """
        method returns company's vacancies
        """
        pass


class HeadHunterAPI(APIWorker):
    HH_VACANCIES = 'https://api.hh.ru/vacancies'
    HH_EMPLOYERS = 'https://api.hh.ru/employers'

    def get_company_list(self, text: str) -> list:

        vac_data = requests.get(self.HH_VACANCIES + f"?text={text.lower()}").json()
        primary_info = vac_data["items"]
        companies_list = [vacancy["employer"]["name"] for vacancy in primary_info]

        return list(set(companies_list))[:10]

    def get_companies_data(self, companies_list: list) -> list:

        company_info_list = []

        for company in companies_list:
            company_data = requests.get(self.HH_EMPLOYERS + f"?text={company.lower()}").json()
            primary_info = company_data["items"][0]
            company_info = (primary_info["id"],
                            primary_info["name"],
                            primary_info["alternate_url"],
                            primary_info["open_vacancies"])

            company_info_list.append(company_info)

        return company_info_list

    def get_vacancies(self, employer_id: int) -> list:

        request = requests.get(self.HH_VACANCIES + f"?employer_id={employer_id}").json()
        vac_lst = request["items"]

        vacancy_info_list = []

        for vacancy in vac_lst:
            try:
                vacancy_info = (vacancy["id"],
                                vacancy["name"],
                                vacancy["area"]["name"],
                                vacancy["employer"]["id"],
                                vacancy["salary"]["from"],
                                vacancy["salary"]["currency"],
                                vacancy["published_at"],
                                vacancy["snippet"]["requirement"],
                                vacancy["snippet"]["responsibility"],
                                vacancy["apply_alternate_url"])
                vacancy_info_list.append(vacancy_info)
            except TypeError:
                vacancy_info = (vacancy["id"],
                                vacancy["name"],
                                vacancy["area"]["name"],
                                vacancy["employer"]["id"],
                                vacancy["salary"],
                                vacancy["published_at"],
                                vacancy["snippet"]["requirement"],
                                vacancy["snippet"]["responsibility"],
                                vacancy["apply_alternate_url"])
                vacancy_info_list.append(vacancy_info)

        return vacancy_info_list
