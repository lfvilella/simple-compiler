# Running

    make build
    make cmd


- Create Grammar.atg
- `$ java -jar Coco.jar Grammar.atg -o Output`
- `$ cd Output`
- Create a `Compiler.java` file (copy/paste an existing)
- `$ javac Parser.java Scanner.java Compiler.java`
- Create `Input.txt` file
- `$ java Compiler Input.txt`
