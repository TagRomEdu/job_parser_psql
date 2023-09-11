import psycopg2


def create_db(db_name: str, params: dict) -> None:
    """
    Create database
    """
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        cur.execute(f'DROP DATABASE {db_name}')
    except Exception:
        pass

    cur.execute(f'CREATE DATABASE {db_name}')

    cur.close()
    conn.close()

    conn_2 = psycopg2.connect(dbname=db_name, **params)

    with conn_2.cursor() as cur_2:
        cur_2.execute('''
            CREATE TABLE employers (
                company_id int PRIMARY KEY, 
                company_name varchar(255) NOT NULL, 
                company_url text, 
                open_vacancies int 
            )
        ''')

    with conn_2.cursor() as cur_3:
        cur_3.execute('''
            CREATE TABLE vacancies (
                vacancy_id int PRIMARY KEY,
                name varchar NOT NULL,
                city varchar NOT NULL,
                company_id int REFERENCES employers(company_id),
                salary int,
                published_at timestamp,
                responsibility text,                
                vacancy_url text   
            )
        ''')

    conn_2.commit()
    conn_2.close()
