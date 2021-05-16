import os
from flask import Flask, render_template, Response, request, send_from_directory
from flask_cors import CORS
import json
import io
import database

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

HOST_IP = "localhost"
API_PORT = "3090"

# Status check
@app.route('/api/status',methods=['GET','HEAD'])
def api_status():
	return Response("Database is running ...", status=200)

@app.route('/api/get/<function_name>', methods=['GET'])
def get_functions(function_name: str):
    try:
        function = getattr(database, function_name)
    except:
        return json.dumps({'success':False, 'error': "Function not found."}), 400, {'ContentType':'application/json'} 
    args = request.args.to_dict(flat=True)
    if args is None:
        args = {}
    response = function(args)
    if not response:
        return Response(json.dumps({ }, default=lambda o: o.__dict__, sort_keys=False, indent=4))
    return Response(json.dumps(response, default=lambda o: o.__dict__, sort_keys=False, indent=4))

@app.route('/api/post/date', methods=['POST'])
def api_post_date():
    database.insert_date(request.json['date'])
    print("Date inserted")
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == "__main__":
	app.run(HOST_IP, port=API_PORT)