// function which calls onclick
function def()
{
 if(document.getElementById("num").value != "")
 {var elem = document.getElementById("num").value;
 var presult = primecheck(elem);
 // function for prime check
 function primecheck(a){
    var count = 0;
        for(var i=2;i<a;i++)
        {
       if(a%i == 0)
                {
                   count++;
                }
        }
        if(count == 0)
        {return 1;}
        else
        {return 0;}
        }
if(presult == 1)
  {
  document.getElementById("ite").innerHTML = "Prime Number";
  }
 else
 {
 document.getElementById("ite").innerHTML = "Not a Prime Number";
 }
modalfun();
  }
else
{
        alert("Please enter the Number");
}
}
function modalfun(){
         // Get the modal
var modal = document.getElementById('myModal');
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
//displays the modal with block
   modal.style.display = "block";

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
   if (event.target == modal) {
        modal.style.display = "none";
    }
  }
 }

