
// var dropFunc = function(event) {
//     var dorp = document.getElementById("mydropdown");

//         if (this.dorp.className.contains("hidden")){
//             this.dorp.className = "dropdown-content";
//         } 
//         else {
//             this.dorp.className += " hidden";

//         }
// };

function dropFunc(event) {
    var drop = document.getElementById("mydropdown");

    if (drop.classList.contains("hidden")) {
        drop.className = "dropdown-content";
    } else {
        drop.className += " hidden";
    }
}

function getById(id) {
    return document.getElementById(id);
}

window.addEventListener("load", function() {

    // document.getElementById("dropdownbtn").onclick = dropFunc();
    // document.onclick =  dropFunc();

    getById("dropdownbtn").addEventListener("click", dropFunc);
    document.addEventListener("click", dropFunc);
    
});