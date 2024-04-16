import requests
from bs4 import BeautifulSoup
import mysql.connector

# Kết nối đến cơ sở dữ liệu MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Tạo cơ sở dữ liệu nếu chưa tồn tại
with mydb.cursor() as mycursor:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS vietnam_news")
    mycursor.execute("USE vietnam_news")

    # Tạo bảng 'articles' nếu chưa tồn tại
    mycursor.execute("CREATE TABLE IF NOT EXISTS articles (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), content TEXT, image VARCHAR(255))")

# Hàm để lấy dữ liệu từ trang chủ VNExpress và lưu vào cơ sở dữ liệu
def scrape_vnexpress():
    try:
        url = "https://vnexpress.net/bong-da"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find_all('article')
            with mydb.cursor() as mycursor:
                for article in articles:
                    title_element = article.find('h2', class_='title-news')
                    content_element = article.find('p', class_='description')
                    image_element = article.find('img')

                    if title_element:
                        title = title_element.text.strip()
                    else:
                        title = "Title not found"

                    if content_element:
                        content = content_element.text.strip()
                    else:
                        content = "Content not found"

                    if image_element and 'src' in image_element.attrs:
                        image = image_element['src']
                    else:
                        image = "Image not found"

                    # Lưu dữ liệu vào cơ sở dữ liệu
                    sql = "INSERT INTO articles (title, content, image) VALUES (%s, %s, %s)"
                    val = (title, content, image)
                    mycursor.execute(sql, val)

                mydb.commit()
            print("Scraping and saving completed successfully.")
        else:
            print("Failed to connect to VNExpress.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Thực hiện hàm để lấy dữ liệu và lưu vào cơ sở dữ liệu
scrape_vnexpress()
