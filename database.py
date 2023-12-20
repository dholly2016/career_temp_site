from sqlalchemy import create_engine,text


db_connection_string = "mysql+pymysql://ax9qwkmu79yqgk2986dc:pscale_pw_5dBAHpKWhaSMDyapbGK3hXNJuKBZW7QZg8x4L8kULet@aws.connect.psdb.cloud/careersdb?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={
"ssl": {
  "ssl_ca": "/etc/ssl/cert.pem"
        }
      })

with engine.connect() as conn:
    result = conn.execute(text('Select * from jobs;'))
    
    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row))
  
    