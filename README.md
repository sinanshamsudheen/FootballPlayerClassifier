# Football Player Classifier

## Project Overview
Football Player Classifier is an **end-to-end machine learning project** that identifies football players from images. This project covers the full pipeline from **data collection to deployment on AWS EC2**, integrating an **SVM-based classification model**, a **Flask backend**, and a **web frontend** for real-time image classification.

## Key Features
- **Automated Image Collection**: Utilized Bing Image Downloader to gather player images.
- **Machine Learning Model**: Trained an **SVM classifier** to distinguish players like Messi, Ronaldo, Neymar, etc.
- **Flask API**: Built a backend API for processing images and returning predictions.
- **Web Interface**: Developed a simple UI for image uploads and real-time classification.
- **Wavelet Transform**: Applied preprocessing techniques for feature enhancement.
- **Cloud Deployment**: Deployed the model and API on **AWS EC2** for accessibility and scalability.

## Technologies Used
- **Python** (OpenCV, Scikit-Learn, Flask)
- **Machine Learning** (Support Vector Machine, Feature Engineering)
- **Cloud Deployment** (AWS EC2, Flask API, Model Serialization with Joblib)
- **Computer Vision** (Image Processing, Wavelet Transform)
- **API Development** (Flask-based Model Integration)

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask
- OpenCV
- Scikit-Learn
- Joblib

### Steps to Run Locally
```bash
# Clone the repository
git clone https://github.com/yourusername/football-player-classifier.git
cd football-player-classifier

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
```
The server will be available at `http://127.0.0.1:5000/`.

## Deployment on AWS EC2
- The Flask API and model are deployed on **AWS EC2**.
- Follow the standard EC2 deployment process, including setting up security groups, SSH access, and running the Flask app on a public IP.

## Usage
1. Upload an image of a football player.
2. The model processes the image and predicts the player's identity.
3. Results are displayed in the web interface.

## Learnings & Impact
- Strengthened **computer vision** and **machine learning** skills.
- Gained hands-on experience in **end-to-end AI development**.
- Learned **cloud deployment strategies** using AWS EC2.

## Contributing
Feel free to fork this repository and contribute! If you find any issues or improvements, submit a pull request.

## License
This project is licensed under the MIT License.

---
Made with ❤️ by Sinan
