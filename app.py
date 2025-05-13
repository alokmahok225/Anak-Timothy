from flask import Flask, request, jsonify
!pip install openai

import openai

openai.api_key = "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"  # Ganti dengan API key kamu

def chatgpt(prompt):
       response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # atau "gpt-4" jika tersedia
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

@app.route('/')
def index():
    prompt = request.args.get('prompt', 'Tidak ada prompt')
    return chatgpt('prompt','dengan kriteria ini buat adengan cerita') 

if __name__=="__main__":
  app.run(debug=True) 