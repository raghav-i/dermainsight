from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename
import torch
from PIL import Image
import torchvision.transforms as T
import os

app = Flask(__name__)
app.config['UPLOAD_PATH'] = '/path/to/your/upload/folder'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.jpeg', '.png']

def predict(model, img, tr, classes):
    img_tensor = tr(img)
    out = model(img_tensor.unsqueeze(0))
    pred, idx = torch.max(out, 1)
    return classes[idx]

def get_transforms():
    transform = []
    transform.append(T.Resize((512, 512)))
    transform.append(T.ToTensor())
    return T.Compose(transform)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    res = None
    if request.method == 'POST':
        classes = ['acanthosis-nigricans', 'acne', 'acne-scars', 'alopecia-areata', 'dry', 'melasma', 'oily', 'vitiligo', 'warts']
        f = request.files['file']
        if f.filename != '':
            filename = secure_filename(f.filename)
            if any(filename.endswith(ext) for ext in app.config['UPLOAD_EXTENSIONS']):
                path = os.path.join(app.config['UPLOAD_PATH'], filename)
                f.save(path)
                model = torch.load('/path/to/your/model/skin-model-pokemon.pt', map_location=torch.device('cpu'))
                device = torch.device('cpu')
                model.to(device)
                img = Image.open(path).convert("RGB")
                tr = get_transforms()
                res = predict(model, img, tr, classes)

    styles_url = url_for('static', filename='css/style.css')
    main_js_url = url_for('static', filename='js/main.js')

    return render_template("index.html", res=res, styles_url=styles_url, main_js_url=main_js_url)

if __name__ == "__main__":
    app.run(debug=True)
