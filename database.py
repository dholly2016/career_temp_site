from sqlalchemy import create_engine


db_connection_string = "mysql+pymysql://lhqtzpy51iqlcz2tguuejobs:pscale_pw_nBcrZPDeMZJlVcSB31aG5vA7OPetpjkHxIjpYnqMEhu@aws.connect.psdb.cloud/careersdb?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={
"ssl": {
  "ssl_ca": "/etc/ssl/cert.pem"
        }
      })
