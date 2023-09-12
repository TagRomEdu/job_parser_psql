from config import config
from src.api_worker import HeadHunterAPI
from src.db_manager import DBManager
from utils import create_db, save_data_company_to_db, save_data_vacancies_to_db


def main():
    params = config()
    create_db('job_data', params)

    job_parser = HeadHunterAPI()
    
    company_list = job_parser.get_companies_data(job_parser.get_company_list('python'))
    save_data_company_to_db(company_list, 'job_data', params)
    for company in company_list:
        save_data_vacancies_to_db(job_parser.get_vacancies(company[0]), 'job_data', params)

    manager = DBManager('job_data', params)

    companies = manager.get_companies_and_vacancies_count()
    vacancies = manager.get_all_vacancies()
    average_salary = manager.get_avg_salary()
    best_vacancies = manager.get_vacancies_with_higher_salary()
    k_word = input("Enter keyword: ")
    vac_by_keyword = manager.get_vacancies_with_keyword(k_word)

    print(f"""
О компаниях и вакансиях:\n{companies}\n\n\nСписок всех вакансий:\n{vacancies}\n\n\n
Средняя зп:\n{average_salary}\n\n\nЛучшие из лучших:\n{best_vacancies}\n\n\n
По ключевомe слову:\n{vac_by_keyword}
    """)


if __name__ == '__main__':
    main()
