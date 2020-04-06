'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the diagonalDifference function below.
function diagonalDifference(arr) {
    diag1 = 0;
    diag2 = 0;
    n = arr.length;
    console.log(n)
    for(i=0; i<n; i++){
        diag1 += arr[i][i];
        diag2 += arr[i][n-i-1];
    }
    return Math.abs(diag1 - diag2);

}

function main() {
    const ws = fs.createWriteStream('output');
    console.log('hello')
    const n = parseInt(readLine(), 10);
    console.log(n)
    let arr = Array(n);

    for (let i = 0; i < n; i++) {
        arr[i] = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    const result = diagonalDifference(arr);

    ws.write(result + '\n');

    ws.end();
}

