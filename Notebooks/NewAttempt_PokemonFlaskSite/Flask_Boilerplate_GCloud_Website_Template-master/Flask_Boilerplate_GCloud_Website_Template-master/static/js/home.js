var pokemonattributes = [
    "status",
    "species",
    "type_2",
    "height_m",
    "weight_kg",
    "ability_1",
    "ability_2",
    "ability_hidden",
    "total_points",
    "hp",
    "attack",
    "defense",
    "sp_attack",
    "sp_defense",
    "speed",
    "catch_rate",
    "base_friendship",
    "base_experience",
    "growth_rate",
    "egg_type_number",
    "egg_type_1",
    "egg_type_2",
    "percentage_male",
    "egg_cycles",
    "against_normal",
    "against_fire",
    "against_water",
    "against_electric",
    "against_grass",
    "against_ice",
    "against_fight",
    "against_poison",
    "against_ground",
    "against_flying",
    "against_psychic",
    "against_bug",
    "against_rock",
    "against_ghost",
    "against_dragon",
    "against_dark",
    "against_steel",
    "against_fairy"
]

// var predictionsform = d3.select("#predictions-form")
var pokemoninputhtml = "";

pokemonattributes.forEach((attribute)=>{
    pokemoninputhtml+=` <label for="fname">${attribute}</label><br>
    <input type="text" id="${attribute}" name="${attribute}" value=""><br>`
})
pokemoninputhtml+=`<input type="submit" value="Submit">`
d3.select("#predictions-form").html(pokemoninputhtml)