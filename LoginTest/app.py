#-----------------------------------
#IMPORTS
import sqlite3
from flask import Flask, render_template, request
#-----------------------------------
#SETUP
app = Flask(__name__)
#-----------------------------------
#ROUTES
@app.route('/', methods=[ 'GET', 'POST'])
def index():
    if request.method == 'POST':
#-----------------------------------
#SQLITE
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()
        if conn:
                print("Connected to database successfully!")
        else:
                print("Error connecting to database!")

#-----------------------------------
#HTML FORM
        name ='billy'         #request.form['name']
        password ='mullen'    #request.form['password']

        print(name, password)
#-----------------------------------
#QUERY
        query = "SELECT name, password FROM users WHERE name = ? AND password = ?"
        #query = "SELECT name,password FROM users where name= '"+name+"' and password='"+password+"'"
        #query = "SELECT name,password FROM users where name='billy' and password='mullen';"
        #print(f"Executing query: {query}")

        with conn:
                cursor = conn.cursor()
                cursor.execute(query, (name, password))
                rows = cursor.fetchall()
                print(rows)
        # Process the result
        if rows:
                print("Login successful!")
        else:
                print("Login failed. Incorrect username or password.")

        #cursor.execute(query)

        #results = cursor.fetchall()
        #print(results)
#-----------------------------------
#VALIDATION
        #if len(results) == 0:
            #print('login failed try again')
        #else:
            #return render_template("logged_in.html")
    
    
    return render_template( "index.html" )

if __name__ == '__main__':
    app.run(debug=True)