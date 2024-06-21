// sendMail() function
// code taken from emailjs tutorial

function sendMail(contactForm) {
    emailjs.send("service_igy3jhp", "template_9gqao0e", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "contactsummary": contactForm.contactsummary.value
    })
    .then(
        function(response) {
            alert("Email sent successfully!");
            console.log("YES SUCCESS", response);
            window.location.href = "/";
            return true;
        },
        function(error) {
            alert("Email failed-please try again");
            console.log("OH NO!!!!", error);
        }
    );
    return false;
}