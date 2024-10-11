function redirectToConsultation() {
    window.location.href = "consult.html";
}


document.getElementById('activityForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    alert("Actividad registrada exitosamente.");
    redirectToConsultation(); 
});
