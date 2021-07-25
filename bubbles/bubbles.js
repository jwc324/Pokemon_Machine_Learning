(function() {
    var width = 1400,
        height = 1000;
    console.log("hello");

    var svg = d3.select("#chart")
        .append("svg")
        .attr("height", height)
        .attr("width", width)
        .append("g")
        .attr("transform", "translate(0,0)");

    // from https://www.youtube.com/watch?v=lPr60pexvEM&t=0s //

    var radiusScale = d3.scaleSqrt().domain([1, 255]).range([0.5, 25])

    var forceXfriendly = d3.forceX(function(d) {
        if(d.base_friendship_group === 'nicest') {
            return 200
        } else {
            return 850 
        }
        }).strength(0.2)
    
    var forceXreturn = d3.forceX(width / 2).strength(0.2)

    var forceCollide = d3.forceCollide(function(d)   {   
        return radiusScale(d.hp) + 2;
        /*.force("collide", d3.forceCollide("r", 10))*/
    })

    // the simulation is a collection of forces
    // about where we want our circles to go
    // and how we want our circles to interact
    // STEP ONE: get them to the middle
    // STEP TWO: don't have them collide - radius of the area of
    // the collision we want to avoid

    var simulation = d3.forceSimulation()
        .force("x", forceXreturn)
        .force("y", d3.forceY(height / 2).strength(0.2))
        .force("collide", forceCollide)


    //read in data
    d3.queue()
        .defer(d3.csv, "test.csv")
        .await(ready)

    function ready (error, datapoints) {

        typesToColors = {
            Bug: "darkkhaki",
            Dark: "dimgrey",
            Dragon: "darkcyan",
            Electric: "gold",
            Fairy: "orchid",
            Fighting: "peru",
            Fire: "red",
            Flying: "skyblue",
            Ghost: "purple",
            Grass: "green",
            Ground: "brown",
            Ice: "lightblue",
            Normal: "linen",
            Poison: "rebeccapurple",
            Psychic: "slateblue",
            Rock: "saddlebrown",
            Steel: "silver",
            Water: "blue"
        }
     
        // create a tooltip
        var Tooltip = d3.select("#chart")
        .append("div")
        .attr("class", "tooltip")
        .style("visibility", "hidden")
        .style("poistion", "absolute")
        .style("z-index", "10")
        .style("height", "100px")
        //.style("background-color", "white")
        //.style("border", "solid")
        //.style("border-width", "2px")
        //.style("border-radius", "5px")
        //.style("padding", "5px")

        // Three function that change the tooltip when user hover / move / leave a cell
        var mouseover = function(d) {
            Tooltip
                .transition()
                .duration(200)
                .style("visibility", "visible")
            Tooltip
                .text("name:" + d.name)
                .style("left", (d3.select(this).attr("cx") + "px"))
                .style("top", (d3.select(this).attr("cy") + "px"))
                //.style('left', (d3.event.pageX) + 'px')
                //.style('top', (d3.event.pageY / 1.5) + 'px')
        }
        console.log("!!!")

        /*var mousemove = function(d) {
            Tooltip.html(d.name + "<br>")
                .style("opacity", 1)
                .style("left", (d3.select(this).attr("cx") + "px"))
                .style("top", (d3.select(this).attr("cy") + "px"))
        }
            console.log("!!!")*/

        var mouseleave = function() {
            Tooltip.transition()
                .duration(200)
                .style("visibility", "hidden")
        }
            console.log("!!!")

        // create circle for every datapoint
        var circles = svg.selectAll(".poke_type")
            .data(datapoints)
            .enter()
            .append("circle")
                .attr("class", "poke_type")
                /*.attr("r", 10)*/
                .attr("r", function(d) {
                    return radiusScale(d.hp)
                })
                .attr("fill", function(d) {
                    return typesToColors[d.type_1]
                })
            //trigger tooltips
            .on("mouseover", mouseover)
            //.on("mousemove", mousemove)
            .on("mouseleave", mouseleave)
            .on('click', function(d) {
                console.log(d)
            })
            console.log("!!!")




        d3.select("#friendly").on('click', function() {
            simulation
            .force("x", forceXfriendly)
            .alphaTarget(0.2)
            .restart()
        })

        d3.select('#return').on('click', function() {
            simulation
                .force("x", forceXreturn)
                .alphaTarget(0.01)
                .restart()
        })

        // for each datapoint, look back at the forces
        simulation.nodes(datapoints)
            .on('tick', ticked)

        // and reposition circle
        function ticked() {
            circles
                .attr("cx", function(d) {
                    return d.x
                })
                .attr("cy", function(d) {
                    return d.y 
                })
        }
    }
        
})();