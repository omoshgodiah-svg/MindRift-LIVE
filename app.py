from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
balance = 0.0

def verify_customers(age, photos, has_filters):
    if age < 18 or age > 30:
        return False, "REJECTED: Age 18-30"
    if photos !=2:
        return False, "REJECTED: 2 photos needed"
    if has_filters:
        return False, "REJECTED: Beauty filter detected"
    return True, "ACCEPTED"

@app.route('/')
def home(): return render_template('index.html')

@app.route('/verify', methods = ['POST'])
def verify():
    global balance
    data = request.json 
    ok, msg = verify_customers(int(data['age']), int(data['photos']), False)
    if ok: balance +=0.07
    return jsonify({"msg":msg,"accepted":ok,"balance": round(balance,2)})

if __name__ == '__main__':
    app.run()
