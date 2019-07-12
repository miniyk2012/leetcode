let a = [1, "1234x", 1, 2, 3, 4, 5, 5, "1234x"];

let c = {};

for (x of a) {
    if (x in c) {
        c[x] += 1;
    } else {
        c[x] = 1;
    }
}

for (inte in c) {
    console.log(inte, c[inte]);
}