#!/usr/bin/python
import os,sys
from flask import Flask, jsonify, render_template, request, abort, make_response
from flask import Response
import lxml.etree as etree
import requests
import json

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
file_path = ROOT_PATH + "/" + "rsdl"


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/api/rsdl',methods=['GET','POST'])
def rsdl() :
   parser = etree.XMLParser(ns_clean=True)
   tree   = etree.parse(file_path, parser)
   result =  etree.tostring(tree, pretty_print = False)
   return Response(result, mimetype='application/xml')

@app.route('/')
def webprint():
    return render_template('index.html')

@app.route('/api/weather',methods=['GET','POST'])
def weather() :
   city = request.args.get('city')
   parameters = {"q": city, "appid": "f0f34657beaede0f908cf2218c677927"}
   response=requests.get("http://api.openweathermap.org/data/2.5/weather",parameters)
   result = json.loads(response.content)
   a = result["main"]
   return  jsonify(a)


@app.route('/api/sort',methods=['GET','POST'])
def get_sort():
        a = request.args.get('array')
        a = a.split(',')
        a = list(map(int, a))
        for i in range(1,len(a)):
                tmp = a[i]
                j = i
                while j>0 and a[j-1]>tmp:
                         a[j]=a[j-1]
                         j = j-1
                a[j]=tmp

        return jsonify({'result': a})

@app.route('/api/wordfreq', methods = ['GET', 'POST'])
def upload_file():
    count = 0
    a = request.form['word']
    f = request.files['file']
    for i in f.read(102400).split():
        if a == i.strip('.,;:"\''):
                count=count+1
    return jsonify({"result":count})

@app.route('/api/prime',methods=['GET','POST'])
def get_prime():
        a = request.args.get('number')
        cou = 0
	n = int(a)
        if n == 1:
        	return jsonify({'result': "Not a Prime Number"})
        elif n > 1 :
		for i in range(2,n):
        		if n%i == 0 :
        			cou = cou + 1
		if cou == 0:
        		return jsonify({'result': "Prime Number"})
		else:
			return jsonify({'result': "Not a Prime Number"})
        else:
        	return jsonify({'result':'error:number should be a positive integer'})
if __name__ == '__main__':
    app.run()

