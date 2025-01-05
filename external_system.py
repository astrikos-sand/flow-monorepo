import psycopg2
import requests


def read_ml_parameters_by_id(db_config, primary_key):
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, accuracy, best_model FROM ml_parameters WHERE id = %s
        """,
            (id,),
        )

        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "accuracy": row[1],
                "best_model": row[2],
            }
        else:
            print("No record found with the given ID.")
            return None

    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        if conn:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    db_config = {
        "dbname": "thingsboard",
        "user": "postgres",
        "password": "postgres",
        "host": "192.168.0.218",
        "port": "5434",
    }
    flow_id = "a5a8b744-eeff-4387-a922-94a0d2c7b615"
    # Retrieving the primary key
    res = requests.get(
        f"http://192.168.0.218:9100/v2/flows/{flow_id}/executions/?count=1"
    )
    # latest execution id
    execution_id = res.json()[0]["id"]
    print(execution_id)

    result = read_ml_parameters_by_id(db_config, execution_id)
    if result:
        print("Fetched Record:", result)
