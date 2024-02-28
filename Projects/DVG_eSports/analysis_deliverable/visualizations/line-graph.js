var margin = {
    top: 20,
    right: 20,
    bottom: 30,
    left: 40
},
width = 960 - margin.left - margin.right,
height = 500 - margin.top - margin.bottom;

var svg = d3.select("#line_graph").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom +50)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

let title = svg.append("text")
    .attr("transform", `translate(400)`)       
    .style("text-anchor", "middle")
    .style("font-size", 15);

function plot(in_game_stat) {
    //svg.select('g').selectAll("dot").remove()

    var x = d3.scaleLinear()
	      .range([0,width]);

	  var y = d3.scaleLinear()
	      .range([height,0]);

	  var xAxis = d3.axisBottom()
	      .scale(x);

	  var yAxis = d3.axisLeft()
	      .scale(y);

    d3.csv("graph_data.csv").then(function(data) {

        var x = d3.scaleLinear()
            .domain([0, 20])
            .range([ 0, width ]);

        // Add Y axis
        var y = d3.scaleLinear()
            .domain([0, 100])
            .range([ height, 0]);
        svg.append("g")
            .call(d3.axisLeft(y));

        // add y axis label
        svg.append("text")
            .attr("text-anchor", "end")
            .attr("transform", "rotate(-90)")
            .attr("y", -30)
            .attr("x", -200)
            .text("Win Rate")    
        
        var lg = calcLinear(data, in_game_stat, "Winrate", d3.min(data, function(d){ return d.x}), d3.min(data, function(d){ return d.x}));

        svg.append("text")
        .attr("text-anchor", "end")
        .attr("x", 500)
        .attr("y", 480)
        .text("Average " + in_game_stat);
        
        svg.append("line")
	        .attr("class", "regression")
	        .attr("x1", x(lg.ptA.x))
	        .attr("y1", y(lg.ptA.y))
	        .attr("x2", x(lg.ptB.x))
	        .attr("y2", y(lg.ptB.y));

        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));


        // hover
        var div = d3.select("body").append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);
        // Add dots
        svg.append('g')
            .selectAll("dot")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", function (d) { return x(parseInt(d[in_game_stat])); } )
            .attr("cy", function (d) { return y(parseInt(d["Winrate"])); } )
            .attr("r", 3.5)
            .style("fill", "#69b3a2")
            .merge(div)
            .on('mouseover', function (d, i) {
                d3.select(this).transition()
                    .duration('100')
                    .attr("r", 7);
                div.transition()
                    .duration(100)
                    .style("opacity", 1);
                div.html(d["name"])
                    .style("left", (d3.event.pageX + 10) + "px")
                    .style("top", (d3.event.pageY - 15) + "px");
           })
           .on('mouseout', function (d, i) {
                d3.select(this).transition()
                    .duration('100')
                    .attr("r", 4);
                div.transition()
                    .duration('100')
                    .style("opacity", 0);
           });
           title.text("In-game Statistics vs Win Rate");

           svg.append("line")
	        .attr("class", "regression")
	        .attr("x1", x(lg.ptA.x))
	        .attr("y1", y(lg.ptA.y))
	        .attr("x2", x(lg.ptB.x))
	        .attr("y2", y(lg.ptB.y));

           div.exit().remove();


        });
    function calcLinear(data, x, y, minX, minY){
        /////////
        //SLOPE//
        /////////
    
        // Let n = the number of data points
        var n = data.length;
        // Get just the points
        var pts = [];
        data.forEach(function(d,i){
            var obj = {};
            obj.x = d[x];
            obj.y = d[y];
            obj.mult = obj.x*obj.y;
            pts.push(obj);
        });
        console.log(pts)

        // Let a equal n times the summation of all x-values multiplied by their corresponding y-values
        // Let b equal the sum of all x-values times the sum of all y-values
        // Let c equal n times the sum of all squared x-values
        // Let d equal the squared sum of all x-values
        var sum = 0;
        var xSum = 0;
        var ySum = 0;
        var sumSq = 0;
        pts.forEach(function(pt){
            sum = sum + pt.mult;
            xSum = xSum + pt.x;
            ySum = ySum + pt.y;
            sumSq = sumSq + (pt.x * pt.x);
        });
        var a = sum * n;
        var b = xSum * ySum;
        var c = sumSq * n;
        var d = xSum * xSum;
    
        // Plug the values that you calculated for a, b, c, and d into the following equation to calculate the slope
        // slope = m = (a - b) / (c - d)
        var m = (a - b) / (c - d);
    
        /////////////
        //INTERCEPT//
        /////////////
    
        // Let e equal the sum of all y-values
        var e = ySum;
    
        // Let f equal the slope times the sum of all x-values
        var f = m * xSum;
    
        // Plug the values you have calculated for e and f into the following equation for the y-intercept
        // y-intercept = b = (e - f) / n
        var b = (e - f) / n;
    
                // Print the equation below the chart
                document.getElementsByClassName("equation")[0].innerHTML = "y = " + m + "x + " + b;
                document.getElementsByClassName("equation")[1].innerHTML = "x = ( y - " + b + " ) / " + m;
    
        // return an object of two points
        // each point is an object with an x and y coordinate
        return {
            ptA : {
            x: minX,
            y: m * minX + b
            },
            ptB : {
            y: minY,
            x: (minY - b) / m
            }
        }
    }
             
}