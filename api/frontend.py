import flask

from flask import request, jsonify, render_template, redirect
import os
import sys


#IMAGES_FOLDER = os.path.join('static', 'images')
LOGS_FOLDER = "/event logs"

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = LOGS_FOLDER

import requests
import graphviz
from graphviz import Digraph
from pm4py.visualization.dfg import visualizer as dfg_visualization

  
@app.route('/', methods=['GET'])
def home():
    
    #freq =requests.get('http://127.0.0.1:7777/dfgFrequency')
    #perf =requests.get('http://127.0.0.1:7777/dfgPerformance')
    #median =requests.get('http://127.0.0.1:7777/median')
    #total =requests.get('http://127.0.0.1:7777/total')
        
    
    #print(total.text)
    #freq_png = graphviz.Source(freq.text, filename="frequency", format="png")
    #dfg_visualization.save(freq_png, "static/images/frequency.png")
    #freq_img = os.path.join(app.config['UPLOAD_FOLDER'], 'frequency.png')

    #perf_png = graphviz.Source(perf.text, filename="performance", format="png")
    #dfg_visualization.save(perf_png, "static/images/performance.png")
    #perf_img = os.path.join(app.config['UPLOAD_FOLDER'], 'performance.png')
    '''
    return render_template("index.html", \
        stringF = str(freq.text), \
        stringP = str(perf.text), \
        median = median.text, \
        total = total.text, \
        myPathF_init = "100", \
        myActF_init = "100", \
        myPathP_init = "100", \
        myActP_init = "100", \
        perf_checked = "false" ) 
    '''
    return render_template("index.html", \
        stringF = "", \
        stringP = "", \
        median = "", \
        total = "", \
        myPathF_init = "100", \
        myActF_init = "100", \
        myPathP_init = "100", \
        myActP_init = "100", \
        perf_checked = "false" ) 
    
    #return render_template("viz-js.html")
    
    
    #return "<h1>This is just an example</h1><p>Here, you should see the Digraph in a String format.</p><img src='dfg.png'>" 

    '''
@app.route('/', methods=['GET', 'POST'])
def myPost():
    
    perfCheck = request.args.get('perf_checked')
    print(perfCheck)
    
    if perfCheck == None:
        return dfgFrequency()

    else:
        return dfgPerformance()
    '''

    '''
    median =requests.get('http://127.0.0.1:7777/median')
    total =requests.get('http://127.0.0.1:7777/total')
        
        
    myPathP = request.form.get('myPathP')
    myActP = request.form.get('myActP')
    myPathF = request.form.get('myPathF')
    myActF = request.form.get('myActF')
    perfCheck = request.form.get('perf_checked')
    
    if perfCheck == None:
        perfCheck = "false";
    else:
        perfCheck = "true";
        
    
    #path = request.args.get('myPathF')
    paramsF = {'myPathF' : myPathF, 'myActF' : myActF}
    paramsP = {'myPathP' : myPathP, 'myActP' : myActP}
    f = requests.get('http://127.0.0.1:7777/dfgFreqReduced', params = paramsF)
    p = requests.get('http://127.0.0.1:7777/dfgPerfReduced', params = paramsP)
    
   
    #f = requests.post('http://127.0.0.1:7777/dfgFreqReduced', path)
    #f = requests.get('http://127.0.0.1:7777/dfgFreqReduced?myPahtF='+path)
    print(request.form.get('updated'))
    if request.form.get('updated') != None:
        f = request.files['file']
        if f.filename != '': 
          #f.save("event logs/" + f.filename)
          f.save("event logs/running-example.xes")
          return home()      
      
    return render_template("index.html", \
        stringF = str(f.text), \
        stringP = str(p.text),\
        median = median.text, \
        total = total.text, \
        myPathF_init = myPathF, \
        myActF_init = myActF, \
        myPathP_init = myPathP, \
        myActP_init = myActP, \
        perf_checked = perfCheck )
        
    '''
    
    
    '''
    #if request.method == 'POST' and request.form.get("frequency") != '':
    if request.form.get("tabType") == 'frequency':
        if request.form.get('myPathF') != '':
            myPathF = request.form.get('myPathF')
            myActF = request.form.get('myActF')
            
            #path = request.args.get('myPathF')
           
            params = {'myPathF' : myPathF, 'myActF' : myActF}
            f = requests.get('http://127.0.0.1:7777/dfgFreqReduced', params = params)
            perf =requests.get('http://127.0.0.1:7777/dfgPerformance')
           
            #f = requests.post('http://127.0.0.1:7777/dfgFreqReduced', path)
            #f = requests.get('http://127.0.0.1:7777/dfgFreqReduced?myPahtF='+path)
            return render_template("index.html", \
                stringF = str(f.text), \
                stringP = str(perf.text), \
                median = median.text, \
                total = total.text, \
                myPathF_init = myPathF, \
                myActF_init = myActF, \
                myPathP_init = "0", \
                myActP_init = "100" )
            
    if request.form.get("tabType") == 'performance':
        if request.form.get('myPathP') != '':
            myPathP = request.form.get('myPathP')
            myActP = request.form.get('myActP')
            myPathF = request.form.get('myPathF')
            myActF = request.form.get('myActF')
            
            #path = request.args.get('myPathF')
            paramsF = {'myPathP' : myPathF, 'myActP' : myActF}
            paramsP = {'myPathP' : myPathP, 'myActP' : myActP}
            f = requests.get('http://127.0.0.1:7777/dfgFreqReduced', params = paramsF)
            p = requests.get('http://127.0.0.1:7777/dfgPerfReduced', params = paramsP)
            
           
            #f = requests.post('http://127.0.0.1:7777/dfgFreqReduced', path)
            #f = requests.get('http://127.0.0.1:7777/dfgFreqReduced?myPahtF='+path)
            return render_template("index.html", \
                stringF = str(f.text), \
                stringP = str(p.text),\
                median = median.text, \
                total = total.text, \
                myPathF_init = myPathF, \
                myActF_init = myActF, \
                myPathP_init = myPathP, \
                myActP_init = myActP )
    '''      


@app.route('/', methods = ['POST'])
def upload_file():
  f = request.files['file']
  if f.filename == '':
    print("empty")
  #f.save("event logs/" + f.filename)
  f.save("event logs/running-example.xes")
  return home()
  #return redirect("http://127.0.0.1:8080", code=200)

@app.route('/petriFreq', methods=['GET', 'POST'])
def petriFreq():
    
    petriF = requests.get('http://127.0.0.1:7777/petriNetFreq')

    return str(petriF.text)
    
@app.route('/petriPerf', methods=['GET', 'POST'])
def petriPerf():
    
    petriP = requests.get('http://127.0.0.1:7777/petriNetPerf')

    return str(petriP.text)
    
@app.route('/bpmn', methods=['GET', 'POST'])
def bpmn():
    
    bpmn = requests.get('http://127.0.0.1:7777/bpmn')

    return str(bpmn.text)

@app.route('/dfgFrequency', methods=['GET', 'POST'])
def dfgFrequency():
    # GET request
    #if request.method == 'GET':
    f = requests.get('http://127.0.0.1:7777/dfgFrequency')
    #myPathF = request.form.get('myPathF')
    myPathF = request.args.get('myPathF')
    #myActF = request.form.get('myActF')
    myActF = request.args.get('myActF')
    #perfCheck = request.form.get('perf_checked')
    perfCheck = request.args.get('perf_checked')

    if perfCheck == None:
        perfCheck = "false";
    else:
        perfCheck = "true";
        
    
    #path = request.args.get('myPathF')
    paramsF = {'myPathF' : myPathF, 'myActF' : myActF}
    f = requests.get('http://127.0.0.1:7777/dfgFreqReduced', params = paramsF)

    #if request.form.get('updated') != None:
    if request.args.get('updated') != None:
        f = request.files['file']
        if f.filename != '': 
          #f.save("event logs/" + f.filename)
          f.save("event logs/running-example.xes")
          return home()      
      
        
    return str(f.text)
    '''
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200 
    '''  

@app.route('/dfgPerformance', methods=['GET', 'POST'])
def dfgPerformance():
    # GET request
    if request.method == 'GET':
        myPathP = request.args.get('myPathP')
        myActP = request.args.get('myActP')
        perfCheck = request.args.get('perf_checked')
    
    if perfCheck == None:
        perfCheck = "false";
    else:
        perfCheck = "true";
        
    
    #path = request.args.get('myPathF')
    paramsP = {'myPathP' : myPathP, 'myActP' : myActP}
    p = requests.get('http://127.0.0.1:7777/dfgPerfReduced', params = paramsP)

    print(request.form.get('updated'))
    if request.form.get('updated') != None:
        f = request.files['file']
        if f.filename != '': 
          #f.save("event logs/" + f.filename)
          f.save("event logs/running-example.xes")
          return home()      
      
        
  
    return str(p.text)
    '''
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200     
    '''
app.run(host='127.0.0.1', port=8080)