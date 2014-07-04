from flask import Flask, render_template, request, make_response
import plivo
from app import app


auth_id = "MAY2Q3ZGQ1MDIWODRJY2"
auth_token = "YTRkMzAyMzc4ZTU1NDA4NWMyYzI1MjNlOWQ1OGY1"

CALLER_ID = "14075303731"

p = plivo.RestAPI(auth_id, auth_token)   
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/forward/', methods=['GET'])
def forward():

    #MOBILE = "9035162272"
    MOBILE = request.args.get('mobile')
    #SIP = "sip:shashisp140702194927@phone.plivo.com"
    SIP = request.args.get('sip')

    CALLER_NAME = "essp"
    response=plivo.Response()
    response.addSpeak("Please wait while we are forwarding your call")
    response.addDial(callerName=CALLER_NAME).addUser(SIP)
    response.addDial(callerId=CALLER_ID).addNumber(MOBILE)
    response=make_response(response.to_xml())
    response.headers['Content-Type']='text/xml'
    
    return response
	
	
	
	# response.addSpeak("The number you're trying is not reachable at the moment. You are being redirected to the voice mail")
	# response.addDial(callerId=CALLER_ID,
			# action=BASE_URL+url_for('voice_mail'),
			# method='GET').addNumber(VOICEMAIL_NUMBER)
	
	
  	
	
    
	#CALLER_NAME = "essp"
	# CALLER_NAME,SIP,MOBILE,VOICEMAIL_NUMBER=get_details_from(plivo_number)
	
   
