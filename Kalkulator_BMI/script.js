let usia, berat, tinggi, tinggi_m, bmi, keterangan, hasil;

function hitung(){
    usia = document.getElementById('age').value;
    berat = document.getElementById('weight').value;
    tinggi = document.getElementById('height').value;
    
    
    console.log(berat);
    tinggi_m = tinggi /100;
    bmi = berat / (tinggi_m * tinggi_m)
    hasil = bmi.toFixed(2);
    document.getElementById('hasil').innerText = hasil;

    if (hasil < 18.5) {
        keterangan = "Kekurangan Berat Badan";
    } else if (18.5 <= hasil <= 24.9) {
        keterangan = "Normal";
    } else if (25 <= hasil <= 29.9) {
        keterangan = "Kelebihan Berat Badan";
    } else if (hasil >= 30) {
        keterangan = "Obesitas";
    } else {
        keterangan = "Salah";
    }

    document.getElementById('ket').innerText = keterangan;
 };