import snowflake.connector

class SnowflakeConnector:
    def __init__(self,account,user,password,warehouse,database,schema,role) -> None:
        self.account = account
        self.user = user
        self.password = password
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.role = role
    
    def connect(self):
        self.connection = snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account,
            warehouse=self.warehouse,
            databse=self.database,
            schema=self.schema
        )
        self.cursor = self.connection.cursor()

    def execute_query(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

account = "GKNDOXY-ON95970"
user = "dineshmote"
password = "Dinesh@1234"  # Optional, or set it securely
database = "SNOWFLAKE_SAMPLE_DATA"    # Optional
schema = "TPCH_SF1"  # Optional
role =  "SYSADMIN "      # Optional
warehouse = "COMPUTE_WH"  # Optional

sf_connector=SnowflakeConnector( 
    account=account,
    user=user,
    password=password,
    database=database,
    schema=schema,
    role=role,
    warehouse=warehouse
)

sf_connector.connect()

query="select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER limit 10"
result=sf_connector.execute_query(query)
print(result)

sf_connector.close_connection()