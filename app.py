from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Benglaru, India',
  'salary': 'Rs. 1,00,000'
}, {
  'id': 2,
  'title': 'Software Engineer',
  'location': 'Delhi, India',
  'salary': 'Rs. 1,50,000'
}, {
  'id': 3,
  'title': 'Frontend Developer',
  'location': 'Remote',
  'salary': 'Rs. 1,60,000'
}, {
  'id': 3,
  'title': 'Backend Developer',
  'location': 'San Francisco, USA',
  'salary': '$120,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

# {% for job in jobs %}
#       {% include 'blogitem.html' %}
#     {% endfor %}
