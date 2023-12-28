# Python数据分析实例
# [跳转到指南手册](#id_666)  

python数据分析实例，并且使用动态数据库MySQL,再通过Echarts输出可视化

## 安装依赖

Python

Echarts

MySQL

Jupyter NoteBook

## 示例

本项目提供了一个简单的示例代码

访问我的网站：

- [Jupyter Notebook](http://1.94.53.219:9000/tree)(不可用)

- [phpmyadmin(MySQL可视化)](http://1.94.53.219:8888/phpmyadmin/index.php?lang=zh_cn)(可用)

## TODO

全球气候变暖与能源转型项目

- 全文件echarts转换

- notebook上运行flask

## 参考文档和链接
-[2023年（第16届）中国大学生计算机设计大赛 大数据主题赛公告 (dhu.edu.cn)](https://jsjds.dhu.edu.cn/2023/0124/c20379a320418/page.htm)

-[Apache ECharts](https://echarts.apache.org/zh/index.html)

-[AWS服务器上在ubuntu系统上安装部署MySQL和Phpmyadmin（超详细图文）](https://blog.csdn.net/weixin_45913922/article/details/130100542)

-[Climate Change: Earth Surface Temperature Data (kaggle.com)](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data/data)

-[Predicting Climate Change Data with Python | Kaggle](https://www.kaggle.com/code/tytibbets/predicting-climate-change-data-with-python)







<span id='id_666'/>

# Python 数据分析实例 - 使用 MySQL 和 Echarts

## 概述

本项目展示了如何使用 Python 进行数据分析，结合动态数据库 MySQL 和 Echarts 进行数据可视化。我们将通过一系列步骤详细介绍数据收集、处理、分析和可视化的整个流程。

## 项目结构

- `Data_collection`: 数据收集脚本，从不同源获取数据。
- `Data_processing`: 数据处理脚本，包括清洗和转换数据。
- `MySQL-database`: MySQL数据库脚本，用于存储和管理数据。
- `Data-analysis`: 数据分析脚本，使用Python进行统计分析。
- `Flask`: Flask调用MySQL实现echarts的内容。
- `EChart-visualization`: 使用Echarts进行数据可视化的脚本。

## 数据收集

数据收集是数据分析的第一步。在本项目中，我们使用 Python 脚本从多个源收集数据。这可能包括公开数据集、API调用或直接的数据输入。

## 数据处理

数据处理涉及数据清洗和转换。我们使用 Python 进行数据预处理，包括处理缺失值、异常值和数据格式化。目的是确保数据质量，为分析阶段做好准备。

## 数据分析

在这一阶段，我们使用 Python 进行数据探索和统计分析。分析可能包括趋势识别、关联性分析和模式识别等。

### 1. **Numpy**
NumPy 是 Python 的一个科学计算库，专注于对多维数组的操作。

主要特点：
- 高性能的多维数组对象 ndarray。
- 广泛的数学函数库：线性代数、随机数生成、傅里叶变换等。
- 用于数组的高效迭代和计算。

常用用法：
- 数组创建：使用 np.array(), np.zeros(), np.ones(), np.arange() 等函数创建数组。
- 数组操作：数组形状改变（reshape()），数组合并（concatenate(), vstack(), hstack()）等。
- 数学运算：支持基本的加减乘除及更复杂的数学运算和矩阵运算。
- 布尔索引和切片：使用布尔索引和切片技术快速访问和修改数组的部分元素。
- 通用函数（ufunc）：提供快速的元素级数组函数，如 sin(), cos(), exp() 等。
- 在实际使用中，Pandas 和 NumPy 经常结合使用，Pandas 用于灵活的数据处理和分析，而 NumPy 则用于进行复杂的数值运算。

### 2. **Pandas**
Pandas 是一个强大的数据分析和操作工具，主要用于处理表格数据。
  
主要特点：
- 处理不同类型的数据：时间序列、非结构化数据等。
- 支持多种文件格式的数据输入输出：CSV、Excel、SQL数据库等。
- 强大的数据清洗和处理能力：缺失数据处理、数据过滤、数据合并等。

常用用法：
- DataFrame 和 Series：Pandas 的两个主要数据结构，分别用于处理表格数据和一维数组。
- 数据读取和写入：使用 pd.read_csv(), pd.read_excel(), pd.to_csv(), pd.to_excel() 等函数读取和写入不同格式的数据。
- 数据选择和过滤：使用 loc[], iloc[], 布尔索引等方法选择和过滤数据。
- 数据清洗：如处理缺失值（fillna(), dropna()），数据类型转换（astype()），字符串操作等。
- 数据统计和聚合：groupby(), sum(), mean(), median() 等函数进行数据的统计和聚合。

## 数据存储 - MySQL

处理后的数据存储在 MySQL 数据库中。我们设计了数据库模式来有效地组织数据，以及编写了脚本来自动化数据的导入过程。

MySQL
MySQL 是一个广泛使用的开源关系型数据库管理系统（RDBMS），它基于 SQL（结构化查询语言）。MySQL 是网络和应用程序中最流行的数据库系统之一，特别适用于网站和在线应用程序。

主要特点
- 开源：MySQL 是开源的，允许用户免费使用和修改。
- 跨平台：支持多种操作系统，如 Linux、Windows 和 MacOS。
- 高性能：MySQL 提供了高性能的数据库解决方案。
- 可扩展性：支持大型数据库，可以处理大量数据。
- 安全性：提供了强大的安全特性，包括访问控制和加密。
- 易用性：具有简单易用的界面和丰富的文档支持。

应用场景
- 网站和网络应用
- 数据仓库
- e-Commerce 应用
- 日志记录

## 数据调用 - Flask

### 使用 DataFrame 导入数据到 MySQL

在 Python 中，可以使用 Pandas 的 DataFrame 结合 SQLalchemy 和 pymysql（或其他数据库连接器）将数据导入到 MySQL 数据库中。以下是一个基本的流程：

1. **安装必要的库**：
   安装 Pandas、SQLalchemy 和 pymysql（或你选择的数据库连接器）。

   ```bash
   pip install pandas sqlalchemy pymysql
   ```

2. **创建 DataFrame**：
   首先在 Pandas 中创建或读取一个 DataFrame。

   ```python
   import pandas as pd
   data = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
   df = pd.DataFrame(data)
   ```

3. **建立数据库连接**：
   使用 SQLalchemy 创建到 MySQL 数据库的连接。

   ```python
   from sqlalchemy import create_engine
   engine = create_engine('mysql+pymysql://user:password@host:port/database')
   ```

4. **导入数据**：
   使用 DataFrame 的 `to_sql` 方法将数据导入到 MySQL 数据库中。

   ```python
   df.to_sql('table_name', con=engine, if_exists='replace', index=False)
   ```

## 数据可视化 - Echarts

最后一步是数据可视化。我们使用 Echarts 创建动态和交互式的图表，这有助于更好地理解数据和分析结果。图表可能包括柱状图、折线图、饼图等。

-[Apache ECharts](https://echarts.apache.org/zh/index.html)

## Flask 与 MySQL 和 Echarts 集成

### 1. 设置 Flask 应用程序

首先，您需要创建一个 Flask 应用程序。这通常包括设置一个 Flask 实例和定义路由。

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### 2. 连接到 MySQL 数据库

使用例如 `PyMySQL` 或 `Flask-MySQLdb` 等库来连接到 MySQL 数据库，并从数据库中查询数据。

```python
import pymysql

def get_db_connection():
    connection = pymysql.connect(host='hostname',
                                 user='username',
                                 password='password',
                                 db='dbname',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
```

### 3. 数据处理

处理从数据库检索到的数据，以便它们可以被 Echarts 使用。这可能涉及数据清洗、转换和聚合。

### 4. 集成 Echarts

在 Flask 应用程序中集成 Echarts。这通常涉及到将数据传递给一个 HTML 模板，该模板包含 Echarts 的配置。

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>数据可视化</title>
    <!-- 引入 Echarts -->
    <script src="https://cdn.bootcdn.net/ajax/libs/echarts/4.9.0-rc.1/echarts.min.js"></script>
</head>
<body>
    <div id="main" style="width: 600px;height:400px;"></div>
    <script type="text/javascript">
        var myChart = echarts.init(document.getElementById('main'));
        var option = {
            // Echarts 配置项
            // 使用从 Flask 传递的数据填充
        };
        myChart.setOption(option);
    </script>
</body>
</html>
```

### 5. 在 Flask 路由中使用

在 Flask 路由中处理数据，并将其传递给 Echarts。

```python
@app.route('/data')
def data():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM your_table")
        result = cursor.fetchall()
    connection.close()

    # 数据处理和转换

    return render_template('data.html', data=result)
```

## 结论

本项目展示了如何使用 Python、MySQL 和 Echarts 进行完整的数据分析流程。这个实例可以作为进行类似分析的基础模板和指导。
