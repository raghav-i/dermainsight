# Derma Insight

Derma Insight is a web application designed to help users analyze their skin type and identify potential skin diseases using machine learning techniques. The application allows users to upload images of their skin, which are then processed using a pre-trained deep learning model to provide insights and recommendations.


# Features

- Skin Type Analysis: Users can upload images of their skin to determine their skin type, whether it's oily, dry, or normal.
- Skin Disease Detection: The application identifies potential skin diseases such as acne, alopecia areata, melasma, vitiligo, and more.
- Educational Resources: Derma Insight provides educational resources and information about various skin diseases and conditions.


# Technologies Used

- Python: The backend logic and machine learning model are implemented using Python.
- Flask: Derma Insight is built as a web application using the Flask web framework, allowing for easy deployment and scalability.
- PyTorch: The machine learning model for skin disease detection is built using PyTorch, a popular deep learning framework.
- HTML/CSS/JavaScript: The frontend of the application is implemented using HTML, CSS, and JavaScript to provide an interactive user experience.
- Werkzeug: Werkzeug is used for handling file uploads securely within the Flask application.


# About the Model - EfficientNetB0

The project utilizes the **EfficientNet-B0** architecture, renowned for its efficient balance between model size and computational performance. 

- Transfer learning with pre-trained weights from ImageNet accelerates adaptation to skin condition classification, reducing the need for extensive training data. 
- Feature extraction with frozen layers conserves computational resources and mitigates overfitting risks, enhancing fine-tuning effectiveness.
- Regularization techniques, including dropout and batch normalization, enhance model generalization by preventing overfitting. 
- Data augmentation, such as random flips and rotations, increases dataset variability, improving model robustness. These techniques collectively optimize model performance and enable accurate skin condition classification.

# Screenshot

![website](https://github.com/raghav-i/dermainsight/blob/main/dermainsight.jpeg)

# Getting Started

Pre-requisites: 
- Pillow 9.0.1
- torch 2.2.1
- torchvision 0.17.1


To run the model locally, run the following in terminal:

```
$ git clone https://github.com/raghav-i/dermainsight.git
$ cd dermainsight
$ python3 -m venv skin-class-env
$ source skin-class-env/bin/activate
$ python3 predict.py -m "Path to torch model" -i "Path to image"
```


# License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/raghav-i/dermainsight/blob/main/LICENSE) file for details.

