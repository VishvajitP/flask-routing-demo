from flask import Flask, url_for
app = Flask(__name__)

# we use route() decorator to tell flask what URL should trigger out function

@app.route('/')         # without explicitly mentioning the end point
def hello_world():
    return '<h1> Index Page! </h1>'

@app.route('/hello')  # explicitly mentioning the end point
def view_function_hello():
    return 'End Point With Hello'

@app.route('/demo/<end_point>') # variable end point
def variable_end_point(end_point):
    return 'Your end point is :  <br> /demo/%s' % end_point

@app.route('/demo_int/<int:end_point>') # variable end point with given data type ; like- int, float, path
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

# you can call the end point associated with a method using `url_for()` function
with app.test_request_context():
    print url_for('hello_world')
    print url_for('variable_end_point_data_type', end_point=100)

if __name__ == '__main__':
    # default port : 5000

    app.run(debug=True)