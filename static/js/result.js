let point = sessionStorage.getItem("point");
if (point >= 40){
    document.getElementById("set-image").innerHTML = `<img src="/static/img/congrats.png" class="img-fluid">`;
    document.getElementById("score").innerHTML += `<h4 class="text-col fw-bolder fst-italic">Congratulations You have passed the test.
                                                <br> You have score ${point} out of 100.<br>Try out some more test.</h1>`;
}
else{
    document.getElementById("set-image").innerHTML = `<img src="/static/img/sad1.png" class="img-fluid mt-5">`;
    document.getElementById("score").innerHTML += `<h4 class="text-col fw-bolder fst-italic"> Sorry to say you have failed the test.
                                                        <br>You have score ${point} out of 100.<br>Try more hard Next Time</h1>`;
}

