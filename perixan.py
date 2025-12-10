from flask import Flask, request, jsonify
from perixan_ai import generate_response

# Flask uygulamasını başlat
app = Flask(__name__)

# Ana sayfa route
@app.route("/")
def home():
    return "✅ Perixan AI çalışıyor!"

# Chat API route
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = generate_response(user_message)
    return jsonify({"response": response})

# Status API route
@app.route("/api/status")
def status():
    return {
        "Veritabanı": "MEZOPOTAMYA",
        "Diller": ["Kurdî", "Türkçe", "English", "العربية", "فارسی", "עברית"],
        "Modüller": ["Chat", "Resim", "Video", "Müzik"],
        "Lisans": "AGPLv3 + Kurdistanî"
    }

# Ana çalıştırma bloğu
if __name__ == "__main__":
    print("🚀 PERİXAN AI BAŞLIYOR...")
    app.run(debug=True, host="0.0.0.0", port=8081, threaded=True)