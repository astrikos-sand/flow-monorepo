# Astrikos


vgs ubuntu-vg

sudo lvextend -L +5G /dev/ubuntu-vg/ubuntu-lv
sudo resize2fs /dev/ubuntu-vg/ubuntu-lv

ps aux | grep thingsboard
lsblk

docker compose -f setup.docker-compose.yml up --build -d
docker compose -f setup.docker-compose.yml up db --build -d

docker run -it --name cnt default-env-6c98f7a9 bash
docker commit cnt default-env-6c98f7a9


# apt-get install unixodbc unixodbc-dev
# apt-get install -y curl gnupg2 apt-transport-https

# curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
# curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
# apt-get update

# ACCEPT_EULA=Y apt-get install -y msodbcsql17
# odbcinst -q -d


docker volume create astrikos_worker_executors

location /notebooks {
    return 301 http://$remote_addr:9300/tree;
}

docker exec -it timescaledb psql

psql
pg_ctl restart
SELECT pg_is_in_recovery();
SELECT pg_wal_replay_resume();


SELECT FROM pg_catalog.pg_stat_database;


SELECT timescaledb_pre_restore()
SELECT timescaledb_post_restore();

ps aux | grep thingsboard
kill PID

docker build -t default-astrikos-env -f docker/temp.Dockerfile .

const input_string = `
    Detect anomalies in the DataFrame using a specified method (Isolation Forest, Z-Score, or IQR).

    Parameters:
    - df: pandas DataFrame, input dataset.
    - method: str, method for anomaly detection ('isolation_forest', 'z_score', or 'iqr').
    - contamination_factor: float, proportion of outliers expected in the data (only for Isolation Forest).
    - z_threshold: float, threshold for Z-Score to classify outliers (only for Z-Score).
    - columns: list of str or None, column names to use for anomaly detection. If None, all columns will be used.
    - remove_anomalies: str, if 'yes', removes rows identified as anomalies.

    Returns:
    - df: pandas DataFrame, processed dataset with an additional 'anomaly' column indicating anomaly status (1 or 0).
    - output: dictionary containing model or other necessary information based on the method used.
`


const [definitionDoc, parametersDoc, returnsDoc] = extractSection(input_string);


docker volume create astrikos_file_server


ps aux | grep thingsboard
kill PID
 

docker cp astrikos_backend:/astrikos/media /root/backup/med-7
cp -r /var/lib/docker/volumes/astrikos_db/_data /root/backup/db-7
