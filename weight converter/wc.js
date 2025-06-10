let kgRef = document.getElementById("kg");
let lbsRef = document.getElementById("lbs");

let convertFromKg = () => {
    let kg = kgRef.value;
    lbsRef.value = (kg * 2.205).toFixed(2);
};

let convertFromLbs = () => {
    let lbs = lbsRef.value;
    kgRefRef.value = (lbs / 2.205).toFixed(2);
};

kgRef.addEventListener("input", convertFromKg);
lbsRef.addEventListener("input", convertFromLbs);


let button = document.getElementById('btn');

button.addEventListener('click', convertFromKg);
button.addEventListener('click', convertFromLbs);