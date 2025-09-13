class Node {

    data
    next

    constructor(data) {
        this.data = data
        this.next = null
    }
}


export default class LinkedList {

    head
    length

    constructor(data) {
        if (data) {
            this.head = new Node (data)
            this.length = 1
        }
        else {
            this.head = null
            this.length = 0
        }
    }

    // add node to the beginning
    addNB(data) {
        const newNode = new Node(data)
        newNode.next = this.head
        this.head = newNode
        this.length++
        return this
    }

    addNE(data) {
        const newNode = new Node(data)
        if (this.head === null) {
            this.head = newNode
            return this
        }
        let ptr = this.head

        while(ptr.next !== null) {
            ptr = ptr.next
        }
        ptr.next = newNode
        this.length++
        return this
    }

    reverse() {
        if (this.head === null) {
            return this
        }

        let current = null
        let after = this.head
        let temp

        while (after !== null) {
            temp = after.next
            after.next = current
            current = after
            after = temp
        }

        this.head = current
        return this
    }

    print() {
        let ptr = this.head

        while(ptr !== null) {
            if (ptr && ptr.next) process.stdout.write(`(${ptr.data}) -> `)
            else console.log(`(${ptr.data})`)
            ptr = ptr.next
        }
    }
}
