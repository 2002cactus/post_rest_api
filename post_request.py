from flask import Flask, jsonify, request
import requests
import json
import os

# Khởi tạo Flask app
app = Flask(__name__)

# API
url = "https://demo-rest-api-ewdl.onrender.com/users"

@app.route('/add_user', methods=['POST'])
def add_user():
    # Kiểm tra nếu môi trường cho phép nhập liệu
    if os.isatty(0):  # Kiểm tra xem chương trình có đang chạy trong môi trường tương tác không
        # Lấy dữ liệu đầu vào từ người dùng
        name = input("Nhập tên: ")
        email = input("Nhập email: ")
    else:
        # Sử dụng giá trị mặc định hoặc lấy từ biến môi trường nếu không có nhập liệu
        name = os.getenv("USER_NAME", "Default Name")  # Lấy từ biến môi trường nếu có
        email = os.getenv("USER_EMAIL", "default@example.com")  # Lấy từ biến môi trường nếu có

    # Đóng gói dữ liệu thành JSON
    data = {
        "name": name,
        "email": email
    }

    # Headers xác định kiểu dữ liệu JSON
    headers = {
        "Content-Type": "application/json"
    }

    # Gửi yêu cầu POST
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Kiểm tra phản hồi từ server
    if response.status_code == 201:  # Mã 201 = Thành công
        return jsonify({
            "message": "✅ Dữ liệu đã gửi thành công!",
            "response": response.json()
        }), 201
    else:
        return jsonify({
            "message": "❌ Gửi dữ liệu thất bại!",
            "error": response.text
        }), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
