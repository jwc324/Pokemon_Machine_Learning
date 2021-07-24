from flask import Flask, render_template, request #Question for Limei are these all of the libraries we needed to import?
from flask.wrappers import Request
from joblib import load
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

app = Flask(__name__)
trained_machine_learning_model = load('static/assets/rf.joblib')

@app.route('/')
def home():
    return render_template('predictions.html') 
    ## need to make button to submit, need to make dropdowns for any string values that we want to input in html, 
    ## need to instruct to user the range of numeric inputs possible as the placeholder

# 4/2/40/1/16
@app.route('/generatepredictions', methods=["GET", "POST"])
# @app.route('/generatepredictions/<Quarter>/<Origin>/<Dest>/<NumTicketsOrdered>/<AirlineCompany>')
def predictioninput():
    ## form_data is an empty dictionary to fill in with user inputs
    form_data = {
        "status":"", 
        "species":"",
        "type_2":"",
        "height_m":"",
        "weight_kg":"",
        "ability_1":"",
        "ability_2":"",
        "ability_hidden":"",
        "total_points":"",
        "hp":"",
        "attack":"",
        "defense":"",
        "sp_attack":"",
        "sp_defense":"",
        "speed":"",
        "catch_rate":"",
        "base_friendship":"",
        "base_experience":"",
        "growth_rate":"",
        "egg_type_number":"",
        "egg_type_1":"",
        "egg_type_2":"",
        "percentage_male":"",
        "egg_cycles":"",
        "against_normal":"",
        "against_fire":"",
        "against_water":"",
        "against_electric":"",
        "against_grass":"",
        "against_ice":"",
        "against_fight":"",
        "against_poison":"",
        "against_ground":"",
        "against_flying":"",
        "against_psychic":"",
        "against_bug":"",
        "against_rock":"",
        "against_ghost":"",
        "against_dragon":"",
        "against_dark":"",
        "against_steel":"",
        "against_fairy":""}

if request.method =="POST":
    form_data = request.form

    status = float(form_data["status"]) ## need to change any string values to STRING and need to make dropdowns in html for all string values
    species = float(form_data["species"])
    type_2 = float(form_data["type_2"])
    height_m = float(form_data["height_m"])
    weight_kg = float(form_data["weight_kg"])
    ability_1 = float(form_data["ability_1"])
    ability_2 = float(form_data["ability_2"])
    ability_hidden = float(form_data["ability_hidden"])
    total_points = float(form_data["total_points"])
    hp = float(form_data["hp"])
    attack = float(form_data["attack"])
    defense = float(form_data["defense"])
    sp_attack = float(form_data["sp_attack"])
    sp_defense = float(form_data["sp_defense"])
    speed = float(form_data["speed"])
    catch_rate = float(form_data["catch_rate"])
    base_friendship = float(form_data["base_friendship"])
    base_experience = float(form_data["base_experience"])
    growth_rate = float(form_data["growth_rate"])
    egg_type_number = float(form_data["egg_type_number"])
    egg_type_1 = float(form_data["egg_type_1"])
    egg_type_2 = float(form_data["egg_type_2"])
    percentage_male = float(form_data["percentage_male"])
    egg_cycles = float(form_data["egg_cycles"])
    against_normal = float(form_data["against_normal"])
    against_fire = float(form_data["against_fire"])
    against_water = float(form_data["against_water"])
    against_electric = float(form_data["against_electric"])
    against_grass = float(form_data["against_grass"])
    against_ice = float(form_data["against_ice"])
    against_fight = float(form_data["against_fight"])
    against_poison = float(form_data["against_poison"])
    against_ground = float(form_data["against_ground"])
    against_flying = float(form_data["against_flying"])
    against_psychic = float(form_data["against_psychic"])
    against_bug = float(form_data["against_bug"])
    against_rock = float(form_data["against_rock"])
    against_ghost = float(form_data["against_ghost"])
    against_dragon = float(form_data["against_dragon"])
    against_dark = float(form_data["against_dark"])
    against_steel = float(form_data["against_steel"])
    against_fairy = float(form_data["against_fairy"])

    return render_template('predictions.html', PokemonPrimaryType='RETRY') 
    ## Need to organize all of the above variables into an ENCODED array
        ## need to take inputs and encode them, using an ordinal encoder... sample code below:
        #   oe = OrdinalEncoder()
        #x_enc = oe.fit_transform(x)
    ## Need to organize array into specific order of the variables listed above   
    ## See screenshot in Slack of Brian's TA's organization example 

    # Jen's TA data organization example
        # predict(Quarter=4, Origin=2, Dest=16, NumTicketsOrdered=1, AirlineCompany=1):
        # try:
        #     df = pd.DataFrame({
        #         'Quarter': [int(Quarter)],
        #         'Origin': [int(Origin)],
        #         'Dest': [int(Dest)],
        #         'Miles': [miles_dict[f"{origin_dict[int(Origin)]}>{dest_dict[int(Dest)]}"]],
        #         'NumTicketsOrdered': [int(NumTicketsOrdered)],
        #         'AirlineCompany': [int(AirlineCompany)]
        #     })

        #     PricePerTicket = str(trained_machine_learning_model.predict(df)[0])[0:6]
        #     PricePerTicket = f"${PricePerTicket}"

        #     return render_template('predictions.html', pricePerTicket=PricePerTicket)

    # except:
    # return render_template('predictions.html', PokemonPrimaryType='RETRY') 
        # Need to make sure html file can output {{PokemonPrimaryType}}

if __name__ == '__main__':
    app.run()