from sqlalchemy import create_engine, text




engine = create_engine(db_connection_string,
                       connect_args={
"ssl": {
  "ssl_ca": "/etc/ssl/cert.pem"
        }
      },  pool_pre_ping=True)

with engine.connect() as conn:
  result = conn.execute(text('Select * from jobs;'))
jobs = []
print(result.all())