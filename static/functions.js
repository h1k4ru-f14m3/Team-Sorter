export let potCount = 1;
export let latestTeamID = 1;

document.addEventListener('DOMContentLoaded', function() {
    function removeBtnListener(removeBtn) {
        removeBtn.addEventListener('click', function(event) {
            event.preventDefault();
            if (potCount === 1) {
                return;
            }

            let parent_element = removeBtn.parentElement;
            parent_element.classList.add('fadeOut');
            parent_element.addEventListener('animationend', function(){
                parent_element.remove();
            });
            potCount -= 1;
        });
    }

    let btn_add = document.querySelector('#addMore');
    let btns = document.querySelector('.btns');
    let form = document.querySelector('form');

    removeBtnListener(form.querySelector('.removeDiv'));

    btn_add.addEventListener('click', function(event) {
        event.preventDefault();
        const to_copy = document.querySelector('form .pots');
        const to_paste = to_copy.cloneNode(true);
        const btn_remove = to_paste.querySelector('.removeDiv');

        potCount += 1;
        latestTeamID += 1;

        to_paste.id = `pot_${latestTeamID}`;
        to_paste.querySelector('input').value = `Pot-${potCount}`;

        removeBtnListener(btn_remove);
        form.insertBefore(to_paste, btns);
    });
});