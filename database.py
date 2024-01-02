import os

from sqlalchemy import create_engine, text

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

def load_job_from_db(id):
  with engine.connect() as conn:
      result = conn.execute(
        text("Select * from jobs where id = :val"),
        {"val" : id}
      )
      rows = result.all()
      if len(rows) == 0:
          return None
      else:
          return dict(rows[0]._mapping)

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
      query = text("Insert into applications (job_id, full_name, email, linkedin_url, education, experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :experience, :resume_url)", )

    conn.execute(query, job_id = job_id, full_name=data['full_name'],email=data['email'],=data['full_name'],full_name=data['full_name'],                 full_name=data['full_name'],)

   