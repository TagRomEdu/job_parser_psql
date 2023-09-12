import psycopg2


class DBManager:
    def __init__(self, db_name, params):
        self.db_name = db_name
        self.params = params

    @staticmethod
    def db_worker(sql_request: str, db_name, params) -> list:
        conn = psycopg2.connect(dbname=db_name, **params)
        with conn.cursor() as cur:
            cur.execute(sql_request)
            rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    def get_companies_and_vacancies_count(self) -> list[tuple]:
        """
        Returns list of companies and vacancies' count
        """
        return self.db_worker("SELECT company_name, open_vacancies FROM employers", self.db_name, self.params)

    def get_all_vacancies(self) -> list[tuple]:
        """
        Returns list of all vacancies in db
        """
        return self.db_worker("""
            SELECT employers.company_name, name, CONCAT(salary, ' ', currency) AS salary, vacancy_url FROM vacancies
            INNER JOIN  employers USING(company_id)
            """, self.db_name, self.params)

    def get_avg_salary(self) -> tuple:
        """
        Returns tuple with average salary
        """
        ru_salary = int(self.db_worker("SELECT AVG(salary) as ru_salary FROM vacancies WHERE currency = 'RUR'",
                                       self.db_name, self.params)[0][0])
        usd_salary = int(self.db_worker("SELECT AVG(salary) as usd_salary FROM vacancies WHERE currency = 'USD'",
                                        self.db_name, self.params)[0][0])

        return f"{ru_salary} RUR", f"{usd_salary} USD"

    def get_vacancies_with_higher_salary(self):
        """
        Returns list of vacancies with high salary
        """
        return self.db_worker("SELECT * FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies)",
                              self.db_name, self.params)

    def get_vacancies_with_keyword(self):
        pass




