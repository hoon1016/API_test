#JSON 형식으로 메세지 처리하기
from flask import Flask, request
# HTTP의 상태코드를 전송할 수 있습니다.
from http import HTTPStatus

app = Flask(__name__)

# get localhost:포트번호/

@app.route('/', methods = ['GET'])
def hello_world():
    return 'Hello World'
    
@app.route('/act', methods = ['GET'])
def act() :
    ret = {'count' : 2 ,
            'students' : [
                {'name' : '홍길동','age' : 30},
                {'name' : '김나나','age' : 25}
            ]
    }
    return ret 

#두개의 숫자를 클라이언트에게 받는다.
#받은 두 숫자를 더해서, 클라이언트에 리스판스 
@app.route('/add_two_nums', methods = ['POST'])
def add_two_nums():
    data = request.get_json()

    #data = { "x" : 345 , "y" : 827 }
    print(data)

    if 'x' not in data or 'y' not in data :
        return {'message' : '파라미터 잘못됬다.'}, HTTPStatus.BAD_REQUEST

    x = data['x']
    y = data['y']

    z = x + y

    ret = {'sum' : z }

    return ret, HTTPStatus.UNAUTHORIZED

if __name__=="__main__":
    app.run()

