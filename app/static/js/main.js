// ===== PAGE LOADER ANIMATION =====
window.addEventListener("load", () => {
    document.body.classList.add("fade-in");
});


// ===== FILE UPLOAD NAME DISPLAY =====
const fileInput = document.querySelector('input[type="file"]');

if (fileInput) {
    fileInput.addEventListener("change", function () {
        if (this.files.length > 0) {
            alert("Selected File: " + this.files[0].name);
        }
    });
}


// ===== BUTTON LOADING EFFECT =====
const buttons = document.querySelectorAll(".btn-custom");

buttons.forEach(btn => {
    btn.addEventListener("click", function () {
        btn.innerHTML = "Processing...";
        btn.disabled = true;
    });
});


// ===== SEARCH FILTER (JOBS) =====
function filterJobs() {
    let input = document.getElementById("jobSearch");
    let filter = input.value.toLowerCase();
    let cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        let text = card.innerText.toLowerCase();
        if (text.includes(filter)) {
            card.style.display = "";
        } else {
            card.style.display = "none";
        }
    });
}


// ===== SCROLL TO TOP BUTTON =====
let topBtn = document.createElement("button");
topBtn.innerHTML = "⬆";
topBtn.style.position = "fixed";
topBtn.style.bottom = "20px";
topBtn.style.right = "20px";
topBtn.style.padding = "10px 15px";
topBtn.style.border = "none";
topBtn.style.borderRadius = "50%";
topBtn.style.background = "#ff6ec4";
topBtn.style.color = "white";
topBtn.style.display = "none";

document.body.appendChild(topBtn);

window.onscroll = function () {
    if (document.documentElement.scrollTop > 200) {
        topBtn.style.display = "block";
    } else {
        topBtn.style.display = "none";
    }
};

topBtn.onclick = function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
};


// ===== MATCH % ANIMATION =====
let progressBars = document.querySelectorAll(".progress-bar");

progressBars.forEach(bar => {
    let width = bar.style.width;
    bar.style.width = "0";

    setTimeout(() => {
        bar.style.width = width;
    }, 500);
});