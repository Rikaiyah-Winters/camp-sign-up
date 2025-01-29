from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campers.db"
db = SQLAlchemy(app)

class Camper(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  age = db.Column(db.String(80), nullable=False)
  phone_number = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(80), unique=True, nullable=False)
  address = db.Column(db.String(80), unique=True, nullable=False)
  t_shirt_size = db.Column(db.String(80), nullable=False)

  def __repr__(self):
    return "<Tallon Camper: "+ self.name + " is " + self.age + " years old and has a " + self.t_shirt_size + " t-shirt size>"

#with app.app_context():
#   db.create_all()
#   db.session.commit()

@app.route("/", methods=["GET"])
def camper_form():
  return render_template("form.html", errors=[])

@app.route("/list")
def camper_list():
   return render_template("list.html", campers=Camper.query.all())

@app.route("/delete", methods=["GET"])
def delete_camper():
   return render_template("delete.html", errors=[])

@app.route("/addCamper", methods=["POST"]) # this is the PROCESS of POSTING whatever the user submits in the form TO the Database
def add_camper():
  errors = []
  name = request.form.get("name")
  if not name:
     errors.append("Please add First and Last name of camper.")
  age = request.form.get("age")
  if not age:
     errors.append("Please add age of camper.")
  phone_number = request.form.get("number")
  if not phone_number:
     errors.append("Please add phone number where we can best reach you.")
  email = request.form.get("email")
  if not email:
     errors.append("Please add email where we can best reach you.")
  address = request.form.get("address")
  if not address:
     errors.append("Please add your home address.")
  t_shirt_size = request.form.get("tshirt")
  if not t_shirt_size:
     errors.append("Please add your camper's tshirt size.")
  
  camper = Camper.query.filter_by(name=name).first()
  if camper:
     errors.append("That camper's name already exists!")
  
  if errors:
     return render_template("form.html", errors=errors)
  else:
     new_camper = Camper(name=name, 
                         age=age, 
                         phone_number=phone_number, 
                         email=email, 
                         address=address, 
                         t_shirt_size=t_shirt_size)
     db.session.add(new_camper)
     db.session.commit()
     return render_template("list.html", campers=Camper.query.all())

@app.route("/deleteCamper", methods=["POST"])
def delete_user():
   name = request.form.get("name")
   camper = Camper.query.filter_by(name=name).first()
   if camper:
      db.session.delete(camper)
      db.session.commit()
      return render_template("list.html", campers=Camper.query.all())
   else:
      return render_template("delete.html", errors=["Oops! That camper doesn't exist!"])

# Run the flask server
if __name__ == "__main__":
    app.run()