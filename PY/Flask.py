from flask import Flask, jsonify, send_from_directory

from sqlalchemy import create_engine, text

# 初始化Flask应用
app = Flask(__name__)

# 配置MySQL连接
username = 'root'
password = 'Ik851851'
host = '1.94.53.219:3306'
database = 'Disaster_wordcloud'
engine = create_engine(f'mysql+pymysql://root:Ik851851@1.94.53.219:3306/Disaster_wordcloud')

@app.route('/')
def index():
    return "Hello, this is the index page. Navigate to /disaster_type_data to see the data."

@app.route('/disaster_type_data')
def disaster_type_data():
    sql_query = text("SELECT * FROM disaster_type")
    with engine.connect() as connection:
        result = connection.execute(sql_query)
        # 使用._mapping属性获取行数据
        # 将RowMapping转换为字典
        # 将每行转换为字典
        data = [dict(row._mapping) for row in result]
    return jsonify(data)

import os
from flask import Flask, send_from_directory

# 假设您的 HTML 文件在以下目录
html_dir = "S:/GIT/PythonDataAnalysis/HTML"

@app.route('/disaster-chart')
def disaster_chart():
    html_file = 'Disaster_Type_Frequency.html'
    return send_from_directory(html_dir, html_file)




if __name__ == '__main__':
    app.run(debug=True)
