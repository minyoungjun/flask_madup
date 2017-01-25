import os
from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

@app.route('/')

def hello_world():
    print ("===================")
    print ("my first flask app!")
    print ("===================")
    return 'Hello World!'

@app.route('/<tracking_tool>/postback', methods=['GET'])

def postback_url(tracking_tool):
    integration_id = request.args.get('cb_param1')
    click_id = request.args.get('cb_param2')
    result = '트래킹 툴: %s <br> 연동아이디: %s <br> 클릭로그ID: %s' % (tracking_tool, integration_id, click_id)
    return result

@app.route('/<affiliate>', methods=['GET'])

def click_url(affiliate):
    print("========연동 ID=========")
    print(request.args.get('token'))
    print("========================")
    print("========CLICK ID========")
    print(request.args.get('click_id'))
    print("========================")
    
    print("========SUB_N1========")
    print(request.args.get('sub_n1'))
    print("========================")
    
    print("========SUB_N2========")
    print(request.args.get('sub_n2'))
    print("========================")
    
    return redirect("https://ref.ad-brix.com/v1/referrallink?ak=622899021&ck=6399150&sub_referral=8221068", code=302)


if __name__ == '__main__':
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
