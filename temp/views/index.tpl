% rebase('layout.tpl', title='Home Page', year=year)


<div style='background-color:black;color:white;border-radius: 25px;'><h3 id='msgt' style="padding:1em"><br><br></h3></div>
{{!gauge[0]}}
{{!gauge[1]}}
<script>
setInterval(get_temp,5000);
function get_temp(){
    $.ajax({
        type: "GET",
        url: "/temp",
        success: function(d){
			if(d.text!="") $('#msgt').html(d.text);
			$('#tmp1').attr('data-value',d.t);
			$('#humid1').attr('data-value',d.h);
		}
    });
}
</script>


