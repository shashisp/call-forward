from flask import Flask, render_template, request, make_response
import plivo
from app import app


auth_id = "MAY2Q3ZGQ1MDIWODRJY2"
auth_token = "YTRkMzAyMzc4ZTU1NDA4NWMyYzI1MjNlOWQ1OGY1"

#CALLER_ID = "14075303731"

p = plivo.RestAPI(auth_id, auth_token)   
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/forward/', methods=['GET'])
def forward():

    CALLER_ID = request.args.get('caller_id')
    MOBILE = request.args.get('mobile')
    SIP = request.args.get('sip')
    timeout_period = request.args.get('timeout')
 
    CALLER_NAME = "essp"
    response=plivo.Response()
    response.addWait(length=10)
    response.addSpeak("Please wait we are forwarding your call")
    response.addDial(callerName=CALLER_NAME).addUser(SIP)
    response.addDial(timeout = 10, callerId=CALLER_ID).addNumber(MOBILE)
    response.addSpeak("Redirecting to Voicemail, Please leave your message")
    response=make_response(response.to_xml())
    response.headers['Content-Type']='text/xml'
    
    return response
	
	
	
	
	
  	
	
    
	
   
