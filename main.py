from src.api_worker import HeadHunterAPI
from utils import create_db, save_data_company_to_db, save_data_vacancies_to_db
from config import config


def main():
    params = config()
    create_db('job_data', params)

    job_parser = HeadHunterAPI()
    company_list = job_parser.get_companies_data(job_parser.get_company_list('python'))
    save_data_company_to_db(company_list, 'job_data', params)
    for company in company_list:
        save_data_vacancies_to_db(job_parser.get_vacancies(company[0]), 'job_data', params)


if __name__ == '__main__':
    main()