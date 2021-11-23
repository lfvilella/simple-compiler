# Running locally

### Install and generate parser

```
$ npm install -g pegjs
$ pegjs -o arithmetics-parser.js arithmetics.pegjs
```

### Running parser
```
$ vim main.js
```
```
const arithmeticsParser = require("./arithmetics-parser");
console.log(arithmeticsParser.parse('2+2*2'))
```
```
node main.js
```
