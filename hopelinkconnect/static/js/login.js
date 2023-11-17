    var n = 2;
    var card = document.getElementById("card");
    var log = document.getElementById("Login");
    var logh = document.getElementById("logh");
    var reg = document.getElementById("Register");
    var regh = document.getElementById("regh");
    var footer = document.getElementById("footer");
    var p = document.getElementById("p")
    var l = 1;
    var r = 0;


    function login() 
    {
        if(l==0)
        {
          
        card.style.animationName = "spin-b";
        card.style.animationDuration = "2s";
        card.style.animationDirection = "linear"
        card.style.animationIterationCount = "1";
       
        logh.style.animationName = "rotate360-l";
            logh.style.animationDuration = "2s";
            logh.style.animationDirection = "linear"
            logh.style.animationIterationCount = "1";
            logh.style.animationFillMode = "forwards";
            logh.style.opacity = "1";
           
            regh.style.animationName="rotate360-b-r";
            regh.style.animationDuration = "2s";
            regh.style.animationDirection = "linear"
            regh.style.animationIterationCount = "1";
            regh.style.animationFillMode = "forwards";
        
      
        setTimeout(codingCourse, 1000);

        function codingCourse() 
        {
           
            
            footer.style.display = "flex";
            log.style.display = "flex";
            regh.style.display = "flex";
            reg.style.display = "none";
            card.style.backgroundColor = "rgba(15,23,43)";
            card.style.boxShadow = "0px 0px 1000px 10px rgb(15,23,43)";
        }
        l=1;
        r=0;
        }
    }
    
    function register() 
    {
        if(r==0)
        {
            card.style.animationName = "spin";
        card.style.animationDuration = "2s";
       
       card.style.animationIterationCount = "1";
     
       logh.style.animationName = "rotate360-b-l";
            logh.style.animationDuration = "2s";
            logh.style.animationDirection = "linear"
            logh.style.animationIterationCount = "1";
            logh.style.animationFillMode = "forwards";
            
          
            regh.style.animationName = "rotate360-r"
            regh.style.animationDuration = "2s";
            regh.style.animationDirection = "linear"
            regh.style.animationIterationCount = "1";
            regh.style.animationFillMode = "forwards";
      
        setTimeout(codingCourse, 1000);

        function codingCourse() 
        {
          
         
            footer.style.display = "none";
            log.style.display = "none";
            regh.style.display = "flex";
            reg.style.display = "flex";
            card.style.backgroundColor = "rgba(255, 55, 0, 0)";
            card.style.boxShadow = "0px 0px 1000px 2px rgb(183, 183, 183)";
      
                  
     
       
        }
        l=0;
        r=1;
     
        }
    }
  