function redirectToConsultation() {
    window.location = "/consult_page";
}

function redirectToIntance() {
    window.location = "/instances_page";
}


document.getElementById('activityForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    alert("Actividad registrada exitosamente.");
    redirectToConsultation(); 
});
