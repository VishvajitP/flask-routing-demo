from flask import Flask, url_for, request
app = Flask(__name__)

# we use route() decorator to tell flask what URL should trigger out function

@app.route('/')         # without explicitly mentioning the end point
def hello_world():
    return '<h1> Index Page! </h1>'

@app.route('/hello')  # explicitly mentioning the end point ;  strict_slashes : if
def view_function_hello():
    return 'End Point With Hello'

@app.route('/demo/<end_point>') # variable end point
def variable_end_point(end_point):
    return 'Your end point is :  <br> /demo/%s' % end_point

@app.route('/demo_int/<int:end_point>') # variable end point with given data type ; like- int, float, path
@app.route('/demo_int/', defaults = {"end_point" : 99})  # multiple enpoints associated with same methods
def variable_end_point_data_type(end_point):
    return 'Your end point is :  <br> /demo/%s' % end_point

# Trailing slash dilemma with flask URLs
@app.route('/with_trailing_slash/')
def with_slash():
    return 'with_trailing_slash'

@app.route('/without_trailing_slash')
def without_slash():
    return 'without_trailing_slash'
'''
if trailing slash is mentioned then you can access this end point irrespective of trailing slash mentioned in the request.
In the second case, however, the URL is defined without a trailing slash, rather like the pathname of a file on UNIX-like systems. Accessing the URL with a trailing slash will produce a 404 "Not Found" error.
'''

@app.route('/with_strict_slash_param', strict_slashes=False)
def with_strict_slash():
    return 'No worries about the trailing slashes.'

# the one with methods
@app.route('/with_methods', methods=['GET'])  # supported methods : 'GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD'
def with_methods():
    return 'See how to use methods.'

# you can use multiple methods for one end point
@app.route('/with_methods_multiple', methods=['GET', 'POST'])  # supported methods : 'GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD'
def with_methods_multiple():
    if request.method == 'GET':
        return 'It was a GET.'
    elif request.method == 'POST':   # you can use a REST Client to make a POST call
        return 'It was a POST.'

# you can call the end point associated with a method using `url_for()` function
with app.test_request_context():
    print url_for('hello_world')
    print url_for('variable_end_point_data_type', end_point=100)

if __name__ == '__main__':
    # default port : 5000

    app.run(debug=True)