// This file contains all custom js code for the sourcing tool dashboard
// except for the diversity bubble chart (which is in bubblechart.js)

var showAffiliations = false;
var selectedAffiliation = null;
var affiliationLabels = { "onsite": "On-Campus", "offsite": "Virtual", "none": "No Affiliation" };

// get results data for schools given reqeust criteria
function schoolResults(urlQuery) {
	$('#load').show()
    $.ajax({
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        type: "GET",
        url: '/universities/universities/' + urlQuery,
        success: function (responseData) {
        	$('#load').hide()
            // check if list or detailed results requested
            if (!isNaN(parseInt(urlQuery))) {
				$('#mapdashboard').modal('show');
				d3.selectAll(".modal-dialog svg").remove();
				getModalSize();          
                $('.titlecontainer').text(responseData.school_name);
                var rank = responseData.rank;
                if (rank == null) {
                	rank = "N/A";
                }
                $('.textcontainer p:eq(0)').text('U.S. News Rank: ' + rank);
                var webaddress = responseData.main_web;
                 if (webaddress == null) {
                	$('.textcontainer p:eq(1)').html("Website unknown");
                } else {
                	$('.textcontainer p:eq(1)').html("<a href='http://" + webaddress + "' target='_blank'>" + webaddress + "</a>");
                }
				appFlowChart(responseData.app_flow_counts);
				actScores(responseData.instchars);
				satScores(responseData.instchars);
				gradRatesPie(responseData.gradrate);
				acceptRatePie(responseData.instchars.accept_rate);
                buildbubblechart(responseData.awardsdetailscounts);

            } else {
                // drawMarkers(responseData.results);
                // populateTable(responseData.results);
                drawMarkers(responseData);
                populateTable(responseData);
            }
        },
        error: function (jqXHR,textStatus,errorThrown) {

        	$('#load').hide()

            //log error details in console
            if(window.console !== undefined) {
                alert("Unable to update data!");
            }
        }
    });
}

// capitalize first letter of each word
String.prototype.toProperCase = function () {
    return this.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
};

// initialize map

var southWest = L.latLng(24.2, -125),
    northEast = L.latLng(49.5, -66.5),
    maxBounds = L.latLngBounds(southWest, northEast);

var bLayer = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        maxZoom: 18,
        id: 'dberenbaum.mpoj67fd',
        accessToken: 'pk.eyJ1IjoiZGJlcmVuYmF1bSIsImEiOiI1NjhkODU2MDU4NTlkMjU1MjFmMTQ1OWUzMDhjNDE4ZSJ9.d3teGcz-PIFv8IEzOcT1oQ'
});

var map = L.map('map', {
    'layers': bLayer,
    'maxBounds': maxBounds,
    'maxZoom': 20,
    'minZoom': 4
}).fitBounds(maxBounds);

//D3 bubbles on leafleft map

map._initPathRoot()

var svg = d3.select("#map").select("svg"),
    g = svg.append("g");

var tip = d3.tip()
    .attr('class','d3-tip');

svg.call(tip);

// replacement functions for d3-tip to show and hide tips
function showTip(tipHtml) {
    d3.select(".d3-tip")
      .style("left", d3.event.pageX + "px")
      .style("top", d3.event.pageY + "px")
      .style("opacity", 1)
      .html(tipHtml);
}

function hideTip() {
    d3.selectAll(".d3-tip")
      .style("opacity", 0); 
}

// redraw map markers based on new data
function drawMarkers(schools){

    // make size relative to max
    // var maxHires = d3.max(schools, function(d) { return d.potential_hires; });
    // var minHires = d3.min(schools, function(d) { return d.potential_hires; });
    var maxDegrees = d3.max(schools, function(d) { return d.degree_count; });
    var minDegrees = d3.min(schools, function(d) { return d.degree_count; });

    var radius_scale = d3.scale
        .linear()
        // .domain([minHires, maxHires])
        .domain([minDegrees, maxDegrees])
        .range([5, 15]);

    // update data for markers
    var feature = g.selectAll("circle")
      .data(schools, function(d) { return d.unitid; });

    // add new markers
    feature.enter().append("circle")
      .attr("class", "school-circle")
      .style("fill", "orange")
      .style("fill-opacity",0.7)
      .attr("r", function(d){
          // return radius_scale(d.potential_hires);
          return radius_scale(d.degree_count);
      })
      .on("click", function(d){
		getSchoolDetails(d.unitid);
      }).on("mouseover", function(d) {
            // var tipHtml = d.school_name + "</br>Hiring Score: " + d.hiring_score; 
            var tipHtml = d.school_name + "</br>Degree Matches: " + d3.format(",.0f")(d.degree_count); 
            showTip(tipHtml);
            $('#schoolsTable').DataTable()
              .search(d.school_name, false, false, false)
              .draw();
      }).on("mouseout", function(d) {
            hideTip();
            $('#schoolsTable').DataTable()
              .search('', false, true, true)
              .draw();
      });

    // transition existing marker sizes
    feature.transition()
      .duration(500)
      .attr("r",function(d){
        // return radius_scale(d.potential_hires);
        return radius_scale(d.degree_count);
    });

    // remove old markers
    feature.exit().remove();

    // redraw on zoom/pan
    map.on("viewreset", update);

    update();
    showScoreLegend();

    // update map coords of markers
    function update() {
        feature.attr("transform", 
        function(d) { 
            var coords = latlong(d);
            return "translate("+ 
                map.latLngToLayerPoint(coords).x +","+ 
                map.latLngToLayerPoint(coords).y +")";
            }
        )
    }

    // show relative size of circles
    function showScoreLegend() {
        d3.selectAll(".map-legend").remove();

        var legendSvg = d3.select("#map-legend").append("svg")
          .attr("class", "map-legend");

        var legendG = legendSvg.append("g")
          .attr("class", "legend-g")
          .attr('transform', 'translate(20,0)');

        legendG.append("rect")
            .attr("height", 140)
            .attr("width", 150)
            .style("stroke", "#606060")
            .style("fill", "none")
            .style("stroke-width", 1);

        legendG.append('text')
          .attr("dy", 20)
          .attr("dx", 5)
          // .text("Hiring Score")
          .text("Degree Matches")
          .style("font-size", "20px")
          .style("fill", "#606060");

        // legendG.append('text')
        //   .attr("dy", 40)
        //   .attr("dx", 5)
        //   .text("(out of 100)")
        //   .style("font-size", "20px")
        //   .style("fill", "#606060");

        var legend = legendG.selectAll('.legend')
          // .data([minHires,(maxHires+minHires)/2,maxHires])
          .data([minDegrees,(maxDegrees+minDegrees)/2,maxDegrees])
          .enter()
          .append('g')
          .attr('transform', function(d, i) {
            var yOffset =  120 - i * 30;
            return 'translate(20,' + yOffset  + ')';
          });

        legend.append('circle')
          .style("fill", "orange")
          .style("fill-opacity",0.7)
          .attr("r", function(d){
              return radius_scale(d);
          });

        // var score = d3.scale.linear()
        //   .domain([0,maxHires])
        //   .rangeRound([0,100]);

        legend.append('text')
          .attr('dx', 20)
          // .text(function(d) { return score(d); })
          .text(function(d) { return d3.format(",.0f")(d); })
          .style("fill", "#606060");

        if(showAffiliations) {
            toggleAffiliations();
        }
    }
}   

// create leaflet LatLng object from coords
function latlong(d) {
    return new L.LatLng(d.latitude,d.longitude);
}

// toggle whether to show affiliations
function toggleAffiliations() {
    showAffiliations = !showAffiliations;

    // show affiliation colors and legend  
    if(showAffiliations) {
        // change colors
        d3.selectAll("#map circle")
          .transition()
          .duration(500)
          .style("fill", function(d) {
                return affiliationColor(d.affiliation);
          });

        // change color of score legend
        d3.selectAll("#map-legend circle")
          .transition()
          .duration(500)
          .style("fill", function(d) {
                return affiliationColor("none");
          });

        showAffiliationsLegend();

    // hide affiliation colors and legend
    } else {

        // change colors
        d3.selectAll("#map circle").transition()
          .duration(500)
          .style("fill", "orange")
          .style("fill-opacity", 0.7);

        // change color of score legend
        d3.selectAll("#map-legend circle")
          .transition()
          .duration(500)
          .style("fill", "orange");

        // remove legend
        d3.select("#afflegend svg").remove();

        // reset selected affiliation
        selectedAffiliation = null;
    }
}

// show legend
function showAffiliationsLegend() {
    var affiliations = ["onsite", "offsite", "none"];
    var affHeight = $(".showaffbtn").height();
    var affWidth = $(".map-container").width() - 
            $("#affbutton").width() - 50;
    var affRadius = 10;

    // draw svg container
    var affSvg = d3.select("#afflegend").append("svg")
          .attr("width", affWidth + "px")
          .attr("height", affHeight + "px");

    // set position ranges for each affiliation type
    var affScale = d3.scale.ordinal()
      .domain(affiliations)
      .rangeRoundBands([0, affWidth], 0.1, 0.1);

    // create 3 groups for onsite, offsite, and none
    var affGroups = affSvg.selectAll("g")
        .data(affiliations)
      .enter().append("g")
        .attr("transform", function(d) { 
            return "translate(" + affScale(d) + "," + affHeight/2 + ")";
        })
        .on("mouseover", function(d) {
            var tipHtml = "Click to highlight schools with this affiliation type."
            showTip(tipHtml);
        })
        .on("mouseout", function(d) {
            hideTip();
        })
        .on("click", function(d) {
            if(selectedAffiliation == d) {
                // if already selected, return all fill opacities to normal
                selectedAffiliation = null;
                affGroups.selectAll("circle")
                  .transition()
                  .duration(500)
                  .style("fill-opacity", function(e) {
                      return 0.7;
                  });
                d3.selectAll(".school-circle")
                  .transition()
                  .duration(500)
                  .style("fill-opacity", function(e) {
                      return 0.7;
                  });
            } else {
                // highlight associated circles
                selectedAffiliation = d;
                affGroups.selectAll("circle")
                  .transition()
                  .duration(500)
                  .style("fill-opacity", function(e) {
                      if(d == e) {
                          return 0.7;
                      } else {
                          return 0.1;
                      }
                  });
                d3.selectAll(".school-circle")
                  .transition()
                  .duration(500)
                  .style("fill-opacity", function(e) {
                      if(e.affiliation == d) {
                          return 0.7;
                      } else {
                          return 0.1;
                      }
                  });
            }
        });

    // draw circles
    affGroups.append("circle")
      .attr("r", affRadius)
      .style("fill-opacity",0.7)
      .attr("fill", affiliationColor);

    // add text
    affGroups.append("text")
      .attr("dx", affRadius*2)
      .attr("dy", affRadius/2)
      .text(function(d) {
            return affiliationLabels[d];
      });

}

// color by affiliation
function affiliationColor(affiliation) {
  if(affiliation == "onsite") {
      return "#A06CD5";
  } else if(affiliation == "offsite") {
      return "#5386E4";
  } else {
      return "#64ED6D";
  }
}

var cssAxis = ({"stroke": "#f7f7f7", 
 				"fill": "none", 
 				"stroke-width": "0.5px",
 				"font-weight": "lighter"})

var cssAxisNumbers = ({"fill": "#f7f7f7", 
		 				"font-size": "0.8em",
		 				"font-weight": "lighter"})
var modalWidth;
var modalHeight;

function getModalSize() {
	modalWidth = $("#mapdashboard").width();
	modalHeight = $("#mapdashboard").height();
}

//Start of Layered Bar Chart for Applicant Flow

var appColors = ["#08306b","#2171b5","#9ecae1", "#f7fbff"];
// var appColors = ["#08519c","#4292c6","#9ecae1","#deebf7"];
function appFlowChart(appData){
	$(".applicantcontainer svg").remove();

	var appData = {
			"applicants":[appData.app_off,appData.app_on],
			"eligible":[appData.qual_off,appData.qual_on],
			"qualified":[appData.bqual_off,appData.bqual_on],
			"hired":[appData.hire_off,appData.hire_on]
		};

	var appWidth = modalWidth * .6 ;
	var appHeight = modalHeight * .25;

	var outerappSVG = d3.select(".applicantcontainer")
		.append("svg")
		.attr("width", appWidth)
		.attr("height", appHeight);

	var appSVG = d3.select(".applicantcontainer svg")
		.append("g")
		.attr("width", appWidth)
		.attr("height", appHeight)
		.attr("transform", "translate(" + appWidth * .1 + "," 
			   + appHeight * .1 + ")");

	var categories= ["Virtual","On-Campus"];

	var baseHeight = appHeight * .25;

	var x = d3.scale.linear()
	    .domain([0,appData.applicants[1]])
	    .range([0, appWidth * .8 ])
        .nice();

	var xAxis = d3.svg.axis()
	    .scale(x)
	    .orient("bottom");

    var chartHeight = appHeight * 0.6;

	var y = d3.scale.linear()
		.domain([-0.5,1.5])
		.range([0, chartHeight]);

	var yAxis = d3.svg.axis()
		.orient('left')
		.scale(y)
		.tickSize(2)
		.tickFormat(function(d,i){ return categories[i]; })
		.tickValues([0,1]);

	var appBars = appSVG.selectAll("rect")
	    .data(appData.applicants)
	    .enter()
	    .append("rect")
	    .attr('class', 'apps')
	    .attr("width", function (d) {
            return x(d);
        })
	    .attr("height", baseHeight)
	    .attr("fill", appColors[0])
	    // .attr("fill","#diagonal-stripe-1")
	    .attr("y", function (d, i) {
            return y(i) - (baseHeight / 2);
        })
	    .on("mouseover", function(d, i) {
            var tipHtml = d.toFixed(1) + " Projected Applicants";
            showTip(tipHtml);
        })
        .on('mouseout', function() {
            hideTip();
        });

	var eligBars = appSVG.selectAll("rect.elig")
	    .data(appData.eligible)
	    .enter()
	    .append("rect")
	    .attr('class', 'elig')
	    .attr("width", function (d) {
             return x(d);
        })
	    .attr("height", baseHeight * 0.8)
	    .attr("y", function (d, i) {
            return y(i) - (baseHeight * 0.8 / 2);
        })
	    .attr("fill",appColors[1])
	    .on("mouseover", function(d, i) {
            var percent = (d / appData.applicants[i] * 100).toFixed(1);
            var tipHtml = d.toFixed(1) + " Projected Eligible</br>" + percent + "% of Applicants";
            showTip(tipHtml);
        })
        .on('mouseout', function() {
            hideTip();
        });

	var qualBars = appSVG.selectAll("rect.qual")
	    .data(appData.qualified)
	    .enter()
	    .append("rect")
	    .attr('class', 'qual')
	    .attr("width", function (d) {
            return x(d);
        })
	    .attr("height", baseHeight * 0.6)
	    .attr("y", function (d, i) {
            return y(i) - (baseHeight * 0.6 / 2);
        })
	    .attr("fill", appColors[2])
	    .on("mouseover", function(d, i) {
            var percent = (d / appData.applicants[i] * 100).toFixed(1);
            var tipHtml = d.toFixed(1) + " Projected Qualified</br>" + percent + "% of Applicants";
            showTip(tipHtml);
        })
        .on('mouseout', function() {
            hideTip();
        });

	var hiredBars = appSVG.selectAll("rect.hire")
	    .data(appData.hired)
	    .enter()
	    .append("rect")
	    .attr('class', 'hire')
	    .attr("width", function (d) {
            return x(d);
        })
	    .attr("height", baseHeight * 0.4)
	    .attr("y", function (d, i) {
            return y(i) - (baseHeight * 0.4 / 2);
        })
	    .attr("fill", appColors[3])
	    .on("mouseover", function(d, i) {
            var percent = (d / appData.applicants[i] * 100).toFixed(1);
            var tipHtml = d.toFixed(1) + " Projected Hires</br>" + percent + "% of Applicants";
            showTip(tipHtml);
        })
        .on('mouseout', function() {
            hideTip();
        });

	appSVG.append("g")
	        .attr("class", "x axis")
	        .call(xAxis)
	        .attr("transform", "translate(0,"+ chartHeight +")")
	        .style(cssAxisNumbers)
	        .style("fill", "black")
	    .append("text")
	        .attr("x", (appWidth/2) * .9 )
	        .attr("y", chartHeight * 0.3)
	        .style({"text-anchor": "middle",
	        	   "font-weight": "normal",
	        		"font-size": "1em"})
	        .text("Student Count");

	appSVG.append("g")
		.attr('class','y axis')
		.call(yAxis)
		.style(cssAxisNumbers)
		.style({"font-size": "1em",
			    "fill": "black"});

	appSVG.selectAll('.axis line, .axis path')
			.style(cssAxis)
	        .style("stroke", "black");

	var legendRectSize = appHeight * 0.075;
	var legendSpacing = appHeight * 0.015;

	var color = d3.scale.ordinal()
	  .range(appColors); 

	color.domain(d3.keys(appData).filter(function (key) {
	    return key !== "type" && key !== "types" ;
	}));

	_.forEach(appData, function (values, d) {
	    var y0 = 0;
	    d.types = color.domain().map(function (type) {
	        return {
	            name: type,
	            y0: y0,
	            y1: y0 += +d[type]
	        };
	    });
	});
		
	var legend = appSVG.selectAll('.legend')
	  .data(color.domain())
	  .enter()
	  .append('g')
	  .attr('class', 'legend')
	  .attr('transform', function(d, i) {
	    var height = legendRectSize + legendSpacing;
	    var offset =  height * color.domain().length / 4;
	    var horz =  appWidth* .8;
	    var vert = i * height - offset;
	    return 'translate(' + horz + ',' + vert + ')';
	  });

	legend.append('rect')
	  .attr('width', legendRectSize)
	  .attr('height', legendRectSize)
	  .style('fill', color)
	  .style('stroke', function(d) {
            return d3.rgb(color(d)).darker().toString();
      })
	  .style("font-size","0.8em");

	legend.append('text')
	  .attr('x', legendRectSize + legendSpacing)
	  .attr('y', legendRectSize)
	  .text(function(d) { return d.toProperCase(); });

}

//End of Layered Bar Chart

var Colorscale = ['#f7f7f7','#31a354','#f7f7f7'];

//Start of Stacked Bar for SAT Scores

function satScores(satDataset){

	$(".satcontainer svg").remove();

	var	satDataset = [
	[{x:satDataset.satmt25, x0:0, y: "Math"},
	 {x:satDataset.satvr25, x0:0, y: "Verbal"},
	 {x:satDataset.satwr25, x0:0, y: "Writing"}],
	[{x:satDataset.satmt75-satDataset.satmt25, 
	  x0:satDataset.satmt25, 
	  y: "Math"},
	 {x:satDataset.satvr75-satDataset.satvr25, 
	  x0:satDataset.satvr25, 
	  y: "Verbal"},
	 {x:satDataset.satwr75-satDataset.satwr25, 
	  x0:satDataset.satwr25, 
	  y: "Writing"}],
	[{x:800-satDataset.satmt75, 
	  x0:satDataset.satmt75, 
	  y: "Math"},
	 {x:800-satDataset.satvr75, 
	  x0:satDataset.satvr75, 
	  y: "Verbal"},
	 {x:800-satDataset.satwr75,
	  x0:satDataset.satwr75, 
	  y: "Writing"}]
	];

	var satMargins = {
	    top: modalHeight * 0.01,
	    left: modalWidth * 0.04,
	    right: modalWidth * 0.01,
	    bottom: modalHeight * 0.04
	},
		satWidth = (modalWidth * .2) - satMargins.left - satMargins.right,
	    satHeight = (modalHeight * .15) - satMargins.top - satMargins.bottom;

	var satSVG = d3.select('.satcontainer')
	    .append('svg')
	    .attr('width', satWidth + satMargins.left + satMargins.right)
	    .attr('height', satHeight + satMargins.top + satMargins.bottom)
	    .append('g')
	    .attr('transform', 'translate(' + satMargins.left + ',' 
	    	  + '0' + ')');

	var satXScale = d3.scale.linear()
		        .domain([0, 800])
		        .range([0, satWidth]);

	var satSections = [ "Math", "Verbal", "Writing" ];

	var satyScale = d3.scale.ordinal()
	        .domain(satSections)
	        .rangeRoundBands([0, satHeight], .1);

	var satXAxis = d3.svg.axis()
	        .scale(satXScale)
	        .orient('bottom');

	var satYAxis = d3.svg.axis()
	        .scale(satyScale)
	        .orient('left');

	satSVG.append('g')
	    .attr('class', 'axis')
	    .attr('transform', 'translate(0,' + satHeight + ')')
	    .call(satXAxis)
	    .style(cssAxisNumbers)
	    .append("text")
	        .attr("x", (satWidth/2))
	        .attr("y", satHeight/2.7)
	        .style({"text-anchor": "middle",
	        	   "font-weight": "normal",
	        		"font-size": "1em"
	        	})
	        .text("Score");

	satSVG.append('g')
	    .attr('class', 'axis')
	    .call(satYAxis)
	    .style(cssAxisNumbers);

	satSVG.selectAll('.axis line, .axis path')
	 		.style(cssAxis);

	var groups = satSVG.selectAll('.satg')
	        .data(satDataset)
	        .enter()
	        .append('g')
	        .style('fill', function (d, i) {
	        return Colorscale[i];
	    }),
	    rects = groups.selectAll('rect')
	        .data(function (d) {
	        return d;
	    })
	        .enter()
	        .append('rect')
	        .attr('x', function (d) {
	        return satXScale(d.x0);
	    })
	        .attr('y', function (d, i) {
	        return satyScale(d.y);
	    })
	        .attr('height', function (d) {
	        return satyScale.rangeBand() * .75;
	    })
	        .attr('width', function (d) {
	        return satXScale(d.x);
	    })

        .on('mouseover', function(d, i) {
            if(satDataset[1][i].y == null || satDataset[1][i].x0 == null || 
               satDataset[1][i].x == null) {
                showTip("No Data");
            } else {
                var tipHtml = satDataset[1][i].y + "<br/>" +
                     " 25th Percentile: " + satDataset[1][i].x0 +
                     "<br/>75th Percentile:  " + (satDataset[1][i].x0 + satDataset[1][i].x);
                showTip(tipHtml);
            }
        })
        .on('mouseout', function() {
            hideTip();
        });
 		
}
//End of Stacked Bar for SAT Scores

//Start of ACT Scores

function actScores(actDataset){

	$(".actcontainer svg").remove();

	var	actDataset = [
		[{x:actDataset.actcm25, x0:0, y: "Composite"}],
		[{x:actDataset.actcm75-actDataset.actcm25, 
		  x0:actDataset.actcm25, 
		  y: "Composite"},],
		[{x:36-actDataset.actcm75, 
		  x0:actDataset.actcm75, 
		  y: "Composite"}]
		];

	var actMargins = {
	    top: modalHeight * 0.01,
	    left: modalWidth * 0.04,
	    right: modalWidth * 0.01,
	    bottom: modalHeight * 0.03
	},
		actWidth = (modalWidth * .2) - actMargins.left - actMargins.right,
	    actHeight = (modalHeight * .1) - actMargins.top - actMargins.bottom;

	var actSVG = d3.select('.actcontainer')
	    .append('svg')
	    .attr('width', actWidth + actMargins.left + actMargins.right)
	    .attr('height', actHeight + actMargins.top + actMargins.bottom)
	    .append('g')
	    .attr('transform', 'translate(' + actMargins.left + ',' 
	    	  + '0'+ ')');

	var actXScale = d3.scale.linear()
		        .domain([0, 36])
		        .range([0, actWidth]);

	var actSections = [ "Composite" ];

	var actyScale = d3.scale.ordinal()
	        .domain(actSections)
	        .rangeRoundBands([0, actHeight], .1);

	var actXAxis = d3.svg.axis()
	        .scale(actXScale)
	        .orient('bottom');

	var actYAxis = d3.svg.axis()
	        .scale(actyScale)
	        .orient('left');

	actSVG.append('g')
	    .attr('class', 'axis')
	    .attr('transform', 'translate(0,' + actHeight + ')')
	    .call(actXAxis)
	    .style(cssAxisNumbers)
	    .append("text")
	        .attr("x", (actWidth/2))
	        .attr("y", actHeight/1.5)
	        .style({"text-anchor": "middle",
	        	   "font-weight": "normal",
	        		"font-size": "1em"
	        	})
	        .text("Score");

	actSVG.append('g')
	    .attr('class', 'axis')
	    .call(actYAxis)
	    .style(cssAxisNumbers);

	actSVG.selectAll('.axis line, .axis path')
	 		.style(cssAxis);

	var groups = actSVG.selectAll('.actg')
	        .data(actDataset)
	        .enter()
	        .append('g')
	        .style('fill', function (d, i) {
	        return Colorscale[i];
	    }),
	    rects = groups.selectAll('rect')
	        .data(function (d) {
                return d;
            })
	        .enter()
	        .append('rect')
	        .attr('x', function (d) {
                return actXScale(d.x0);
            })
	        .attr('y', function (d, i) {
                return actyScale(d.y);
            })
	        .attr('height', function (d) {
                return actyScale.rangeBand() * .75;
            })
	        .attr('width', function (d) {
                return actXScale(d.x);
            })
            .on("mouseover", function(d, i) {
                if(actDataset[0][0].x == null || actDataset[1][0].x == null) {
                    showTip("No Data");
                } else {
                    var tipHtml = " 25th Percentile: " + actDataset[0][0].x +
                        "<br/>75th Percentile:  " + (actDataset[0][0].x + actDataset[1][0].x);
                    showTip(tipHtml);
                }
            })
            .on('mouseout', function() {
                hideTip();
            });
}
//End of ACT Scores



//Start Graduation Rates	

function gradRatesPie(gradRate){
	$(".gradcontainer svg").remove();

	var grData = [ 
				{label: "4-Year", 
				 count: gradRate.bach_gradrate_100, 
				 total: gradRate.bach_gradrate_100},
				{label: "6-Year", 
				 count: gradRate.bach_gradrate_150 - gradRate.bach_gradrate_100,
				 total: gradRate.bach_gradrate_150},
				{label: "8-Year", 
				 count: gradRate.bach_gradrate_200 - gradRate.bach_gradrate_150,
				 total: gradRate.bach_gradrate_200},
				{label: "diff", 
				 count:  100 - gradRate.bach_gradrate_200, 
				 total: 100}
				];

	var gradHeight = modalHeight * .15;
	var	gradWidth = gradHeight;

	var gradSVG = d3.select(".gradcontainer")
					.append('svg')
				    .attr("width", gradWidth)
				    .attr("height", gradHeight)
				   .append("g")
	    			.attr("transform", "translate(" + (gradWidth/2)
	    				   + "," + (gradHeight/2) + ")");
	
	var radius = Math.min(gradWidth, gradHeight) / 2 - 1;

	var color = d3.scale.ordinal()
        .range(['#31a354','#006d2c','#a0a0a0','#f7f7f7']);

	var arc = d3.svg.arc()
	    .outerRadius(radius)
	    .innerRadius(radius * 0.8);

	var pie = d3.layout.pie()
	    .sort(null)
	    .startAngle(Math.PI * .5)
	    .endAngle(2.5 * Math.PI)
	    .value(function(d) { return d.count; });

	var g = gradSVG.selectAll(".arc")
	  .data(pie(grData))
	.enter().append("g")
	  .attr("class", "arc")
      .on('mouseover',function(d){	
      	if(d.data.label !=="diff"){
      		gradLabel
      			.text(d.data.label)
      			.style("visibility","visible");
      		gradNum
      			.text(d.data.total + "%")
      			.style("visibility","visible");
			gradSVG.selectAll('.legend').style("visibility","hidden");
      	}})

      .on('mouseout', function(){
			gradLabel.style("visibility","hidden");
			gradNum.style("visibility","hidden");
			gradSVG.selectAll('.legend').style("visibility","visible");
      	});

	var legendRectSize = radius * 0.25;
	var legendSpacing = radius * 0.05;

  	var gradLabel = g.append("text")
        .attr("text-anchor", "middle")  
        .style(cssAxisNumbers)
        .style("font-size", "1.5em")
        .text(" ");

  	var gradNum = g.append("text")
        .attr("text-anchor", "middle")
        .attr("dy", "1em")
        .style(cssAxisNumbers)
        .style("font-size", "1.5em")
        .text(" ");

	g.append("path")
	    .attr("fill", function(d, i) { return color( d.data.label); })
	  .transition()
	    .ease("exp")
	    .duration(1000)
	    .attrTween("d", tweenPie);

    var legend = gradSVG.selectAll('.legend')                 
      .data(color.domain().slice(0,grData.length -1))                               
      .enter()                                            
      .append('g')                                        
      .attr('class', 'legend')                            
      .attr('transform', function(d, i) {                 
        var height = legendRectSize + legendSpacing;      
        var offset =  height * color.domain().length /2.5; 
        var horz = -radius + 2 * legendRectSize;                   
        var vert = i * height - offset;                   
        return 'translate(' + horz + ',' + vert + ')';    
      });

	function tweenPie(b) {
	  var i = d3.interpolate({startAngle: 1*Math.PI, endAngle: 1*Math.PI}, b);
	  return function(t) { return arc(i(t)); };
	}                                             

    legend.append('rect')                                 
      .attr('width', legendRectSize)                      
      .attr('height', legendRectSize)                     
      .style('fill', color)                               
      .style('stroke', color);                            
      
    legend.append('text')                                 
      .attr('x', legendRectSize + legendSpacing)          
      .attr('y', legendRectSize - legendSpacing)          
      .text(function(d) { return d; })
      .style("fill", "white")
      .style("font-size", "1.2em");     

}
//End Graduation Rates

//Start Acceptance Rates

function acceptRatePie(acceptRate){
	$(".acceptcontainer svg").remove();

	var arData = [ {value: acceptRate},
				   {value: 100 - acceptRate}];

	var acceptHeight = modalHeight * .15;
	var	acceptWidth = acceptHeight;		

	var acceptSVG = d3.select(".acceptcontainer")
					.append('svg')
				    .attr("width", acceptWidth)
				    .attr("height", acceptHeight)
				   .append("g")
	    			.attr("transform", "translate(" + (acceptWidth/2)
	    				   + "," + (acceptHeight/2) + ")");

	var radius = Math.min(acceptWidth, acceptHeight) / 2 - 1;

	var color = d3.scale.ordinal()
        .range(['#31a354','#f7f7f7']);

	var arc = d3.svg.arc()
	    .outerRadius(radius)
	    .innerRadius(radius * 0.8);

	var pie = d3.layout.pie()
	    .sort(null)
	    .startAngle(Math.PI * .5)
	    .endAngle(2.5 * Math.PI)
	    .value(function(d) { return d.value; });

	var g = acceptSVG.selectAll(".arc")
	  .data(pie(arData))
	.enter().append("g")
	  .attr("class", "arc");

	g.append("path")
	    .attr("fill", function(d, i) { return color(i); })
	  .transition()
	    .ease("exp")
	    .duration(1000)
	    .attrTween("d", tweenPie);

	function tweenPie(b) {
	  var i = d3.interpolate({startAngle: 1*Math.PI, endAngle: 1*Math.PI}, b);
	  return function(t) { return arc(i(t)); };
	}

	g.append("text")
        .attr("text-anchor", "middle")  
        .style(cssAxisNumbers)
        .style("font-size", "1.5em")
        .text(function(d){return acceptRate + "%";})
        .attr("dominant-baseline", "central");

}
//End Acceptance Rates

function getSchoolDetails(unitid) {
    var queryString = parseQueryFromInputs();
    schoolResults(unitid + queryString);
}

// redraw table with new data
function populateTable(data) {

    // // add attribute for hiring score
    // var maxHires = d3.max(data, function(school) { 
    //     return school.potential_hires; 
    // });
    //
    // // add attribute for hiring score
    // var minHires = d3.min(data, function(school) { 
    //     return school.potential_hires; 
    // });
    //
    // var score = d3.scale.linear()
    //   .domain([0,maxHires])
    //   .rangeRound([0,100]);

    _.forEach(data, function(school) {
        // school.hiring_score = score(school.potential_hires);
        school.affiliation_label = affiliationLabels[school.affiliation];
        school.pct_degrees = school.degree_count / school.total_degrees * 100;
    });

    //set number of rows depending on screen size
    var numRows;
    if(window.innerHeight > 1000 || window.innerWidth > 2000) {
        numRows = 15;
    } else if(window.innerHeight > 500 || window.innerWidth > 1000) {
        numRows = 10;
    } else {
        numRows = 5;
    }

    // set up school table structure
    $("#schoolsTable").DataTable( {
        "destroy": true,
        "scrollY": $("#map").height(),
        "scrollCollapse": true,
        "iDisplayLength": numRows,
        "lengthMenu": [5,10,20],
        "order": [[4, "desc"]],
        "columns": [
            {"data": "unitid", "title": "unitid", "visible": false},
            {"data": "school_name", "title": "School"},
            {"data": "affiliation_label", "title": "Affiliation"},
            {"data": "pct_degrees", "title": "Percent of Total Degrees",
             "render": function(data, type, row, meta) {
                return d3.format(",.0f")(data) + "%";
             }
            },
            {"data": "degree_count", "title": "Degree Matches",
             "render": function(data, type, row, meta) { 
                 return d3.format(",.0f")(data); 
             } 
            },
        ],
        "data": data,
        "pagingType": "full"
    } );

    // get school details when table row clicked
    $('#schoolsTable tbody').on( 'click', 'tr', function () {
        var schoolData = $("#schoolsTable").DataTable().row(this).data();
        getSchoolDetails(schoolData.unitid);
    });

    // fade out other circles when hovering over row
    $('#schoolsTable tbody').on( 'mouseover', 'tr', function () {
        var schoolData = $("#schoolsTable").DataTable().row(this).data();
        var feature = d3.selectAll(".school-circle")
          .style("fill-opacity", function(d) {
              if(d.unitid == schoolData.unitid) {
                  return 0.7;
              } else {
                  return 0.1;
              }
          });
    });

    // return circles to same opacity on mouse exit
    $('#schoolsTable tbody').on( 'mouseout', 'tr', function () {
        var schoolData = $("#schoolsTable").DataTable().row(this).data();
        var feature = d3.selectAll(".school-circle")
          .style("fill-opacity", function(d) {
              if(selectedAffiliation && d.affiliation != selectedAffiliation) {
                  return 0.1;
              } else {
                  return 0.7;
              }
          });
    });
}

// make query string from select inputs
function parseQueryFromInputs() {

    // get input values
    var majors = $("#select2-major").val();
    var levels = $("#select2-level").val();
    var gender = $("#optgroup-gender :selected").val();
    var ethnicities = [];
    $("#optgroup-ethnicity :selected").each(function() {
        ethnicities.push(this.value);
    });
    var locations = $("#select2-location").val();

    // use values to create query string
    var queryString = "?";
    if (majors != null) {
        queryString += "major=" + majors.toString() + "&";
    }
    if (levels != null) {
        queryString += "level=" + levels.toString() + "&";
    }
    if (gender != null) {
        queryString += "gender=" + gender + "&";
    }
    if (ethnicities.length > 0) {
        queryString += "ethnicity=" + ethnicities.toString() + "&";
    }
    if (locations != null) {
        queryString += "location=" + locations + "&";
    }

    return queryString;

}

//resize elements when window size changes
$(window).bind('resize', function () {
    if(showAffiliations) {
        d3.select("#afflegend svg").remove();
        showAffiliationsLegend();
    }
    var table = $("#schoolsTable").DataTable();
    //set number of rows depending on screen size
    if(window.innerWidth > 1200) {
        table.page.len(15);
    } else {
        table.page.len(10);
    }
    table.draw();
});

$(document).ready(function () {
    $(".select2-container").select2({closeOnSelect: false});

    schoolResults("");

    // resizing based on screen size
    if(window.innerHeight > 1000 || window.innerWidth > 2000) {
        $('.splash-message').css('padding-top', '25%');
        $('.gradcontainer').css('float', 'none');
        $('.acceptcontainer').css('float', 'none');
    } else if (window.innerHeight < 500 || window.innerWidth < 1000) {
        $('.splash-sourcingtitle').css('font-size', '2em');
        $('.splash-desc').css('font-size', '1em');
        $('.splash-pagescrollbtn').css('font-size', '1em');
        $('.map-inputs').css('width', '30%');
        $('.map-list').css('width', '30%');
        $('.map-container').css('width', '40%');
    }

    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $(".map-page").toggleClass("toggled");
        $(".map-list").toggle();
        $("#schoolsTable").DataTable().columns.adjust();
    });

    $(".map-list").hide();

    // submit query to get school results
    $("#submit").click(function() {
        var queryString = parseQueryFromInputs();
        schoolResults(queryString);
    });

    // clear all inputs
    $("#clear").click(function() {
        $("#select2-job").val([]).change();
        $("#select2-major").val([]).change();
        $("#select2-level").val([]).change();
        $("#select2-diversity").val([]).change();
        $("#select2-location").val([]).change();
        $("#checkbox-stem").attr("checked", false);
    });

    // add or remove stem majors
    $("#checkbox-stem").change(function() {
        var current_majors = $("#select2-major").val();
        var new_majors;
        if(this.checked) {
            if (current_majors != null) {
                new_majors = Array.from(Set($.merge(current_majors, stem_majors)));
            } else {
                new_majors = stem_majors;
            }
        } else {
            if (current_majors != null) {
                new_majors = current_majors.filter(function(maj) { 
                    return stem_majors.indexOf(parseInt(maj)) == -1;
                });
            } else {
                new_majors = [];
            }
        }
        $("#select2-major").val(new_majors).change();
    });

    // add or remove majors mapped to job descriptions
    $("#select2-job").change(function() {
        var majors = $(this).val();
        if(majors != null) {
            majors = majors.filter(function(v) { return v != ""; }); // remove empty values
            majors = majors.join(); // create one comma-separated string
            majors = majors.split(',') // divide into list
            majors = majors.map(Number); // convert string to numbers
            $("#select2-major").val(majors).change();
        }
    });

    // toggle showing affiliations on button click
    $('.showaffbtn button').click(function() {
        toggleAffiliations();
    });

    // use bootstrap tooltips
    $('[data-toggle="tooltip"]').tooltip(); 

    // set tooltip for bubble chart
    var bubbletip = bubbleTooltip();
    $('#bubbleinfo').tooltip({html: true, title: bubbletip});

    // show instructions for map page when enter button clicked
    $("#enter").click(function() {
        window.location = this.hash;
        $("#introModal").modal('show');
        $('[data-toggle="popover"]').popover({trigger: 'manual'});
        $('[data-toggle="popover"]').popover('show');
    })

    // close popovers when instructions closed
    $("#introModal button").click(function() {
        $('#introModal').modal('hide');
        $('[data-toggle="popover"]').popover('hide');
    });
}); 
