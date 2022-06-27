from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        'id':1,
        'name':'Preetika',
        'contact':'832776497'
    },
    {
        'id':2,
        'name':'Yati',
        'contact':'9372659987'
        
    }
]
@app.route("/")
def gettask():
    return jsonify({ 
        'data':tasks
    })
@app.route('/add_data',methods=['POST']) 
def add_data():
    if not request.josn:
        return jsonify({
            'mesaage':'please provide data'
        })

    task={
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact','') 
           }
    tasks.append(task) 
    return jsonify({
        'message':'contact added sucessefully'
    })      

if(__name__=='__main__'):
    app.run()
