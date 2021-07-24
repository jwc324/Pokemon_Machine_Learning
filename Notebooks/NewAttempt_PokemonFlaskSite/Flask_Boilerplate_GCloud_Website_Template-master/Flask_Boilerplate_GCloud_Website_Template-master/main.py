
from flask import Flask, render_template, redirect, request
from joblib import load
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

app = Flask(__name__)
trained_machine_learning_model = load('static/rf.joblib')
pokemontypeprediction = {"prediction":""}

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pokemontypeprediction = pokemontypeprediction["prediction"])


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/generateprediction', methods=["POST"])
def generateprediction():
    form_data = request.form

    status = form_data["status"] ## need to change any string values to STRING and need to make dropdowns in html for all string values
    species = form_data["species"]
    type_2 = form_data["type_2"]
    height_m = form_data["height_m"]
    weight_kg = form_data["weight_kg"]
    ability_1 = form_data["ability_1"]
    ability_2 = form_data["ability_2"]
    ability_hidden = form_data["ability_hidden"]
    total_points = form_data["total_points"]
    hp = form_data["hp"]
    attack = form_data["attack"]
    defense = form_data["defense"]
    sp_attack = form_data["sp_attack"]
    sp_defense = form_data["sp_defense"]
    speed = form_data["speed"]
    catch_rate = form_data["catch_rate"]
    base_friendship = form_data["base_friendship"]
    base_experience = form_data["base_experience"]
    growth_rate = form_data["growth_rate"]
    egg_type_number = form_data["egg_type_number"]
    egg_type_1 = form_data["egg_type_1"]
    egg_type_2 = form_data["egg_type_2"]
    percentage_male = form_data["percentage_male"]
    egg_cycles = form_data["egg_cycles"]
    against_normal = form_data["against_normal"]
    against_fire = form_data["against_fire"]
    against_water = form_data["against_water"]
    against_electric = form_data["against_electric"]
    against_grass = form_data["against_grass"]
    against_ice = form_data["against_ice"]
    against_fight = form_data["against_fight"]
    against_poison = form_data["against_poison"]
    against_ground = form_data["against_ground"]
    against_flying = form_data["against_flying"]
    against_psychic = form_data["against_psychic"]
    against_bug = form_data["against_bug"]
    against_rock = form_data["against_rock"]
    against_ghost = form_data["against_ghost"]
    against_dragon = form_data["against_dragon"]
    against_dark = form_data["against_dark"]
    against_steel = form_data["against_steel"]
    against_fairy = form_data["against_fairy"]
    
    pokemontypeprediction["prediction"] = "PLACEHOLDERFORTYPE"
    
    return redirect("/")

    ## look up how to get a map of the encoder and save that as a dictionary and export as a json

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)