from flask import Flask, jsonify, send_from_directory

from sqlalchemy import create_engine, text

# 初始化Flask应用
app = Flask(__name__)

# 配置第一个数据库
username_1 = 'root'
password_1 = 'Ik851851'
host_1 = '1.94.53.219:3306'
database_1 = 'Disaster_wordcloud'
engine_1 = create_engine(f'mysql+pymysql://root:Ik851851@1.94.53.219:3306/Disaster_wordcloud')

# 配置第二个数据库
username_2 = 'root'
password_2 = 'Ik851851'
host_2 = '1.94.53.219:3306'
database_2 = 'Greenhouse_Gas'
engine_2 = create_engine(f'mysql+pymysql://root:Ik851851@1.94.53.219:3306/Greenhouse_Gas')




@app.route('/')
def index():
    return "Hello, this is the index page. Navigate to /disaster_type_data to see the data."

@app.route('/disaster_type_data')
def disaster_type_data():
    sql_query_1 = text("SELECT * FROM disaster_type")
    with engine_1.connect() as connection:
        result = connection.execute(sql_query_1)
        # 使用._mapping属性获取行数据
        # 将RowMapping转换为字典
        # 将每行转换为字典
        data = [dict(row._mapping) for row in result]
    return jsonify(data)

@app.route('/disaster_subtype_data')
def disaster_subtype_data():
    sql_query_1 = text("SELECT * FROM disaster_subtype")
    with engine_1.connect() as connection:
        result = connection.execute(sql_query_1)
        # 使用._mapping属性获取行数据
        # 将RowMapping转换为字典
        # 将每行转换为字典
        data = [dict(row._mapping) for row in result]
    return jsonify(data)

@app.route('/greenhouse_gas_emissions_data')
def greenhouse_gas_emissions_data():
    sql_query_2 = text("SELECT * FROM greenhouse_gas_emissions")
    with engine_2.connect() as connection:
        result = connection.execute(sql_query_2)
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
    html_file = 'Disaster_Frequency_WordCloud.html'
    return send_from_directory(html_dir, html_file)

@app.route('/greenhouse_gas_emissions')
def greenhouse_gas_emissions():
    html_file = 'Greenhouse_Gas_Emissions.html'
    return send_from_directory(html_dir, html_file)


if __name__ == '__main__':
    app.run(debug=True)
