from flask import Flask ,url_for ,redirect ,render_template ,request
app = Flask(__name__)
import pyrebase
from firebase import Firebase

config = {
            "apiKey": "AIzaSyCsmHR5hm0RFUud2ne1SjKHYb03PCFXMDU",
            "authDomain": "svg-to-png-6f884.firebaseapp.com",
            "projectId": "svg-to-png-6f884",
            "storageBucket": "svg-to-png-6f884.appspot.com",
            "messagingSenderId": "21624816502",
            "appId": "1:21624816502:web:c5906ae0272db555ab3057",
            "measurementId": "G-C3D4TL0CCR"
        }

@app.route("/upload", methods=["POST","GET"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
            return redirect(request.url)
    return render_template("upload_image.html")
    fb = pyrebase.initialize_app(config) 
    storage = fb.storage()
    storage.child(image).put(image)

## get the url in post body and download the image 
## convert image to png 
## upload the image to storage 
## return ajson with new image url 
    
if __name__ == "__main__":
    app.run(debug=True)


