// ==========================================
// DELETE CONFIRMATION
// ==========================================

function confirmDelete() {

    return confirm(
        "Are you sure you want to delete this task?"
    );

}


// ==========================================
// PAGE LOADED
// ==========================================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        console.log(
            "Personal Task Management System loaded successfully."
        );


        // ======================================
        // AUTOMATICALLY HIDE FLASH MESSAGES
        // ======================================

        const messages =
            document.querySelectorAll(
                ".flash-message"
            );


        messages.forEach(function (message) {

            setTimeout(function () {

                message.style.opacity = "0";

                message.style.transition =
                    "opacity 0.5s ease";


                setTimeout(function () {

                    message.remove();

                }, 500);

            }, 3000);

        });


    }
);