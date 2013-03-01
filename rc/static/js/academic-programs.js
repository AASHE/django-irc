$(document).ready(function() {
	 
	// Tabs
	$('.tab-wrapper').find('.tab').hide().end().find('.tab:first').show();
	$('.program-nav-tabs').find('a:first').addClass('active');
	$('.program-nav-tabs a').click(function(e){
		e.preventDefault();
		if($($(this).attr('href')).is(':hidden')){
			$(this).closest('.tab-wrapper').find('.tab').hide();
			$($(this).attr('href')).fadeIn();
			$(this).closest('.tab-wrapper').find('.program-nav-tabs a').removeClass();
			$(this).addClass('active');
			if($($(this).attr('href')).find('.carousel').length){
				$($(this).attr('href')).find('.carousel').trigger('configuration',['height','variable']);
			}
		}
	});

  if($(".search-wrapper").length > 0) {
    collapseFilters(".search-wrapper");
  }

});

function resetForm(t){
  // Clear all of the text inputs
  $(t).find(".fieldWrapper input.form-text").each(function(n,element) {
    $(element).val('');
  });

  // Clear all of the text inputs
  $(t).find(".query input.form-text").each(function(n,element) {
    $(element).val('');
  });

  // clear selects
  $(t).find(".fieldWrapper select option").each(function(n,element) { 
    $(element).attr('selected', false);
  });

  // Set any of the exposed filter options back to the first option
  //$(t).find(".views-exposed-widget select option:first-child").attr('selected', 'selected');

  // Deselect all selected elements
  $(t).find(".fieldWrapper .views-widget select option").each(function(n,element) {
    $(element).attr('selected', false);
  });

  // Submit the cleared form to reset the page to all items visible
  $(t).find("form").submit();
};

function collapseFilters(t) {
  var search = $(t).find('.search-form');
  if(search.length > 0){
    $(t).addClass("advanced");
    $(t).find(".search-form #first-submit").after("<div id='advanced-search-wrapper'><a href='#' class='advanced-search-link advanced-open'>Advanced Search</a></div>");
    $('.advanced-search-link').click(function(){
      $(this).toggleClass("advanced-close");
      $(this).toggleClass("advanced-open");
      $(".advanced-filters").slideToggle();
      return false;
    })
    // Add a reset button to our forms
    $(t).find(".search-form #second-submit").after('<div id="reset-form-wrapper"><a class="button" id="edit-reset" href="#">Reset Form</a></div>');
    $(t).find("#edit-reset").click(function(){
      resetForm(t);
      return false;
    });

    var filters = $(t).find(".fieldWrapper");
    // filters.wrapAll("<div class='advanced-filters'></div>");
    $(".advanced-filters").css("display","none");
    filters.each(function(){
      var $this = $(this);
      $this.addClass("filter-section");
      $this.children("label").addClass("section-label");
      $this.children("label").click(function(){
        toggleFilters($(this));
        return false;
      });
    })
  }
  //toggleFilters(filters, filters.eq(0).children("label"));

  // show advanced search if field hase value
  $(".fieldWrapper select").each( function(n,element){
  if ($(element).val()!='') {
    $(element).parents().show();
    // $(element).parents().siblings(".views-operator").show();
    return true;
  }
  });
}

function toggleFilters(target){
  /*
  filters.each(function(){
    var $this = $(this);
    var $label = $this.children("label");
    var $widget = $this.children(".views-widget");
    if($label.hasClass("section-open") && $label == target.parent().children("label")){
      $label.removeClass("section-open");
      $widget.css("display", "none");
    }
  });
  target.parent().children("label").addClass("section-open");
  target.parent().children(".views-widget").css("display", "block");
  */

  $label = target.parent().children("label");
  $widget = target.parent().children(".views-widget");
  $operator = target.parent().children(".views-operator");
  if($label.hasClass("section-open")){
    $label.removeClass("section-open");
    $widget.css("display", "none");
    $operator.css("display", "none");
  }else{
    $label.addClass("section-open");
    $widget.css("display", "block");
    $operator.css("display", "block");
  }

  //$(".advanced-filters").height(Math.max(target.parent().children(".views-widget").height() + 40, $(".advanced-filters").height()));
  //target.parent().children(".views-widget").height($(".advanced-filters").height() - 40);
}

