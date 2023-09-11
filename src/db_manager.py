import requests
import psycopg2


class DBManager:
    HH_EMPLOYERS = 'https://api.hh.ru/employers'

    def get_companies_and_vacancies_count(self, company_lst: list) -> dict:
        """
        Returns dict of companies and vacancies' count
        """
        company_dict = {}
        for company in company_lst:
            company_data = requests.get(self.HH_EMPLOYERS + f"?text={company.lower()}").json()
            primary_info = company_data["items"][0]

            company_dict[primary_info["name"]] = len(requests.get(primary_info["vacancies_url"]).json()["items"])

        return company_dict

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass




