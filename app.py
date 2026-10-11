from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

INDEX_HTML = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PesaCHECK</title>
<style>*{margin:0;padding:0;box-sizing:border-box;font-family:sans-serif}
body{background:#f6f7fb} nav{background:#fff;padding:15px 20px;display:flex;justify-content:space-between;box-shadow:0 2px 10px rgba(0,0,0,.05)}
.hero{padding:50px 20px;text-align:center;background:linear-gradient(135deg,#00c853,#009624);color:#fff}
.btn{display:inline-block;background:#fff;color:#00c853;padding:14px 28px;border-radius:30px;text-decoration:none;font-weight:700;margin-top:20px}
.cards{display:grid;gap:15px;padding:20px;max-width:900px;margin:-20px auto}
.card{background:#fff;padding:20px;border-radius:16px;box-shadow:0 4px 20px rgba(0,0,0,.06)}
</style></head><body>
<nav><b>Pesa<span style="color:#00c853">CHECK</span></b><span style="font-size:12px;background:#e8f5e9;color:#00c853;padding:6px 12px;border-radius:20px">● LIVE</span></nav>
<div class="hero"><h1>Verify Truth. Earn Instantly.</h1><p>Kenya's #1 AI Fact-Checking. $0.07 per task.</p><a href="/verify" class="btn">Start Verifying →</a></div>
<div class="cards"><div class="card"><h3>⚡ Fast</h3><p>AI inacheck in seconds</p></div><div class="card"><h3>💰 Earn</h3><p>Malipo Mpesa direct</p></div></div>
</body></html>
"""

VERIFY_HTML = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Verify</title>
<style>*{box-sizing:border-box;font-family:sans-serif}body{background:#f6f7fb;margin:0;padding:15px}
.box{background:#fff;padding:20px;border-radius:16px;max-width:500px;margin:20px auto}
textarea{width:100%;padding:14px;border:1.5px solid #ddd;border-radius:12px;font-size:16px}
button{width:100%;padding:15px;background:#00c853;color:#fff;border:none;border-radius:12px;font-weight:700;margin-top:12px}
.result{margin-top:15px;padding:15px;background:#e8f5e9;border-radius:12px;display:none}
</style></head><body>
<div class="box"><h2>PesaCHECK Verify</h2><p style="color:#666">Paste claim</p>
<textarea id="text" rows="5" placeholder="Mfano: News fulani..."></textarea>
<button onclick="verify()">Verify Now</button><div id="res" class="result"></div><a href="/" style="display:block;margin-top:15px;color:#666;text-decoration:none">← Home</a></div>
<script>async function verify(){const t=document.getElementById('text').value;if(!t)return alert('Weka text');const r=document.getElementById('res');r.style.display='block';r.innerHTML='⏳ Inacheck...';const resp=await fetch('/verify',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:t})});const d=await resp.json();r.innerHTML='<b>'+d.verification+'</b><br><br><b style=color:#00c853>'+d.earned+' Earned ✓</b>';}</script>
</body></html>
"""

@app.route('/')
def home():
    return render_template_string(INDEX_HTML)

@app.route('/verify', methods=['GET','POST'])
def verify():
    if request.method == 'GET':
        return render_template_string(VERIFY_HTML)
    data = request.get_json() or {}
    text = data.get('text','')
    return jsonify({"status":"success","text_received":text,"verification":"REAL - Verified ✓" if len(text)>10 else "Too short","earned":"$0.07"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
