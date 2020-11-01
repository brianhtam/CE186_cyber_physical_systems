var ul = $('ul#side-menu');
$.ajax({
    url : '/static/extend_dashboard_links.html', 
    type: "get", 
    success : function(response){
console.log("Load /static/extend_dashboard_links.html");
ul.append(response);}
});

var wrapper = $('div#wrapper'); 
$.ajax({
        url : '/static/extend_dashboard_pages.html', 
        type: "get",
        success : function(response){
console.log("Load /static/extend_dashboard_pages.html"); 
wrapper.append(response);
    // Form submit call goes here.
$("form#form-input").submit(onInputFormSubmit); }
});



function onInputFormSubmit(e){ 
    e.preventDefault();
        
    var object_id = "names";
    var stream_id = "form-input";
    // Gather the data
    // and remove any undefined keys

    var data = {};
    $('input',this).each( function(i, v){
        var input = $(v); 
        data[input.attr("name")] = input.val();
});
delete data["undefined"];

console.log( data );


var url = '/networks/'+network_id+'/objects/';
url = url + object_id+'/streams/'+stream_id+'/points'; 
var query = {
    "points-value": JSON.stringify( data ) 
};

// Send the request to the Pico server
$.ajax({
    url : url+'?'+$.param(query), type: "post",
    success : function(response){
        var this_form = $("form#form-input");
if( response['points-code'] == 200 ){
        console.log("Success");
        // Clear the form
        this_form.trigger("reset"); }
        // Log the response to the console
        console.log(response); },
error : function(jqXHR, textStatus, errorThrown){
// Do nothing
} });
};


function getPoints( the_network_id, the_object_id, the_stream_id, callback ){
    var query_data = {};
    var query_string = '?'+$.param(query_data);
    var url = '/networks/'+the_network_id+'/objects/'+the_object_id;
    url += '/streams/'+the_stream_id+'/points'+query_string;

// Send the request to the server
$.ajax({
    url : url,
    type: "get",
    success : function(response){
        console.log( response );

    if( response['points-code'] == 200 ){
        var num_points = response.points.length
    var most_recent_value = response.points[0].value 
    console.log("Most recent value: "+most_recent_value); 
    console.log("Number of points retrieved: "+num_points); 
    callback( response.points );
    } 
    },
    error : function(jqXHR, textStatus, errorThrown){ 
        console.log(jqXHR);
    }
    }); 
}

// Call getPoints if Input or Report is selected
custom_sidebar_link_callback = function( select ){ 
        if (select == 'Received Data') {
            var plotCalls = 0;
            var plotTimer = setInterval( function(){
                getPoints('local','ReceivedData','ReceivedDataStream', function(points){ 
                        console.log( "The points request was successful!" );
                        loadPlot1( points );
                        });
                if( plotCalls > 20 ){ 
                        console.log( 'Clear timer' ); 
                        clearInterval( plotTimer );
                }else{
                        plotCalls += 1; 
                }
                }, 1000); 
            }

        else if (select == 'CO2'){
            var plotCalls = 0;
            var plotTimer = setInterval( function(){
                getPoints('local','Arduino','CO2', 
                          function(points){ 
                        console.log( "The CO2 points request was successful!" );
                        loadPlot2( points );
                        });
                if( plotCalls > 20 ){ 
                        console.log( 'Clear timer' ); 
                        clearInterval( plotTimer );
                }else{
                        plotCalls += 1; 
                }
                }, 1000); 
            }

        else if (select == 'PM'){
            var plotCalls = 0;
            var plotTimer = setInterval( function(){
                getPoints('local', 'Arduino', 'PM',function(points){
                    console.log("The PM points request was succesful!");
                    loadPlot3( points );
                    });
                if( plotCalls > 20 ){
                        console.log( 'Clear Timer' );
                        clearInterval( plotTimer );
                }else{
                        plotCalls += 1;
                }
                }, 1000);
            }

        else if (select == 'VOC'){
            var plotCalls = 0;
            var plotTimer = setInterval( function(){
                getPoints('local', 'Arduino', 'VOC',function(points){
                    console.log("The VOC points request was succesful!");
                    loadPlot4( points );
                    });
                if( plotCalls > 20 ){
                        console.log( 'Clear Timer' );
                        clearInterval( plotTimer );
                }else{
                        plotCalls += 1;
                }
                }, 1000);
            }

        else if (select == 'Humidity'){
            var plotCalls = 0;
            var plotTimer = setInterval( function(){
                getPoints('local', 'Arduino', 'Humidity',function(points){
                    console.log("The Humidity points request was succesful!");
                    loadPlot5( points );
                    });
                if( plotCalls > 20 ){
                        console.log( 'Clear Timer' );
                        clearInterval( plotTimer );
                }else{
                        plotCalls += 1;
                }
                }, 1000);
            }

        else if (select == 'Temperature'){
            var plotCalls = 0;
            var plotTimer = setInterval( function(){
                getPoints('local', 'Arduino', 'Temperature',function(points){
                    console.log("The Temperature points request was succesful!");
                    loadPlot6( points );
                    });
                if( plotCalls > 20 ){
                        console.log( 'Clear Timer' );
                        clearInterval( plotTimer );
                }else{
                        plotCalls += 1;
                }
                }, 1000);
            }

}

function loadPlot1( points ){
    var plot = $('#content-ReceivedData');
    // Check if plot has a Highcharts element 
    if( plot.highcharts() === undefined ){
    // Create a Highcharts element
        plot.highcharts( report_plot_options_1 ); 
    }
    
  // Iterate over points to place in Highcharts format
    var datapoints = [];
    for ( var i = 0; i < points.length; i++){
        var at_date = new Date(points[i].at);
        var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; 
        datapoints.unshift( [ at, points[i].value] );
}
  
    // Update Highcharts plot
    if( plot.highcharts().series.length > 0 ){ 
        plot.highcharts().series[0].setData( datapoints );
    }else{ 
        plot.highcharts().addSeries({
            name: "Stream Points",
            data: datapoints 
        });
    } 
}

function loadPlot2( points ){
    var plot = $('#content-CO2');
    // Check if plot has a Highcharts element 
    if( plot.highcharts() === undefined ){
    // Create a Highcharts element
        plot.highcharts( report_plot_options_2 ); 
    }
    
  // Iterate over points to place in Highcharts format
    var datapoints = [];
    for ( var i = 0; i < points.length; i++){
        var at_date = new Date(points[i].at);
        var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; 
        datapoints.unshift( [ at, points[i].value] );
}
  
    // Update Highcharts plot
    if( plot.highcharts().series.length > 0 ){ 
        plot.highcharts().series[0].setData( datapoints );
    }else{ 
        plot.highcharts().addSeries({
            name: "CO2 Stream Points",
            data: datapoints 
        });
    } 
}
        
function loadPlot3( points ){
    var plot = $('#content-PM');
    // Check if plot has a Highcharts element 
    if( plot.highcharts() === undefined ){
    // Create a Highcharts element
        plot.highcharts( report_plot_options_3 ); 
    }
    
  // Iterate over points to place in Highcharts format
    var datapoints = [];
    for ( var i = 0; i < points.length; i++){
        var at_date = new Date(points[i].at);
        var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; 
        datapoints.unshift( [ at, points[i].value] );
}
  
    // Update Highcharts plot
    if( plot.highcharts().series.length > 0 ){ 
        plot.highcharts().series[0].setData( datapoints );
    }else{ 
        plot.highcharts().addSeries({
            name: "PM Stream Points",
            data: datapoints 
        });
    } 
}

function loadPlot4( points ){
    var plot = $('#content-VOC');
    // Check if plot has a Highcharts element 
    if( plot.highcharts() === undefined ){
    // Create a Highcharts element
        plot.highcharts( report_plot_options_4 ); 
    }
    
  // Iterate over points to place in Highcharts format
    var datapoints = [];
    for ( var i = 0; i < points.length; i++){
        var at_date = new Date(points[i].at);
        var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; 
        datapoints.unshift( [ at, points[i].value] );
}
  
    // Update Highcharts plot
    if( plot.highcharts().series.length > 0 ){ 
        plot.highcharts().series[0].setData( datapoints );
    }else{ 
        plot.highcharts().addSeries({
            name: "VOC Stream Points",
            data: datapoints 
        });
    } 
}
        
function loadPlot5( points ){
    var plot = $('#content-Humidity');
    // Check if plot has a Highcharts element 
    if( plot.highcharts() === undefined ){
    // Create a Highcharts element
        plot.highcharts( report_plot_options_5 ); 
    }
    
  // Iterate over points to place in Highcharts format
    var datapoints = [];
    for ( var i = 0; i < points.length; i++){
        var at_date = new Date(points[i].at);
        var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; 
        datapoints.unshift( [ at, points[i].value] );
}
  
    // Update Highcharts plot
    if( plot.highcharts().series.length > 0 ){ 
        plot.highcharts().series[0].setData( datapoints );
    }else{ 
        plot.highcharts().addSeries({
            name: "Humidity Stream Points",
            data: datapoints 
        });
    } 
}

function loadPlot6( points ){
    var plot = $('#content-Temperature');
    // Check if plot has a Highcharts element 
    if( plot.highcharts() === undefined ){
    // Create a Highcharts element
        plot.highcharts( report_plot_options_6 ); 
    }
    
  // Iterate over points to place in Highcharts format
    var datapoints = [];
    for ( var i = 0; i < points.length; i++){
        var at_date = new Date(points[i].at);
        var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; 
        datapoints.unshift( [ at, points[i].value] );
}
  
    // Update Highcharts plot
    if( plot.highcharts().series.length > 0 ){ 
        plot.highcharts().series[0].setData( datapoints );
    }else{ 
        plot.highcharts().addSeries({
            name: "Temperature Stream Points",
            data: datapoints 
        });
    } 
}
    
        

var report_plot_options_1 = {
 chart: {
 type: 'spline'
 },
 title: {
 text: 'ReceivedDataStream Data Points'
 },
 subtitle: {
 text: 'By_ Matthew Choi'
 },
 yAxis: {
 title: {
 text: 'Received Data Point'
 },
 },
 xAxis: {
 type: 'datetime',
 dateTimeLabelFormats: {//don't display the dummy year
 month: '%e. %b',
 year: '%b'
 },
 }
};
 
var report_plot_options_2 = {
 chart: {
 type: 'spline'
 },
 title: {
 text: 'CO2 Stream Data Points'
 },
 subtitle: {
 text: 'By_ Matthew Choi'
 },
yAxis: {
 title: {
 text: 'CO2',
 },
 },
 xAxis: {
 type: 'datetime',
  dateTimeLabelFormats: {//don't display the dummy year
 month: '%e. %b',
 year: '%b'
 },
 },
};
                         
var report_plot_options_3 = {
 chart: {
 type: 'spline'
 },
 title: {
 text: 'PM Stream Data Points'
 },
 subtitle: {
 text: 'By_ Matthew Choi'
 },
 yAxis: {
 title: {
 text: 'PM'
 },
 },
 xAxis: {
 type: 'datetime',
 dateTimeLabelFormats: {//don't display the dummy year
 month: '%e. %b',
 year: '%b'
 },
 },
};
                        
                        
var report_plot_options_4 = {
 chart: {
 type: 'spline'
 },
 title: {
 text: 'VOC Stream Data Points'
 },
 subtitle: {
 text: 'By_ Matthew Choi'
 },
 yAxis: {
 title: {
 text: 'VOC'
 },
 },
 xAxis: {
 type: 'datetime',
 dateTimeLabelFormats: {//don't display the dummy year
 month: '%e. %b',
 year: '%b'
 },
 },
};

var report_plot_options_5 = {
 chart: {
 type: 'spline'
 },
 title: {
 text: 'Humidity Stream Data Points'
 },
 subtitle: {
 text: 'By_ Matthew Choi'
 },
 yAxis: {
 title: {
 text: 'Humidity'
 },
 },
 xAxis: {
 type: 'datetime',
 dateTimeLabelFormats: {//don't display the dummy year
 month: '%e. %b',
 year: '%b'
 },
 },
};
                        
var report_plot_options_6 = {
 chart: {
 type: 'spline'
 },
 title: {
 text: 'Temperature Stream Data Points'
 },
 subtitle: {
 text: 'By_ Matthew Choi'
 },
 yAxis: {
 title: {
 text: 'Temperature'
 },
 },
 xAxis: {
 type: 'datetime',
 dateTimeLabelFormats: {//don't display the dummy year
 month: '%e. %b',
 year: '%b'
 },
 },
};