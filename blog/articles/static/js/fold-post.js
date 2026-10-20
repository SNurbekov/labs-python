document.addEventListener("DOMContentLoaded", function() {
    // Находим все кнопки с классом fold-button
    var foldBtns = document.getElementsByClassName("fold-button");

    for (var i = 0; i < foldBtns.length; i++) {
        foldBtns[i].addEventListener("click", function(event) {
            // Находим родительский блок .one-post
            var postDiv = event.target.closest('.one-post');

            // Переключаем класс folded у родителя
            if (postDiv.classList.contains('folded')) {
                postDiv.classList.remove('folded');
                event.target.innerHTML = "свернуть";
            } else {
                postDiv.classList.add('folded');
                event.target.innerHTML = "развернуть";
            }
        });
    }
});