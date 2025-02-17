import requests
import json

# API
url = "https://demo-rest-api-ewdl.onrender.com/users"

# Lấy dữ liệu đầu vào từ người dùng
name = input("Nhập tên: ")
email = input("Nhập email: ")

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
    print("✅ Dữ liệu đã gửi thành công!")
    print("Phản hồi từ server:", response.json())
else:
    print("❌ Gửi dữ liệu thất bại! Mã lỗi:", response.status_code)
    print("Nội dung phản hồi:", response.text)
