function move_disks(n, source, auxillary, destination) {
    if (n === 1) {
        console.log(`Move Disk ${n} from ${source} to ${destination}`)
        return
    }
    move_disks(n - 1, source, destination, auxillary)
    console.log(`Move Disk ${n} from ${source} to ${destination}`)
    move_disks(n - 1, auxillary, source, destination)
}

move_disks(4, 'A', 'B', 'C')