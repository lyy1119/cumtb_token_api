from flask import Flask, request, jsonify
from getXIdToken import get_x_id_token

app = Flask(__name__)

# 定义一个带查询参数的API端点
@app.route('/api/token', methods=['GET'])
def process_data():
    # 从URL中获取参数
    id = request.args.get('id')
    pwd = request.args.get('pwd')
    result = your_python_function(id, pwd)  # 调用Python函数处理参数
    return jsonify(result)  # 返回JSON响应

def your_python_function(id, pwd):
    # 示例处理逻辑，假设只是返回拼接后的参数
    # return f"id = %s , pwd = %s" % (id , pwd)
    return get_x_id_token(id , pwd)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
