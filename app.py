from flask import Flask, render_template_string
import os

app = Flask(_name_)

@app.route('/')
def home():
    return render_template_string("""
        <h1>ESP8266 LED Control</h1>
        <button onclick="fetch('/led/on')">Turn ON</button>
        <button onclick="fetch('/led/off')">Turn OFF</button>
    """)

@app.route('/led/on')
def led_on():
    return "LED turned ON"

@app.route('/led/off')
def led_off():
    return "LED turned OFF"

if _name_ == "main":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
