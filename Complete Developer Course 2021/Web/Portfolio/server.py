from flask import Flask, request, render_template, redirect
import csv
app = Flask(__name__)

def write_to_file(data):
  with open('database.txt', mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
  with open('database.csv', newline='', mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email, subject, message])



@app.route("/")
def my_home():
  return render_template('index.html')

@app.route("/<page_name>")
def page(page_name):
  return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
    try:
      data = request.form.to_dict()
      write_to_file(data)
      write_to_csv(data)
    except:
      return 'did not save to database'
    return redirect('/thank_you.html')
  return 'something went wrong'

