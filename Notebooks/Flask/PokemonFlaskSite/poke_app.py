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



    form_data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    form_data[0][0] = status
    form_data[0][1] = species
    form_data[0][2] = type_2
    form_data[0][3] = height_m
    form_data[0][4] = weight_kg
    form_data[0][5] = ability_1
    form_data[0][6] = ability_2
    form_data[0][7] = ability_hidden
    form_data[0][8] = total_points
    form_data[0][9] = hp
    form_data[0][10] = attack
    form_data[0][11] = defense
    form_data[0][12] = sp_attack
    form_data[0][13] = sp_defense
    form_data[0][14] = speed
    form_data[0][15] = catch_rate
    form_data[0][16] = base_friendship
    form_data[0][17] = base_experience
    form_data[0][18] = growth_rate
    form_data[0][19] = egg_type_number
    form_data[0][20] = egg_type_1
    form_data[0][21] = egg_type_2
    form_data[0][22] = percentage_male
    form_data[0][23] = egg_cycles
    form_data[0][24] = against_normal
    form_data[0][25] = against_fire
    form_data[0][26] = against_water
    form_data[0][27] = against_electric
    form_data[0][28] = against_grass
    form_data[0][29] = against_ice
    form_data[0][30] = against_fight
    form_data[0][31] = against_poison
    form_data[0][32] = against_ground
    form_data[0][33] = against_flying
    form_data[0][34] = against_psychic
    form_data[0][35] = against_bug
    form_data[0][36] = against_rock
    form_data[0][37] = against_ghost
    form_data[0][38] = against_dragon
    form_data[0][39] = against_dark
    form_data[0][40] = against_steel
    form_data[0][41] = against_fairy

    form_array = np.asarray(form_data, dtype=np.float32) 


    # Encode all data

    oe = OrdinalEncoder()
    x_enc = oe.fit_transform(x)

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x_enc,
        y,  random_state=42)
    print(x_train.shape)
    print(x_test.shape)
    print(y_train.shape)
    print(y_test.shape)



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

    except:
        return render_template('predictions.html', PokemonPrimaryType='RETRY') 
        # Need to make sure html file can output {{PokemonPrimaryType}}

if __name__ == '__main__':
    app.run()

<body>
    <div class="panel panel-default">
        <div class="panel-heading">Filter Search</div>
        <div class="panel-body">
            <div class="form-group">
                <ul class="list-group" id="filters">
                    <li class="filter list-group-item">
                        <label for="date">Enter a Date</label>
                        <input class="form-control" id="datetime" type="text" placeholder="1/11/2011">
                    </li>
                    <li class="filter list-group-item">
                        <label for="city">Enter a City</label>
                        <input class="form-control" id="city" type="text" placeholder="roswell">
                    </li>
                    <li class="filter list-group-item">
                        <label for="state">Enter a State</label>
                        <input class="form-control" id="state" type="text" placeholder="ca">
                    </li>
                    <li class="filter list-group-item">
                        <label for="country">Enter a Country</label>
                        <input class="form-control" id="country" type="text" placeholder="us">
                    </li>
                    <li class="filter list-group-item">
                        <label for="shape">Select a Shape</label>
                        <input class="form-control" id="shape" type="text" placeholder="circle">
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <h1>Price Per Ticket</h1>
    <h1>{{pricePerTicket}}</h1>
</body>