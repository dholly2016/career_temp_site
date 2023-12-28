from sqlalchemy import create_engine, text 
import os 

db_connection_string = os.environ['DB_CONNECTION_STRING']


engine = create_engine(db_connection_string,
                       connect_args={
"ssl": {
  "ssl_ca": "/etc/ssl/cert.pem"
        }
      },  pool_pre_ping=True)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('Select * from jobs;'))
    jobs = []
    for row in result.all():
        jobs.append(dict(row._mapping))
    return jobs





   