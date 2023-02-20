const name = 'Hong-gil-dong';
function foo() {
    this.name = "John-doe";
    this.name = name.substring(0, 4);

    console.log(name)
}
