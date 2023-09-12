# job_parser_psql
Program scrapes vacancies from hh.ru and saves it with PostgreSQL.

It has utils.py with funcs for crate database and save data in database. In also has config.py with script for unpacking database.ini.

Python package 'src', there are api_worker.py (class for work with api hh.ru) and db_manager (class for work with database).

The program starts from main.py. 
Next, you need to enter a keyword to search in the name of the vacancy. That's all.
