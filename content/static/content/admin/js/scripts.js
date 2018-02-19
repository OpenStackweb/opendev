jQuery(function($){
	$('#slug-form').submit(function(e) {
		window.location.replace($('#header-select').val());
		return false;
	});
});

jQuery(function($){
    var event_name = $('#header-select option:selected, #header-select-text').text();
    $(".app-content, .app-menus").find("caption a").each(function(){
        $(this).text(event_name + " " + $(this).text());
    });
    $(".dashboard .app-content tr:contains('~')").each(function(){ 
        var $this = $(this);            
        $this.addClass("separator");
        $this.find("th").html($this.find("th a").text().replace(' ~', ''));
        $this.find("td a").remove();
    });
});