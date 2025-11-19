from airflow.sdk import dag, task, chain
from datetime import datetime


@dag(
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    description="DAG to check data"
) 
def check_dag():

    @task.bash
    def create_file():
        return 'echo "Hi there!" >/tmp/dummy.txt'


    @task.bash
    def check_file():
        # check the exact file created by create_file (includes .txt)
        return 'test -f /tmp/dummy.txt'
        
        
    @task
    def read_file():
        # read and print the file contents
        with open('/tmp/dummy.txt','rb') as f:
            data = f.read()
        try:
            # decode for nicer printing when possible
            print(data.decode('utf-8'))
        except Exception:
            print(data)


    chain(create_file(),check_file(),read_file())


check_dag()