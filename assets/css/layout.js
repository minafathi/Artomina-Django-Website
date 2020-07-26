

$(document).ready(function(){

    $('.namebox').hide()
    $('.colorpencil').hide()
    $('.oilcolor').hide()
    $('.sofal').hide()
    $('.tshert').hide()
    $('.boom').hide()



    $(function(){
		$('a.nav-link').click(function(){
			$(this).parent().addClass('active').siblings().removeClass('active')	
		})
	})	
    
    
    // NavBar-------------------------------------------------------
    $('button.navbar-toggler').click( function(){
        $('.navbar-collapse').toggle();
    });
    
    $('#navbarDropdownMenuLink').click(function(){
        $('.dropdown-menu').toggle();
    }); 

    $('.nav-link').click(function(){
        $('.navbar-collapse').toggle();
  
    })

    $('.notnow').click(function(){
        alert('در حال حاظر این آیتم غیرفعال میباشد!')
    })
    // Collection---------------------------------------------------
    // ----------- Portrait --------------------------------------
    $('.homeportrate1').mouseover(function(){
        $(this).addClass('darken_img');
        $('.namebox1').show()

    })
    $('.homeportrate1').mouseout(function(){
        $(this).removeClass('darken_img');
        $('.namebox1').hide()
    })
    // ----------- Boom --------------------------------------
    $('.homeportrate2').mouseover(function(){
        $(this).addClass('darken_img');
        $('.namebox2').show()

    })
    $('.homeportrate2').mouseout(function(){
        $(this).removeClass('darken_img');
        $('.namebox2').hide()
    })
    // ----------- Parche --------------------------------------
    $('.homeportrate3').mouseover(function(){
        $(this).addClass('darken_img');
        $('.namebox3').show()

    })
    $('.homeportrate3').mouseout(function(){
        $(this).removeClass('darken_img');
        $('.namebox3').hide()
    })
    // ----------- Sofal --------------------------------------
    $('.homeportrate4').mouseover(function(){
        $(this).addClass('darken_img');
        $('.namebox4').show()

    })
    $('.homeportrate4').mouseout(function(){
        $(this).removeClass('darken_img');
        $('.namebox4').hide()
    })
    
    // Prices --------------------------------------------------------
    $('#archol').click(function(){
        $('.archol').toggle();
            
    }); 
    $('#colorpencil').click(function(){
        $('.colorpencil').toggle();
    }); 
    $('#oilcolor').click(function(){
        $('.oilcolor').toggle();
    }); 
    $('#sofal').click(function(){
        $('.sofal').toggle();
    }); 
    $('#tshert').click(function(){
        $('.tshert').toggle();
    }); 
    $('#boom').click(function(){
        $('.boom').toggle();
    }); 
 


})

