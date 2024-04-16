from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)

# Kết nối đến cơ sở dữ liệu MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vietnam_news"
)
mycursor = mydb.cursor()

# Áp dụng CORS cho tất cả các route
CORS(app)

# Định nghĩa route /list/articles
@app.route('/list/articles', methods=['GET'])
def list_articles():
    mycursor.execute("SELECT id, title, content, image FROM articles LIMIT 10")
    articles = []
    for (id, title, content, image) in mycursor:
        articles.append({"id": id, "title": title, "content": content, "image": image})
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
