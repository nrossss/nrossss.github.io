from flask import Flask, render_template, abort
from flask import request

app = Flask(__name__)
users = {
    "archie.andrews@email.com": "football4life",
    "veronica.lodge@email.com": "fashiondiva"
}
Pets = [
    {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at "
                                                        "Paws Rescue Center. I love squeaky toys and cuddles."},
    {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to "
                                                        "dress up in bow ties."},
    {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
    {"id": 5, "name": "Trapecio", "age": "5 years", "bio": "Probably napping."},
    {"id": 6, "name": "Polenta", "age": "6 years", "bio": "Probably napping."}
]

@app.route('/')
def home():
    return render_template('homepage.html', Pets = Pets)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get ("email")
        passwd = request.form.get ("password")

        if email in users and users[email] == passwd:
            return render_template ("login.html", message="Successfully Logged In")
        else:
            return render_template ("login.html", message="Incorrect Email or Password")
    return render_template ('login.html')


@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    pet = next((pet for pet in Pets if pet["id"] == pet_id), None)
    if pet is None:
        abort(404, description="Pet not found")
    return render_template("details.html", pet = pet)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)


