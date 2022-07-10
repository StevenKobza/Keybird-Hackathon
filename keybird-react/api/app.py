from flask import Flask, request
import time
import os

app = Flask(__name__)

@app.route('/api/uploadfile', methods=["GET", "POST"])
def form_example():
    #print(os.getcwd())
    request_data = request.files
    print(request_data)
    print(request_data["myFile"])
    print(os.getcwd())
    #path = "../../../Keybird-Hackathon/Deep Learning/gen_file"
    if "gen_file" in os.listdir(os.getcwd()) or "gen_file" in os.getcwd():
        path = os.getcwd() + "/gen_file/"
        os.chdir(path)
    else:
        os.mkdir("gen_file")
    
    file_name = str(int(time.time())) + ".wav"
    request_data["myFile"].save(file_name)
    path = "../"
    os.chdir(path)
    print(os.getcwd())
    #print(exec(open("gen_json.py").read()))
    #os.remove("gen_file/" + file_name)
    return 'Form Data Example'