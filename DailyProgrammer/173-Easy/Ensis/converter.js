if (process.argv.length < 3)
    console.warn("Usage: node converter.js '<N> <unit> to <unit>'") || process.exit();

var res = (/^([0-9]+(?:\.[0-9]+)?) ([a-zA-Z ]+) to ([a-zA-Z ]+)$/.exec(process.argv[2]));

if (!res)
    console.warn("Usage: node converter.js '<N> <unit> to <unit>'") || process.exit();

var dist = {"metres":1, "inches":0.0254, "miles":1609.344, "attoparsecs":0.0308567758};
var mass = {"kilograms":1000, "pounds":453.592, "ounces":28.3495, "hogsheads of beryllium":440700};

var n = parseFloat(res[1]);
var u1 = res[2].trim().toLowerCase();
var u2 = res[3].trim().toLowerCase();
var unit = dist[u1] && dist[u2] ? dist : mass[u1] && mass[u2] ? mass : null;

process.stdout.write(n + " " + u1);
if (unit)
    console.log(" is " + (n * unit[u1] / unit[u2]).toFixed(4) + " " + u2);
else
    console.log(" cannot be converted to " + u2);
