# Database commands during setup and general maintainence

- To check if db was created:
 ```bash
 docker exec -it mysql_container mysql -u root -p
 SHOW DATABASES;
 ```
 If you see something like this, then our db got created

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

- To generate migration files and create tables
 ```bash
docker exec -ti flask_app_container flask db init
docker exec -ti flask_app_container flask db upgrade
 ```