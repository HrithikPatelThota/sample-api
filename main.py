from flask import Flask, jsonify

app = Flask(__name__)

courses = [{'name': "Python Programming Certification",
            'course_id': 0,
            'Description': "...Hrithik...",
            'Price': "1000"},
           {'name': "Python Programming Certificate",
            'course_id': 1,
            'Description': "...Parthiv...",
            'Price': "2000"}
           ]


@app.route('/')
def index():
    return "finally created API"


@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses': courses})


@app.route("/courses/<int:course_id>", methods=['GET'])
def get_courseid(course_id):
    return jsonify({'course': courses[course_id]})


if __name__ == "__main__":
    app.run(debug=True)
