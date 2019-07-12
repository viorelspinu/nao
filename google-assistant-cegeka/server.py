from flask import Flask, render_template, request, send_from_directory
from werkzeug import secure_filename
import os

app = Flask(__name__)


	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      os.system("rm ./*.ogg")
      os.system("rm ./*.wav")
      f.save("sound_record.wav")
      os.system("./push-to-talk.sh")
      return send_from_directory(directory="./", filename="response_robot.wav")
		
if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')