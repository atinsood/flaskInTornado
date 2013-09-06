This is a very basic skeletal project which shows how to use

- Tornado and Flask together for the back end
- Angular and bootstrap managed by bower for the front end

```
Things to note
```

- flaskProjectCode.py script basically instantiates a flask application and
defines all the routes. Even though a main method is defnied in this script 
the method is never used in practice. 

- flaskFromTornado.py is the startup script which basically wraps the Flask
application and starts it within tornado. 

- Also note the arrangement of folders, how the static code is separated from 
actual code. 

To start the project:

cd flaskProjectCode/static/components
bower install

cd flaskProjectCode
python flaskFromTornado

This should start the project at 

http://localhost:8000/flask
