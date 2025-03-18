# Database commands during setup and general maintainence

### Create a local sqlite db for development and populate data from json file.
```bash
flask create-db
flask load-data
```
**Note**: Check if a app.sqlite3 file has been create at root.

### On docker, to check if db was created:
 ```bash
 docker exec -it mysql_container mysql -u root -p
 SHOW DATABASES;
 ```
 
 The db got created if the following is observed.

 ```sql
 mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| flask_proj_db      |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)

SHOW GRANTS FOR 'projectuser'@'%';

+------------------------------------------------------------------+
| Grants for projectuser@%                                         |
+------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `projectuser`@`%`                          |
| GRANT ALL PRIVILEGES ON `flask\_proj\_db`.* TO `projectuser`@`%` |
| GRANT ALL PRIVILEGES ON `flask_proj_db`.* TO `projectuser`@`%`   |
+------------------------------------------------------------------+
3 rows in set (0.00 sec)
```

### To generate migration files and create tables
 ```bash
docker exec -ti flask_app_container flask db init
docker exec -ti flask_app_container flask db upgrade
 ```