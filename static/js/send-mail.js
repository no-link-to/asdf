window.onload = function() {

    let button = document.getElementById('sendButton');

    button.addEventListener('click', function() {

        let name_input = document.getElementById('nameInput').value;
        let phone_input = document.getElementById('phoneInput').value;
        let mail_input = document.getElementById('mailInput').value;
        let question_input = document.getElementById('questionInput').value;

        if (name_input === '' || phone_input === '' || mail_input === '' || question_input === ''
            || name_input === null || phone_input === null || mail_input === null || question_input === null) {

            alert('Пожалуста заполните все поля')

        } else {

            document.getElementById('nameInput').value = '';
            document.getElementById('phoneInput').value = '';
            document.getElementById('mailInput').value = '';
            document.getElementById('questionInput').value = '';

        }
    })
}