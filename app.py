from flask import Flask,render_template,redirect,jsonify, request
import base64
from pymongo import MongoClient
import certifi


app = Flask(__name__, static_url_path='/static')
app.config["MONGO_URI"] = "mongodb+srv://Pranav:Pranav369@new.srmghf6.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient("mongodb+srv://Pranav:Pranav369@new.srmghf6.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client.get_database('memories')

records = db.demo
app = Flask(__name__,static_url_path='/static/')

@app.route("/")
def main():
    return render_template("index.html")





@app.route("/frames",methods=["GET"])
def frames():
    frame = records.find({})
    return render_template("frames.html", frame=frame)

@app.route("/add_frames")
def add_frames():
    return render_template("add_frames.html")

@app.route("/insert", methods=["POST"])
def insert():
    image = request.files['img']
    if image:

        image_data = image.read()
        image_base64 = base64.b64encode(image_data).decode('utf-8')

        records.insert_one({
            "image_data": image_base64,
        })
        return redirect('/frames')


@app.route("/thanks")
def thanks():
    return render_template("thanks.html")


@app.route("/frames/delete/<img>", methods=["GET"])
def delete(img):
    records.delete_one({"image": img})
    return redirect("/frames")

if __name__ == "__main__":
    app.run()  
