
$('head').append('<style type="text/css">body.page-membership-about #content {visibility:hidden;} body.page-membership-about #content.has-js {visibility:visible}</style>');

$(document).ready(function() {
  
  createDropDownMenus();
  
  /*  Homepage Slideshow  */
  
  if($("#block-views-homepage_callouts-block_1").length > 0){
    if($("#block-views-homepage_callouts-block_1").find('.views-item').length > 1) {
      makeSlideshow("#block-views-homepage_callouts-block_1");
    }
  }
  
  /*  Announcements & Upcoming Events  */
  
  if($("#block-views-homepage_events-block_1").length > 0 && $("#block-views-homepage_announcements-block_1").length > 0){
    $("#block-views-homepage_announcements-block_1, #block-views-homepage_events-block_1").wrapAll("<div class='tab-group' id='header-tab-group'></div>");
    makeTabGroup("#header-tab-group");
  }
  
  /*  Recent Blog & Forum Posts  */
  
  if($(".front").length > 0){
    if($("#block-views-blog-block_1").length > 0 && $("#block-views-forum_post_list-block_1").length > 0){
      $("#block-views-blog-block_1, #block-views-forum_post_list-block_1").wrapAll("<div class='tab-group' id='blog-forum-tab-group'></div>");
      makeTabGroup("#blog-forum-tab-group");
    }
  }
  
  //  Replace lock icon with class on link
  
  $("img[src='/images/lock.gif']").each(function(){
    var p = $(this).parent();
    if(!p.is("a")){
      p = p.find("a");
    }
    p.addClass("restricted-content");
    p.wrapInner("<span></span>");
    $(this).remove();
  })
  
  //  Strip empty p tags
  
  if($(".node-type-campus-profile").length > 0){
    $("#content p").filter( function() {
        return $.trim($(this).text()) == '';
    }).remove();
  }
  
  //  Clean up filters
  //  Case Studies
  /*
  if($(".case-studies-search-page").length > 0){
    collapseFilters(".case-studies-search-page");
  }
  */
  //  Student Research
  if($(".filters").length > 0){
    collapseFilters(".filters");
  }
  
  //  Membership Description
  if($("#block-views-membership_benefits-block_2").length > 0){
    setupMembershipDetails();
    $("#content").addClass("has-js");
  }
  
  //  Blog Topics
  if($("#block-views-taxblock2-block_1").length > 0){
    $("#block-views-taxblock2-block_1 h2.block-title").addClass("collapsible").wrapInner("<a class='topic-toggle collapsed' href='#'></a>");
    $("#block-views-taxblock2-block_1 h2.block-title a").click(function(){
      $(this).toggleClass("collapsed");
      $("#block-views-taxblock2-block_1 ul.views-items").slideToggle();
      return false;
    });
    $("#block-views-taxblock2-block_1 ul.views-items").slideToggle(0);
  }
  
});

slidecounter = 0;

function makeSlideshow(t){
  var slideshow = $(t);
  if($("ul.views-items li.views-item", slideshow).length > 1){
  
    slideshow.addClass("slideshow");
  
    slideshow.find("ul.views-items").before("<a href='#' class='slide-previous'>Previous</a>");
    slideshow.find("a.slide-previous").click(function(){
      switchSlide(t, -1);
      return false;
    });
    slideshow.find("ul.views-items").before("<a href='#' class='slide-next'>Next</a>");
    slideshow.find("a.slide-next").click(function(){
      switchSlide(t, 1);
      return false;
    });
  
    $("ul.views-items li.views-item", slideshow).each(function(index){
      if(index == 0){
        $(this).addClass("current");
        slideshow.height($(this).height());
        slideshow.width($(this).width());
        $(this).fadeIn("fast");
      }
    });
  }
  
  setTimeout('checkCounter()', 1000);
  
}

function checkCounter(){
  slidecounter += 1;
  var wait = 10; //  Number of seconds to wait
  if(slidecounter >= wait){
    switchSlide("#block-views-homepage_callouts-block_1", 1);
  }
  setTimeout('checkCounter()', 1000);
}

function switchSlide(t, direction){
  slidecounter = 0;
  var slideshow = $(t);
  if(!slideshow.hasClass("switching")){
    
    slideshow.addClass("switching");

    var slides = $("ul.views-items li.views-item", slideshow);
    var totalSlides = slides.length;
    var currentSlide = 0;
    slides.each(function(index){
      if($(this).hasClass("current")){
        currentSlide = index;
      }
    })
  
    var nextSlide = currentSlide + direction;
    if(nextSlide < 0){
      nextSlide = totalSlides - 1;
    }else if (nextSlide >= totalSlides){
      nextSlide = 0;
    }
    
    slides.eq(currentSlide).removeClass("current");
    slides.eq(currentSlide).addClass("fading");
    slides.eq(nextSlide).addClass("current");
    slides.eq(nextSlide).css("visibility", "visible");
    slides.eq(nextSlide).css("display", "block");
    slides.eq(currentSlide).fadeOut(1000, function(){
      slideshow.removeClass("switching");
      $(this).removeClass("fading");
    });
        
        /*
    slides.each(function(index){
      if($(this).hasClass("current")){
        $(this).removeClass("current");
        $(this).addClass("fading");
        $(this).fadeOut(1000, function(){
          slideshow.removeClass("switching");
          $(this).removeClass("fading");
        });
      }else if(index == nextSlide){
        $(this).addClass("current");
        $(this).css("visibility", "visible");
        $(this).css("display", "block");
      }
    });
    */
  }
}


function makeTabGroup(t){
  
  var group = $(t);
  
  group.prepend("<ul class='display-tabs'></ul>");
  group.find('h2.block-title').each(function(index){
    group.find('ul.display-tabs').append("<a href='#' class='tab" + index + "'>" + $(this).text() + "</a>");
  });
  
  group.find('ul.display-tabs a').each(function(index){
    $(this).click(function(){
      switchTab(t, index);
      return false;
    })
    $(this).wrap("<li></li>");
  });
  
  switchTab(t, 0);
}

function switchTab(t, i){
  showItemAtIndex(i, $(t).find('.block'));
  setActiveAtIndex(i, $(t).find('ul.display-tabs li'));
}

function showItemAtIndex(i, items){
  items.each(function(index){
    if(index == i){
      $(this).css({display:"block", visibility:"visible"});
    }else{
      $(this).css({display:"none", visibility:"hidden"});
    }
  })
}

function setActiveAtIndex(i, items){
  items.each(function(index){
    var l = $(this);
    if(index == i){
      if(!l.hasClass("active")){
        l.addClass("active");
        l.find('a').addClass("active");
      }
    }else{
      if(l.hasClass("active")){
        l.removeClass("active");
        l.find('a').removeClass("active");
      }
    }
  });
}

function collapseFilters(t) {
  var search = $(t).find('.widget-filter-keys');
  if(search.length > 0){
    $(t).addClass("advanced");
    search.append("<a href='#' class='advanced-search-link'>Advanced Search</a>");
    $('.advanced-search-link').click(function(){
      $(this).toggleClass("advanced-close");
      $(".advanced-filters").slideToggle();
      return false;
    })
    // Add a reset button to our forms
    $(t).find(".views-exposed-widget .form-submit").after('<a class="button-small" id="edit-reset" href="#">Reset Form</a>');
    $(t).find("#edit-reset").click(function(){
      resetForm(t);
      return false;
    });
  
    var filters = $(t).find(".views-exposed-widget").not('.widget-filter-keys').not(".views-exposed-widget:last");
    filters.wrapAll("<div class='advanced-filters'></div>");
    $(".advanced-filters").css("display","none");
    filters.each(function(){
      var $this = $(this);
      $this.addClass("filter-section");
      $this.children(".views-widget").css("display", "none");
      $this.children("label").addClass("section-label");
      $this.children("label").click(function(){
        toggleFilters($(this));
        return false;
      });
    })
  }
  //toggleFilters(filters, filters.eq(0).children("label"));
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
  if($label.hasClass("section-open")){
    $label.removeClass("section-open");
    $widget.css("display", "none");
  }else{
    $label.addClass("section-open");
    $widget.css("display", "block");
  }
  
  //$(".advanced-filters").height(Math.max(target.parent().children(".views-widget").height() + 40, $(".advanced-filters").height()));
  //target.parent().children(".views-widget").height($(".advanced-filters").height() - 40);
}

function resetForm(t){
  // Clear all of the text inputs
  $(t).find(".views-exposed-widget input.form-text").each(function(n,element) {
    $(element).val('');
  });

  // The first select is a taxonomy selector, let's select them all
  $(t).find(".views-exposed-widget:first .views-widget select option").each(function(n,element) { 
    $(element).attr('selected', 'selected');
  });

  // Set any of the exposed filter options back to the first option
  $(t).find(".views-exposed-widget select option:first-child").attr('selected', 'selected');

  // Submit the cleared form to reset the page to all items visible
  $(t).find("form").submit();
};

function createDropDownMenus(){
  var sitemap = $(".menu-block-3").children(".menu").children("li");
  var nav = $("#navigation ul.primary-links li");
  nav.each(function(index){
    sitemap.eq(index).children("ul.menu").clone().appendTo($(this));
    $(this).hover(
      function(){
        $(this).children(".menu").css({
          display: "block",
          visibility: "visible"
        })
      },
      function(){
        $(this).children(".menu").css({
          display: "none",
          visibility: "hidden"
        })
      })
  })
}

var scrollPosition = 0;
var scrolledOnce = false;

function setupMembershipDetails(){
  
  var currentType = 0;
  var currentSection = 0;
  var currentHash = $(location).attr('hash');
  
  var $view = $("#block-views-membership_benefits-block_2");
  $view.addClass("membership-collapsed");
  $("<ul class='membership-tabs'></ul>").prependTo($view);
  getMembershipTypes($view).each(function(index){
    var $section = $(this);
    
    //  Create Type Navigation
    
    var $title = $(this).find("h3.node-title").text();
    $("<a href='#'>" + $title + "</a>").click(function(){
      switchTypeTab($view, index, 0);
      return false;
    }).appendTo($view.children('.membership-tabs')).wrapAll("<li class='type-" + index + "'></li>");
    
    //  Create Section Navigation
    
    $("<ul class='section-tabs'></ul>").prependTo($section);
    getMembershipSections($section).each(function(index2){
      if("#" + $(this).attr("id") == $(location).attr('hash')){
        currentType = index;
        currentSection = index2;
      }
      var $title = $(this).children("h2").text();
      var $hash = $(this).attr("id");
      $("<a href='#" + $hash + "'>" + $title + "</a>").click(function(event){
        if($(this).hasClass("current")){
          return false;
        }
        event.preventDefault();
        //$section.addClass("switchingTabs");
        //setTimeout( "removeSwitchingTabsClass()", 20);
        //currentHash = $(this).hash;
        window.location.hash = this.hash;
        switchSectionTab($section, index2);
        return false;
      }).appendTo($section.children('.section-tabs')).wrapAll("<li class='section-" + index2 + "'></li>");
    })
    
    //  Hide all but the first Section
    /*
    if(index == currentType){
      switchSectionTab($section, currentSection);
    }else{
      switchSectionTab($section, 0);
    }
    */
  });
  switchTypeTab($view, currentType, currentSection);
  //$(location).attr('hash') = $(location).attr('hash');
}

function removeSwitchingTabsClass(){
  $(".switchingTabs").removeClass("switchingTabs");
  //$.scrollTo(scrollPosition, 0);
}

function getMembershipTypes(view){
  return view.find("ul.views-items").children("li.views-item");
}

function getMembershipSections(type){
  return type.find(".fieldgroup");
}

function switchTypeTab(view, tab, section){
  var currentTab = 0;
  view.find("ul.membership-tabs li a").each(function(index){
    $(this).removeClass("current");
    if(index == tab){
      currentTab = index;
      $(this).addClass("current");
    }
  })
  getMembershipTypes(view).each(function(index){
    $(this).css({
      display:"none",
      visibility:"hidden"
    })
    if(index == currentTab){
      switchSectionTab($(this), section);
      $(this).css({
        display:"block",
        visibility:"visible"
      })
    }
  })
}

function switchSectionTab(section, tab){
  var currentTab = 0;
  //scrollPosition = $.scrollTop();
  section.find("ul.section-tabs li a").each(function(index){
    $(this).removeClass("current");
    if(index == tab){
      currentTab = index;
      if(scrolledOnce){
        window.location.hash = this.hash;
      }
      $(this).addClass("current");
    }
  })
  getMembershipSections(section).each(function(index){
    $(this).css({
      display:"none",
      visibility:"hidden"
    })
    if(index == currentTab){
      $(this).css({
        display:"block",
        visibility:"visible"
      })
    }
  })
  
  if(!scrolledOnce){
    scrolledOnce = true;
    $.scrollTo(0, 0);
  }
}
