from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id':1,
  'title':'Financial Analyst',
  'location':'New Haven, CT',
   'salary': '$ 95,000', 
},
{
  'id':2 ,
  'title':'Data Analyst',
  'location':'Hamden, CT',
   'salary': '$ 85,000', 
},
{
  'id':3 ,
  'title':'Contract Analyst',
  'location':'Bridgeport, CT',
   'salary': '$ 80,000', 
},
{
  'id':4 ,
  'title':'Sales Analyst',
  'location':'Stamford, CT',
   'salary': '88,000', 
}

]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                          jobs = JOBS,
                          company_name="Dwight")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True )

