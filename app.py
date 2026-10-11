VERIFY_PAGE = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Verify - PesaCHECK</title>
<style>*{box-sizing:border-box;font-family:sans-serif}body{background:#f6f7fb;margin:0;padding:15px}
.top{background:#fff;padding:15px;border-radius:12px;display:flex;justify-content:space-between;margin-bottom:15px}
.box{background:#fff;padding:20px;border-radius:16px;box-shadow:0 4px 20px rgba(0,0,0,.06)}
textarea{width:100%;padding:14px;border:1.5px solid #ddd;border-radius:12px;font-size:16px}
button{width:100%;padding:15px;background:#00c853;color:#fff;border:none;border-radius:12px;font-size:16px;font-weight:700;margin-top:12px}
.result{margin-top:15px;padding:15px;background:#e8f5e9;border-radius:12px;display:none}
</style></head><body>
<div class="top"><b>PesaCHECK</b><span style="color:#00c853">● $0.07/task</span></div>
<div class="box">
<h2>Verify Claim</h2>
<p style="color:#666">Paste any news or statement</p>
<textarea id="text" rows="5" placeholder="Mfano: Raila amesema..."></textarea>
<button onclick="verify()">Verify Now</button>
<div id="res" class="result"></div>
<a href="/" style="display:block;margin-top:15px;color:#666;text-decoration:none">← Home</a>
</div>
<script>
async function verify(){
 const t=document.getElementById('text').value; if(!t){alert('Weka text kwanza');return}
 const r=document.getElementById('res'); r.style.display='block'; r.innerHTML='⏳ Inacheck...';
 const resp=await fetch('/verify',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:t})});
 const d=await resp.json();
 r.innerHTML='<b>'+d.verification+'</b><br><small>'+d.text_received.substring(0,80)+'</small><br><br><b style=color:#00c853>'+d.earned+' Earned ✓</b>';
}
</script></body></html>
"""
