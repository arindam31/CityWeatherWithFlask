# Flask Template project
- User auth with JWT
- Online API document with Swagger
- Connexions usage
- Logging
- Permissions

# QUICK Start
- create a .env file at root. Add variables as shown below.
- On shell, use: flask run
- Visit url: 127:0.0.1:5000

# ENV file contents
Add these in the .env file:
```
FLASK_APP=app
FLASK_ENV=development
```


# Running the project
- With flask command directly:
 ```bash
 flask run
 ```

- Start the docker container
 ```bash
 docker compose up --build
 ```

# Command execution with docker.
- To execute commands inside the container:
 ```bash
docker exec -ti flask_app_container bash
 ```

 # To see flask routes
 ```bash
docker exec -it flask_app_container flask routes

Endpoint           Methods    Rule
-----------------  ---------  ---------------------------------
admin.index        GET        /admin/
admin.static       GET        /admin/static/<path:filename>    
static             GET        /static/<path:filename>
user.action_view   POST       /admin/user/action/
user.ajax_lookup   GET        /admin/user/ajax/lookup/
user.ajax_update   POST       /admin/user/ajax/update/
user.create_view   GET, POST  /admin/user/new/
user.delete_view   POST       /admin/user/delete/
user.details_view  GET        /admin/user/details/
user.edit_view     GET, POST  /admin/user/edit/
user.export        GET        /admin/user/export/<export_type>/
user.index_view    GET        /admin/user/
 ```