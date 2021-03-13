window.onload = function(){
    show(0);
}

let qtscount = 0;
let point = 0;
function qts_count(){
    qtscount++;
    show(qtscount);
}

function show(count){
    var data = get_data();
    let option = document.querySelectorAll("input.btn");
    for(let i = 0; i<option.length; i++)
    {
            option[i].classList.remove("disabled","btn-outline-success","text-success");
            option[i].classList.remove("disabled","btn-outline-danger","text-danger");
    }
    document.getElementById("btn_nxt").classList.add("disabled");
    document.getElementById("qts").innerHTML = data[count].qts;
    document.getElementById("btn-1").value = data[count].opt1;
    document.getElementById("btn-2").value = data[count].opt2;
    document.getElementById("btn-3").value = data[count].opt3;
    document.getElementById("btn-4").value = data[count].opt4;
    if (data.length == count+1){
        document.getElementById("btn_nxt").remove();
        document.getElementById("submit").innerHTML = '<button class="btn btn-primary mt-4 onclick="submit_page()" d-grid" type="submit" id="btn_submit">Submit</button>'
    }

}
var all_answer = [];
function check(btn){
    user_answer = document.getElementById(btn).value;
    all_answer.push(user_answer);
    nxt_button = document.getElementById("btn_nxt");
    submit_button = document.getElementById("btn_submit");
    if (nxt_button)
        {
            nxt_button.classList.remove("disabled");
        }
    if (submit_button)
       {
        submit_button.classList.remove("disabled");
       }

    var data = get_data();
    var answer = data[qtscount].answer;
    let option = document.querySelectorAll("input.btn");
    for(let i = 0; i<option.length; i++)
    {
        let val = option[i].value;
        if (val == answer)
            {
                option[i].classList.add("disabled","btn-outline-success","text-success");
            }
        else{
                option[i].classList.add("disabled","btn-outline-danger","text-danger");
            }
    }
    if (answer == user_answer){
        point+=10;
        sessionStorage.setItem("point",point);
    }
}


