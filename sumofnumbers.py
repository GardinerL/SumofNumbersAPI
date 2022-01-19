from flask import Flask, jsonify, request, abort
app=Flask(__name__)

#numbers_to_add = list(range(10000001))
#Assumes request is a JSON and response should be returned as a JSON.

def bad_request(message):
    response = jsonify({'bad_request': message})
    response.status_code = 400
    return response

@app.route('/total',methods=['POST'])
def total(): 
    if request.is_json is False:
        return bad_request("the request should be a JSON")
    else:
        data = request.get_json()
        if 'numbers_to_add' not in data.keys():
            return bad_request("numbers_to_add key missing from JSON")

        elif type(data['numbers_to_add']) is not list: 
            return bad_request(f"format of numbers_to_add value is {data['numbers_to_add']} but should be e.g. [1,2,3]")
        
        elif not all(isinstance(x, (int,float)) for x in data['numbers_to_add']):
            return bad_request("List of numbers contains something other than integer or float")
        
        elif len(data['numbers_to_add']) <=1:  
            return bad_request("List of numbers contains 1 number or less")
        
        else: 
            total = sum(data['numbers_to_add'])
            return(jsonify({'total': total}),200)

if __name__ == "__main__":
    app.run(debug=True, port=int(5000))

