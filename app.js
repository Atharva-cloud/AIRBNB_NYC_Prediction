 
 function get_no_of_revs() {
    var uireviews = document.getElementsByName("uireviews");
    for(var i in uireviews) {
      if(uireviews[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }




    function onClickedEstimatePrice() {
        console.log("Estimate price button clicked");

        var no_of_revs = get_no_of_revs();

        var revpmonth = document.getElementById("uirevpermonth");
        var availability = document.getElementById("uiavailability");
        var min_nights =  document.getElementById("uimin_nights");
        var host_count = document.getElementById("uihost_count");
        var name_length = document.getElementById("uilength");

        var nh_grp = document.getElementById("uineighbourhoodgrp");
        var nh_names = document.getElementById("uineighbourhood");
        var rt_names = document.getElementById("uiroomtype");
        
        var estPrice = document.getElementById("uiEstimatedPrice");

        var url = "http://127.0.0.1:5000/get_airbnb_price";

        $.post(url, {
            revpmonth: revpmonth.value,
            no_of_revs: no_of_revs,
            availability: availability.value,
            min_nights: min_nights.value,
            host_count: host_count.value,
            name_length:  name_length.value,

            nh_grp: nh_grp.value,
            nh_names : nh_names.value,
            rt_names : rt_names.value

        },function(data, status) {
            console.log(data.airbnb_price);
            estPrice.innerHTML = "<h2>" + data.airbnb_price.toString() + " $</h2>";
            console.log(status);
        });
      }

      function onPageLoad() {
        console.log( "document loaded" );
        var url = "http://127.0.0.1:5000/get_ng_grp_names"  ; 
        $.get(url,function(data, status) {
            console.log("got response for get_ng_grp_names request");
            if(data) {
                var ng_grps = data.ng_grps;
                var uineighbourhoodgrp = document.getElementById("uineighbourhoodgrp");
                $('#uineighbourhoodgrp').empty();
                for(var i in ng_grps) {
                    var opt = new Option(ng_grps[i]);
                    $('#uineighbourhoodgrp').append(opt);
                }
            }
        });
    
        console.log( "document loaded" );
        var url = "http://127.0.0.1:5000/get_nh_names"  ; 
        $.get(url,function(data, status) {
            console.log("got response for get_nh_names request");
            if(data) {
                var nh_names = data.nh_names;
                var uineighbourhood = document.getElementById("uineighbourhood");
                $('#uineighbourhood').empty();
                for(var i in nh_names) {
                    var opt = new Option(nh_names[i]);
                    $('#uineighbourhood').append(opt);
                }
            }
        });
        console.log( "document loaded" );
        var url = "http://127.0.0.1:5000/get_rt_names"  ; 
        $.get(url,function(data, status) {
            console.log("got response for get_rt_names request");
            if(data) {
                var rt_names = data.rt_names;
                var uiroomtype = document.getElementById("uiroomtype");
                $('#uiroomtype').empty();
                for(var i in rt_names) {
                    var opt = new Option(rt_names[i]);
                    $('#uiroomtype').append(opt);
                }
            }
        });
    }
        window.onload = onPageLoad;

 