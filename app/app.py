from flask import Flask, request, Response
from flask.templating import render_template
from flask import request
from werkzeug.utils import secure_filename
import torch
from PIL import Image
import torchvision.transforms as T
import os
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired



app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_PATH'] = 'static/uploads'


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    res = None
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_PATH'],secure_filename(file.filename))) # Then save the file
    if request.method == 'POST':
        classes = ['acanthosis-nigricans',
                'acne',
                'acne-scars',
                'alopecia-areata',
                'dry',
                'melasma',
                'oily',
                'vitiligo',
                'warts']
        # f = request.files['file']
        # filename = secure_filename(f.filename)
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_PATH'],secure_filename(file.filename))
        model = torch.load('./skin-model.pt', map_location=torch.device('cpu'))
        device = torch.device('cpu')
        model.to(device)
        img = Image.open(path).convert("RGB")
        tr = get_transforms()
        res = predict(model, img, tr, classes)

    return render_template("index.html", form = form, res = res)

def get_transforms():
    transform = []
    transform.append(T.Resize((512, 512)))
    transform.append(T.ToTensor())
    return T.Compose(transform)

def predict(model, img, tr, classes):
    img_tensor = tr(img)
    out = model(img_tensor.unsqueeze(0))
    pred, idx = torch.max(out, 1)
    return classes[idx]





if __name__ == '__main__':
    app.run(debug=True)