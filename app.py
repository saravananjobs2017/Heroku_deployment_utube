# This is a sample Python script.

from pytube import YouTube
from flask import *

app = Flask(__name__)


@app.route('/',methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def renderHomePage():

    link_to_download = request.form['URL']
    download_metrics = YouTube(link_to_download)
    file = download_metrics.streams.get_highest_resolution()
    file.download()
    return 'download completed'


if __name__ == '__main__':
    app.run(debug=True)
