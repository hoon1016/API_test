from flask import Flask

app = Flask(__name__)

# get localhost:포트번호/

@app.route('/', methods = ['GET'])
def hello_world():
    return 'Hello World'
    

if __name__=="__main__":
    app.run()

