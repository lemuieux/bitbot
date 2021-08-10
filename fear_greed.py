import requests
import json

url = "https://api.alternative.me/fng/?limit="
#querystring = {'limit':'7'}

def fear_day():
    _url = url+"1"
    res = requests.request("GET", _url);
    
    # 파싱
    parsed = json.loads(res.text)
    data = parsed["data"]
    
    return data[0]["value"]
    # for index, value in enumerate(data):
    #     print(str(index) + ":" +value["value"])
        
    # 출력
    # output = json.loads(res.text)
    # print(json.dumps(output, indent=4))
        
def fear_yester():
    _url = url+"2"
    res = requests.request("GET", _url);
    
    #파싱
    parsed = json.loads(res.text)
    data = parsed["data"]

    return data[1]["value"]
    
    # 출력
    # output = json.loads(res.text)
    # print(json.dumps(output, indent=4))

def fear_twodaysago():
    _url = url+"3"
    res = requests.request("GET", _url);
    
    # 파싱
    parsed = json.loads(res.text)
    data = parsed["data"]

    return data[2]["value"]

    # 출력
    # output = json.loads(res.text)
    # print(json.dumps(output, indent=4))
    
def fear_week():
    _url = url+"7"
    res = requests.request("GET", _url);
    
    parsed = json.loads(res.text)
    data = parsed["data"]
    
    sum = 0
    for index, value in enumerate(data):
        sum += int(value["value"])
        
    return sum/7
    
    # 출력
    # output = json.loads(res.text)
    # print(json.dumps(output, indent=4))
    
def fear_month():
    _url = url+"30"
    res = requests.request("GET", _url);
    
    parsed = json.loads(res.text)
    data = parsed["data"]

    sum = 0
    for index, value in enumerate(data):
        sum += int(value["value"])
    
    return sum/30

    # 출력
    # output = json.loads(res.text)
    # print(json.dumps(output, indent=4))
    

# test
# print(fear_day())
# print(fear_yester())
# print(fear_twodaysago())
# print(fear_week())
# print(fear_month())