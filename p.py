import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from PyQt5.QtGui import QFont, QPalette, QColor
import ipaddress

def get_ip_info(ip_address):
    try:
        if ipaddress.ip_address(ip_address).is_private:
            return "This is a private IP. GeoIP information is unavailable."
        
        response = requests.get(f"http://ip-api.com/json/{ip_address}").json()
        if response['status'] == 'success':
            info = f"""
IP: {response.get('query')}
Country: {response.get('country')}
Region: {response.get('regionName')}
City: {response.get('city')}
ZIP: {response.get('zip')}
ISP/Operator: {response.get('isp')}
Approx. Location: {response.get('lat')}, {response.get('lon')}
            """
        else:
            info = f"Error: {response.get('message')}"
        return info
    except:
        return "Unable to fetch IP information."

def login():
    username = username_input.text()
    password = password_input.text()
    ip = ip_input.text()
    if username == "admin" and password == "1234":
        info = get_ip_info(ip)
        info_box.setText(info)
    else:
        QMessageBox.warning(window, "Error", "Incorrect username or password!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("IP Lookup Tool")
window.resize(500, 400)

palette = QPalette()
palette.setColor(QPalette.Window, QColor(30, 30, 30))
palette.setColor(QPalette.WindowText, QColor(220, 220, 220))
palette.setColor(QPalette.Base, QColor(45, 45, 45))
palette.setColor(QPalette.Text, QColor(220, 220, 220))
palette.setColor(QPalette.Button, QColor(70, 70, 70))
palette.setColor(QPalette.ButtonText, QColor(220, 220, 220))
app.setPalette(palette)

font_label = QFont("Arial", 10)
font_input = QFont("Arial", 11)

lbl_username = QLabel("Username:", window)
lbl_username.setFont(font_label)
lbl_username.move(50, 30)

lbl_password = QLabel("Password:", window)
lbl_password.setFont(font_label)
lbl_password.move(50, 70)

lbl_ip = QLabel("Enter IP:", window)
lbl_ip.setFont(font_label)
lbl_ip.move(50, 110)

username_input = QLineEdit(window)
username_input.setFont(font_input)
username_input.move(150, 30)
username_input.resize(250, 25)

password_input = QLineEdit(window)
password_input.setFont(font_input)
password_input.setEchoMode(QLineEdit.Password)
password_input.move(150, 70)
password_input.resize(250, 25)

ip_input = QLineEdit(window)
ip_input.setFont(font_input)
ip_input.move(150, 110)
ip_input.resize(250, 25)

login_btn = QPushButton("Lookup IP", window)
login_btn.move(180, 150)
login_btn.resize(140, 35)
login_btn.setStyleSheet("""
QPushButton {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    font-size: 14px;
}
QPushButton:hover {
    background-color: #45a049;
}
""")
login_btn.clicked.connect(login)

info_box = QTextEdit(window)
info_box.setReadOnly(True)
info_box.setFont(QFont("Courier", 10))
info_box.resize(420, 170)
info_box.move(40, 200)
info_box.setStyleSheet("background-color: #2d2d2d; color: #e0e0e0; border-radius: 5px;")

window.show()
sys.exit(app.exec_())
