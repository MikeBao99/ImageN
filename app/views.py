from flask import * #TODO: actually look at imports
import boto3
import requests
import json
from werkzeug import * #TODO: actually look at imports

views = Blueprint('views', __name__)

extensions = set(['jpg'])

def file_allowed(file):
    return '.' in file and \
           file.rsplit('.', 1)[1] in extensions

@views.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
#         print str(request.files)
#         if not len(request.files) == 0:
#             return render_template('homepage.html', WordCount = "No File Found")
        #ocr-im = ocr_space_url(url='https://s3.us-east-2.amazonaws.com/imagen50/IMG_1732.JPG')
        s3 = boto3.resource('s3')
#         s3.Bucket('imagen50').put_object(Key=request.files['input-b1'].filename, Body=request.files['input-b1'].stream.read())
        
#         name = request.files['input-b1'].filename
#         formatted_name = ''
#         for let in name:
#             if let == '.':
#                 break
#             else:
#                 formatted_name = formatted_name + let
        bucket = s3.Bucket('imagen50')
        bucket.upload_fileobj(request.files['input-b1'], request.files['input-b1'].filename, ExtraArgs={'ContentType': 'image/jpeg'})
#         formatted_name = formatted_name + '.JPG'
        
#         s3_object = s3.Object('imagen50', request.files['input-b1'].filename)
#         s3_object.metadata.update({'Content-Type':'image/jpg'})
#         s3_object.copy_from(CopySource={'Bucket':'imagen50', 'Key':request.files['input-b1'].filename}, Metadata=s3_object.metadata, MetadataDirective='REPLACE')
        
        return render_template('homepage.html', WordCount =  json.loads(ocr_space_url(url='https://s3.us-east-2.amazonaws.com/imagen50/%s' % request.files['input-b1'].filename))['ParsedText'])
        #return render_template('homepage.html', WordCount = "We Win!!")
    else:
        return render_template('homepage.html', WordCount = "")

@views.route('/about')
def about():
    return render_template('about.html')


def ocr_space_file(filename, overlay=False, api_key='6960bb930988957', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()



