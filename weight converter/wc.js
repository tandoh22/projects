let kgRef = document.getElementById("kg");
let lbsRef = document.getElementById("lbs");

let convertFromKg = () => {
    let kg = kgRef.value;
    lbsRef.value = (kg * 2.205).toFixed(2);
}

let convertFromLbs = () => {
    
    kgRefRef.value = (lbs / 2.205).toFixed(2);
}