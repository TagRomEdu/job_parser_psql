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
                requirement text,
                responsibility text,                
                vacancy_url text   
            )
        ''')

    conn_2.commit()
    conn_2.close()


def save_data_company_to_db(data: list[tuple], db_name: str, params: dict) -> None:
    """
    Saves company's data to database
    """
    conn = psycopg2.connect(dbname=db_name, **params)

    with conn.cursor() as cur:
        for company in data:
            cur.execute(
                """
                INSERT INTO employers (company_id, company_name, company_url, open_vacancies)
                VALUES (%s, %s, %s, %s)
                """,
                (company[0], company[1], company[2], company[3])
            )
    conn.commit()
    conn.close()


def save_data_vacancies_to_db(data: list[tuple], db_name: str, params: dict) -> None:
    """
    Saves vacancy's data to database
    """
    conn = psycopg2.connect(dbname=db_name, **params)

    videos_data = channel['videos']
    for video in videos_data:
        video_data = video['snippet']
        cur.execute(
            """
            INSERT INTO videos (channel_id, title, publish_date, video_url)
            VALUES (%s, %s, %s, %s)
            """,
            (channel_id, video_data['title'], video_data['publishedAt'],
             f"https://www.youtube.com/watch?v={video['id']['videoId']}")
                )

    conn.commit()
    conn.close()
