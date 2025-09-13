import LinkedList from "./ll.js";

const head = new LinkedList(10)

head.addNB(20).addNB(30).addNB(40).addNE(5).reverse().print()
console.log('length: ' + head.length)
