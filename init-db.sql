-- We need to grant our user permission to access our db cause by default, he has none.
GRANT ALL PRIVILEGES ON flask_proj_db.* TO 'projectuser'@'%';
FLUSH PRIVILEGES;
