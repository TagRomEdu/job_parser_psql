import psycopg2


class DBManager:
    def __init__(self, db_name, params):
        self.db_name = db_name
        self.params = params

    def get_companies_and_vacancies_count(self) -> list[tuple]:
        """
        Returns dict of companies and vacancies' count
        """

        conn = psycopg2.connect(dbname=self.db_name, **self.params)
        with conn.cursor() as cur:
            cur.execute("SELECT company_name, open_vacancies FROM employers")
            rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass




