/*
    a12847
*/

// Type assertion function with custom error
// function assert(condition: unknown, message: string): asserts condition {
//     if (!condition) {
//         throw new Error(message);
//     }
// }

const input: string[] = require("fs").readFileSync("/dev/stdin")
    .toString().trim().split("\n");

let [N, M] = input[0].split(" ").map(Number); // as [number, number];
const A = input[1].split(' ').map(Number); // as number[];

// assert(A.length === N, "wrong length");

let profit = A.slice(0, M).reduce((acc, cur) => acc+cur, 0);
let max_profit = profit;

for (let k=M; k<N; k++) {
    profit = profit + A[k] - A[k-M];
    if (max_profit < profit) max_profit = profit;
}

console.log("%d", max_profit)


/*
pr=12847
run=(npx ts-node a${pr}.ts)
echo '5 3\n10 20 30 20 10' | $run
# 70


*/

