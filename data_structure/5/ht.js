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

// node没有基础set类型，用{}伪装成set即可
console.log("\nnode没有set类型，用{}伪装成set即可")
let b = [1, "1234x", 1, 2, 3, 4, 5, 5, "1234x"];
let unique = {};
for (x of b) {
    if (!(x in unique)) {
        unique[x] = x;
    }
}
for (x in unique) {
    console.log(x);
}