// this js file contains code for diversity bubble chart

// bubble colors
var colors = ["#1f77b4","#aec7e8","#ff7f0e","#ffbb78","#2ca02c","#98df8a",
    "#d62728","#ff9896","#9467bd","#c5b0d5","#8c564b","#c49c94","#e377c2",
    "#f7b6d2","#7f7f7f","#c7c7c7","#bcbd22","#dbdb8d","#17becf","#9edae5"];

// color based on ethnicity-gender combo
function fill_color(ethn, gender) {
    if (gender == 'male') {
        if (ethn == 'white') {
            return colors[0];
        } else if (ethn == 'hispanic') {
            return colors[2];
        } else if (ethn == 'black') {
            return colors[4];
        } else if (ethn == 'asian') {
            return colors[6];
        } else if (ethn == 'aian') {
            return colors[8];
        } else if (ethn == 'nhpi') {
            return colors[10];
        } else if (ethn == 'biracial') {
            return colors[12];
        } else if (ethn == 'unknown') {
            return colors[14];
        }
    } else if (gender == 'female') {
        if (ethn == 'white') {
            return colors[1];
        } else if (ethn == 'hispanic') {
            return colors[3];
        } else if (ethn == 'black') {
            return colors[5];
        } else if (ethn == 'asian') {
            return colors[7];
        } else if (ethn == 'aian') {
            return colors[9];
        } else if (ethn == 'nhpi') {
            return colors[11];
        } else if (ethn == 'biracial') {
            return colors[13];
        } else if (ethn == 'unknown') {
            return colors[15];
        }
    } else {
        return "#FFF"
    }
};

// make tooltip for bubble chart
function bubbleTooltip() {
    var bubbletip = "<p>Bubbles are colored by ethnicity " +
        "and gender:</p><svg height='300' width='350'><g><text x='7' y='20' " +
        "fill='white'>F</text><text x='35' y='20' fill='white'>M</text>";
    var ethnicityList = _(ethnicities).pairs().sortBy(function(n) { return n[1];}).value();
    // add circles and text for each ethnicity
    for(i = 0; i < ethnicityList.length; i++) {
        var y = 40 + 35 * i;
        var col = fill_color(ethnicityList[i][0], 'female');
        bubbletip += "<circle cx='12' cy='" + y + "' r='10' fill='" + col + "'/>";
        col = fill_color(ethnicityList[i][0], 'male');
        bubbletip += "<circle cx='40' cy='" + y + "' r='10' fill='" + col + "'/>";
        bubbletip += "<text x='60' y='" + y + "' fill='white'>" + ethnicityList[i][1] + "</text>";
    }
    bubbletip += '</g></svg>';
    return bubbletip;
}


// render the bubble chart
function buildbubblechart(data) {

    // reset chart and buttons
    $(".bubblesvgcontainer svg").remove();
    $(".bubblecontainer .btn").removeClass("active");
    $("#all").addClass("active");

    // set dimensions
    var width = modalWidth * .62;
    var height = modalHeight * .53;
    var padding = 0;

    // get scale for circles based on max value
    var max_amount = d3.max(data, function(d) { 
        return parseInt(d.degrees, 10); } );
    var radius_scale = d3.scale.sqrt()
        .domain([0, max_amount])
        .range([2, 90]);

    // set radius and other attributes
    _.each(data, function(elem) {
        elem.r = 1;
        elem.radius = radius_scale(elem.degrees)*.8;
        elem.all = 'all';
        elem.x = _.random(0, width);
        elem.y = _.random(0, height);
    });

    var maxRadius = d3.max(_.pluck(data, 'radius'));

    var bubblecontainer = d3.select(".bubblesvgcontainer").append("svg")
        .attr("width", width)
        .attr("height", height);
    
    // draw border around chart container
    var borderPath = bubblecontainer.append("rect")
        .attr("x", 1)
        .attr("y", 1)
        .attr("height", height-2)
        .attr("width", width-2)
        .style("stroke", "#a9a9a9")
        .style("fill", "none")
        .style("stroke-width", 1);

    // bind data to nodes in chart
    var nodes = bubblecontainer.selectAll("bubble_circle")
        .data(data, function(d) {
            return d.ethnicity + d.gender + d.awlevel + d.cip_family;})
    ;



    // create nodes
    nodes.enter()
        .append("circle")
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; })
        .attr("r", 1)
        .style("fill", function(d) { 
            return fill_color(d.ethnicity, d.gender);})
        .style("stroke", function(d){
            return d3.rgb(fill_color(d.ethnicity, d.gender)).darker().toString();})
	    .on("mouseover", function(d, i) {
            var tipHtml = "Degree:  " + d.awlevel + 
                 "<br/>Major:  " + d.cip_family +
                 "<br/>Ethnicity:  " + ethnicities[d.ethnicity] +
                 "<br/>Gender:  " + genders[d.gender] +
                 "<br/>Count:  " + d3.format(",")(+d.degrees);
            showTip(tipHtml);
        })
        .on('mouseout', function() {
            hideTip();
        });

    // create force layout
    var force = d3.layout.force();

    // draw the graph
    function draw (varname) {
        var foci = find_foci(varname);
        force.on("tick", tick(foci, varname));
        labels(foci);
        force.start();
    }

    // find center point for each category
    function find_foci(centerType) {
        if(centerType == "all") {
            var degrees = _.sum(data, function(e) { return e.degrees; });
            return {"all": {name:"All Degrees", x: width/2, y: height/2, dx: width, degrees: degrees}};
        } else {
            // group by selected type
            var groups = _.groupBy(data, centerType);

            // format data as nodes of "root" with size equal to total # of degrees in the group
            var nodeData = _.map(groups, function(d, k) { return {"name": k, "degrees": _.sum(d, function(e) { return e.degrees; })}; });
            var root = {"name": "all", "children": nodeData};

            // use treemap layout to partition container into square "nodes"
            var treemap = d3.layout.treemap()
                .size([width, height])
                .value(function(d) { return 1; })
                .sort(function(a,b) {
                    var bn = formatCategory(a.name, centerType).toLowerCase();
                    var an = formatCategory(b.name, centerType).toLowerCase();
                    return an < bn ? -1 : an > bn ? 1 : an >= bn ? 0 : NaN;
                });
            var treemapNodes = treemap.nodes(root);
            treemapNodes.shift(); // eliminate "root" node

            // calculate center of each node and format object
            var treemapGroups = {};
            _.forEach(treemapNodes, function(n) {
                // reformat names
                var cat_name = formatCategory(n.name, centerType);
                // calculate center of each node
                var x = n.x + n.dx/2;
                var y = n.y + n.dy/2;
                treemapGroups[n.name] = {name: cat_name, x: x, y: y, dx: n.dx, degrees: n.degrees};
            });

            return treemapGroups;
        }
    }

    // move the nodes a little closer to the foci with each tick
    function tick (foci, varname) {
        return function (e) {
            for (var i = 0; i < data.length; i++) {
                var o = data[i];
                var f = foci[o[varname]];
                o.y += (f.y - o.y) * e.alpha;
                o.x += (f.x - o.x) * e.alpha;
                o.r += (o.radius - o.r) * e.alpha;
            }
            nodes
                .each(collide(.15))
                .attr("cx", function (d) { return d.x; })
                .attr("cy", function (d) { return d.y; })
                .attr("r", function (d) { return d.r; });
        }
    }

    // prevent overlapping nodes
    function collide(alpha) {
        var quadtree = d3.geom.quadtree(data);
        return function(d) {
            var r = d.radius + maxRadius + padding,
                nx1 = d.x - r,
                nx2 = d.x + r,
                ny1 = d.y - r,
                ny2 = d.y + r;
            quadtree.visit(function(quad, x1, y1, x2, y2) {
                if (quad.point && (quad.point !== d)) {
                    var x = d.x - quad.point.x,
                y = d.y - quad.point.y,
                l = Math.sqrt(x * x + y * y),
                r = d.radius + quad.point.radius + padding;
            if (l < r) {
                l = (l - r) / l * alpha;
                d.x -= x *= l;
                d.y -= y *= l;
                quad.point.x += x;
                quad.point.y += y;
            }
                }
                return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
            });
        };
    }

    // create labels for each category/foci
    function labels (foci) {
        bubblecontainer.selectAll(".label").remove();

        bubblecontainer.selectAll(".label")
            .data(_.toArray(foci)).enter().append("text")
            .attr("class", "label")
            .text(function (d) { return d.name + " " + d3.format(",.0f")(d.degrees) + " degrees"})
            .attr("transform", function (d) {
                return "translate(" + (d.x) + "," 
                + (d.y - d.dx/10) + ")";
            })
            .attr("text-anchor", "middle")
            .call(wrap);
    }

    // draw all degrees
    draw('all');

    // destroy previous click events
    $( ".bubblecontainer .btn" ).unbind();

    // redraw graph on click
    $( ".bubblecontainer .btn" ).click(function() {
        draw(this.id);
    });

};

// format ethnicity-gender labels
function formatCategory(cat, type) {
    if(type == 'gender') {
        return genders[cat];
    } else if(type == 'ethnicity') {
        return ethnicities[cat];
    } else {
        return cat;
    }
}

// wrap svg text
function wrap(text) {
    text.each(function() {
        var text = d3.select(this),
            words = text.text().split(/\s+/).reverse(),
            word,
            width = text.data()[0].dx,
            line = [],
            lineNumber = 0,
            lineHeight = 1, // ems
            y = 0,
            dy = 0,
            tspan = text.text(null).append("tspan").attr("x", 0).attr("y", y).attr("dy", "0em");
        while (word = words.pop()) {
            line.push(word);
            tspan.text(line.join(" "));
            if (tspan.node().getComputedTextLength() > width || !isNaN(word)) { // new line if too long or if word is a number
                line.pop();
                tspan.text(line.join(" "));
                line = [word];
                tspan = text.append("tspan").attr("x", 0).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
            }
        }
    });
}
