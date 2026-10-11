from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

VERIFY_PAGE = """
<!DOCTYPE html>
<html>
<head><title>PesaCHECK - Verify</title>
<style>
body{background:#000;color:#fff;font-family:Arial;display:flex;justify-content:center;padding:30px}
.card{background:#111;padding:30px;border-radius:16px;border:1px solid #333;width:100%;max-width:500px}
input,textarea{width:100%;padding:12px;margin:8px 0;border-radius:8px;border:1px solid #333;background:#222;color:#fff}
button{background:#00ff88;color:#000;padding:12px;border:none;border-radius:8px;font-weight:bold;width:100%;cursor:pointer}
.result{margin-top:15px;padding:12px;background:#1a1a1a;border-radius:8px}
</style>
</head>
<body>
<div class="card">
<h2 style="color:#00ff88">PesaCHECK Verify</h2>
<p>Earning: $0.07 / task</p>
<textarea id="text" rows="4" placeholder="Weka text ya ku-verify hapa..."></textarea>
<button onclick="verify()">Verify Now</button>
<div id="res" class="result" style="display:none"></div>
<a href="/" style="color:#888;display:block;margin-top:15px">← Back Home</a>
</div>
<script>
async function verify(){
 const t=document.getElementById('text').value;
 const r=document.getElementById('res');
 r.style.display='block'; r.innerHTML='Verifying...';
 const resp=await fetch('/verify',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:t})});
 const data=await resp.json();
 r.innerHTML='<b>Result:</b><br>'+JSON.stringify(data,null,2);
}
</script>
</div>
</body>
</html>
"""

@app.route('/')
def home():
    try:
        return open('templates/index.html').read()
    except:
        from flask import render_template
        return render_template('index.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'GET':
        return render_template_string(VERIFY_PAGE)
    
    # POST - inataka JSON
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON sent"}), 400
    
    text = data.get('text', '')
    # Hapa ndio logic yako ya ku-verify
    result = {
        "status": "success",
        "text_received": text,
        "verification": "REAL" if len(text) > 10 else "Too short",
        "earned": "$0.07"
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
