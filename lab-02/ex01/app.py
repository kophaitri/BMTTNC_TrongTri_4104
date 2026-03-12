from flask import Flask, render_template, request
# Đảm bảo bạn đã để file RailFenceCipher trong thư mục cipher hoặc cùng cấp
from cipher.railfence.rail_fence_cipher import RailFenceCipher 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/railfence")
def railfence_page():
    return render_template('railfence.html')

@app.route("/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form.get('inputPlainText')
    # Rail Fence cần số lượng đường ray (integer)
    try:
        num_rails = int(request.form.get('inputRails', 3))
    except:
        num_rails = 3
    
    cipher = RailFenceCipher()
    result = cipher.ma_hoa_duong_ray(text, num_rails)
    
    return render_template('railfence.html', 
                           result_encrypt=result, 
                           old_text_encrypt=text, 
                           old_rails_encrypt=num_rails)

@app.route("/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form.get('inputCipherText')
    try:
        num_rails = int(request.form.get('inputRails', 3))
    except:
        num_rails = 3
    
    cipher = RailFenceCipher()
    result = cipher.giai_ma_duong_ray(text, num_rails)
    
    return render_template('railfence.html', 
                           result_decrypt=result, 
                           old_text_decrypt=text, 
                           old_rails_decrypt=num_rails)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3636, debug=True)