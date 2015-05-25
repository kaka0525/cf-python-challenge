var inItemText = document.getElementById("inItemText");
inItemText.focus();
$( inItemText ).keyup(function(event) {
    var listItem
    if (event.which == 13) { // on 'enter'
        var itemText = $.trim(inItemText.value);
        if (itemText == "" || itemText == "Finish" || !itemText) {
            return false;
        } else {
            addNewItem(document.getElementById("todoList"), itemText);
            $(inItemText).val('');
        }
    }
});

function addNewItem(list, itemText){
    var listItem = document.createElement("li");
    listItem.innerHTML = itemText;
    $(listItem).click(function() {
        $(this).remove();
    });
    list.insertBefore(listItem, list.firstChild);
}

