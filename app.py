from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)




@app.route('/api/data/', methods=['GET'])
def get_data():
    data={}
    conn=sqlite3.connect('users.db')
    cursor=conn.cursor()
    cursor.execute('select * from users')
    table=cursor.fetchall()
    for d in table:
            data[int(d[0])]={"name":d[1],"age":d[2]}
            
    return jsonify(data)

# POST method to add new data
@app.route('/api/data/', methods=['POST'])
def add_data():
    new_entry = request.get_json()
    name=new_entry["name"]
    age=new_entry["age"]
    
    data={}
    conn=sqlite3.connect('users.db')
    cursor=conn.cursor()
    cursor.execute('insert into users(name,age) values(?,?)',(name,age))
    conn.commit()
    if(cursor.rowcount>0):
        data={}
        conn=sqlite3.connect('users.db')
        cursor=conn.cursor()
        cursor.execute('select max(id) from users')
        id=cursor.fetchall()[0][0]
        return jsonify({"message":f"Data added successfully with id {id} "})
    return jsonify({"message":f"Data Not Added successfully "})


# DELETE method to remove data by ID
@app.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
   
    conn=sqlite3.connect('users.db')
    cursor=conn.cursor()
    cursor.execute('delete from users where id=?',(data_id,))
    conn.commit()
    if(cursor.rowcount>0):
         return {"message":f"Data with id {data_id} deleted successfully"}
    return {"message":f"Data with id {data_id} not present"}


