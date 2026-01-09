from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:tiger=123@127.0.0.1:3306/phonepe"
)

conn = engine.connect()
print("Connection successful!")