from flask import Flask, request, jsonify
import openai
import os

# Menggunakan environment variable untuk API key agar lebih aman
openai.api_key=os.getenv("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")

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Fungsi untuk berinteraksi dengan OpenAI ChatGPT API
def chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Gunakan model terbaru yang tersedia
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        return f"Terjadi kesalahan saat mengakses OpenAI API: {str(e)}"
    except Exception as e:
        return f"Kesalahan tidak terduga: {str(e)}"

# Route utama untuk menerima prompt dari pengguna
@app.route('/', methods=['GET'])
def index():
    try:
        # Mengambil parameter 'prompt' dari query string
        prompt = request.args.get('prompt')
        if not prompt:
            return jsonify({"error": "Prompt tidak boleh kosong"}), 400
        
        # Memanggil fungsi chatgpt dan mengembalikan hasilnya
        response = chatgpt(prompt)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": f"Terjadi kesalahan: {str(e)}"}), 500

# Menjalankan aplikasi Flask
if __name__ == "__main__":
    # Pastikan aplikasi dapat diakses dari publik
    app.run(host="0.0.0.0", port=5000, debug=True)