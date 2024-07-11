## DFS && BFS

### Graph 1

start: A<br/>end: F

```mermaid
  block-beta
  columns 3
  A(("&nbsp;&nbsp;A&nbsp;&nbsp;")) space C(("<font color='cyan'>&nbsp;&nbsp;C&nbsp;&nbsp;</font>"))
  space space space
  B(("<font color='cyan'>&nbsp;&nbsp;B&nbsp;&nbsp;</font>")) space E(("<font color='cyan'>&nbsp;&nbsp;E&nbsp;&nbsp;</font>"))
  space space space
  D(("<font color='cyan'>&nbsp;&nbsp;D&nbsp;&nbsp;</font>")) space F(("&nbsp;&nbsp;F&nbsp;&nbsp;"))
  A-->C
  C-->E
  A-->B
  D-->F
  B-->D

  style A fill:black,stroke:lime,stroke-width:4px,color:lime
  style F fill:black,stroke:red,stroke-width:4px,color:red

  style B fill:black,stroke:cyan,stroke-width:4px,color:cyan
  style C fill:black,stroke:cyan,stroke-width:4px,color:cyan
  style D fill:black,stroke:cyan,stroke-width:4px,color:cyan
  style E fill:black,stroke:cyan,stroke-width:4px,color:cyan
```

`DFS: a,b,d,f,c,e`

`BFS: a,b,c,d,e,f`


### Graph 2

start: F<br/>end: K

```mermaid
  block-beta
  columns 5
  F(("&nbsp;&nbsp;F&nbsp;&nbsp;")) space G(("&nbsp;&nbsp;G&nbsp;&nbsp;")) space H(("&nbsp;&nbsp;H&nbsp;&nbsp;"))
  space space space space space
  I(("&nbsp;&nbsp;I&nbsp;&nbsp;")) space J(("&nbsp;&nbsp;J&nbsp;&nbsp;"))
  space space space space space space space
  K(("&nbsp;&nbsp;K&nbsp;&nbsp;"))

  F-->G
  G-->H
  F-->I
  I-->G
  J-->I
  I-->K

  style F fill:black,stroke:cyan,stroke-width:4px,color:cyan
  style K fill:black,stroke:cyan,stroke-width:4px,color:cyan

  style G fill:black,stroke:cyan,stroke-width:4px,color:cyan
  style H fill:black,stroke:cyan,stroke-width:4px,color:cyan
  style I fill:black,stroke:cyan,stroke-width:4px,color:cyan
  style J fill:black,stroke:cyan,stroke-width:4px,color:cyan
```

### Graph 3

```mermaid
  flowchart LR

  i(("<font>&nbsp;&nbsp;i&nbsp;&nbsp;</font>")):::node --- |cycle| j(("<font>&nbsp;&nbsp;j&nbsp;&nbsp;</font>")):::node

  i(("<font>&nbsp;&nbsp;i&nbsp;&nbsp;</font>")):::node --- |cycle| k(("<font>&nbsp;&nbsp;k&nbsp;&nbsp;</font>")):::node

  k(("<font>&nbsp;&nbsp;k&nbsp;&nbsp;</font>")):::node --- |cycle| j(("<font>&nbsp;&nbsp;j&nbsp;&nbsp;</font>")):::node

  k(("<font>&nbsp;&nbsp;k&nbsp;&nbsp;</font>")):::node --- l(("<font>&nbsp;&nbsp;l&nbsp;&nbsp;</font>")):::node

  k(("<font>&nbsp;&nbsp;k&nbsp;&nbsp;</font>")):::node --- m(("<font>&nbsp;&nbsp;m&nbsp;&nbsp;</font>")):::node
  
  o(("<font>&nbsp;&nbsp;o&nbsp;&nbsp;</font>")):::node --- n(("<font>&nbsp;&nbsp;n&nbsp;&nbsp;</font>")):::node
  
  classDef node fill:black,stroke:cyan,stroke-width:4px,color:cyan
```

### Graph 4
```mermaid
  flowchart LR

  n1(("<font>&nbsp;&nbsp;1&nbsp;&nbsp;</font>")) --- n2(("<font>&nbsp;&nbsp;2&nbsp;&nbsp;</font>"))

  n6(("<font>&nbsp;&nbsp;6&nbsp;&nbsp;</font>")) --- n4(("<font>&nbsp;&nbsp;4&nbsp;&nbsp;</font>"))

  n6(("<font>&nbsp;&nbsp;6&nbsp;&nbsp;</font>")) --- n5(("<font>&nbsp;&nbsp;5&nbsp;&nbsp;</font>"))

  n6(("<font>&nbsp;&nbsp;6&nbsp;&nbsp;</font>")) --- n7(("<font>&nbsp;&nbsp;7&nbsp;&nbsp;</font>"))

  n6(("<font>&nbsp;&nbsp;6&nbsp;&nbsp;</font>")) --- n8(("<font>&nbsp;&nbsp;8&nbsp;&nbsp;</font>"))

  n3(("<font>&nbsp;&nbsp;3&nbsp;&nbsp;</font>"))

  classDef node fill:black,stroke:cyan,stroke-width:4px,color:cyan
```

### Graph 5
```mermaid
  flowchart LR
  n1(("<font>&nbsp;&nbsp;1&nbsp;&nbsp;</font>")) --- n0(("<font>&nbsp;&nbsp;0&nbsp;&nbsp;</font>"))
  n0(("<font>&nbsp;&nbsp;0&nbsp;&nbsp;</font>")) --- n5(("<font>&nbsp;&nbsp;5&nbsp;&nbsp;</font>"))
  n0(("<font>&nbsp;&nbsp;0&nbsp;&nbsp;</font>")) --- n8(("<font>&nbsp;&nbsp;8&nbsp;&nbsp;</font>"))
  n5(("<font>&nbsp;&nbsp;5&nbsp;&nbsp;</font>")) --- n8(("<font>&nbsp;&nbsp;8&nbsp;&nbsp;</font>"))

  n4(("<font>&nbsp;&nbsp;4&nbsp;&nbsp;</font>")) --- n2(("<font>&nbsp;&nbsp;2&nbsp;&nbsp;</font>"))
  n3(("<font>&nbsp;&nbsp;3&nbsp;&nbsp;</font>")) --- n2(("<font>&nbsp;&nbsp;2&nbsp;&nbsp;</font>"))
  n3(("<font>&nbsp;&nbsp;3&nbsp;&nbsp;</font>")) --- n4(("<font>&nbsp;&nbsp;4&nbsp;&nbsp;</font>"))

  classDef node fill:black,stroke:cyan,stroke-width:4px,color:cyan
```

### Graph 6

#### Start: W
#### End: Z
#### Shortest Path: 2 &nbsp; &nbsp; &nbsp; {w, v, z}

```mermaid
  flowchart LR

  w(("<font>&nbsp;&nbsp;W&nbsp;&nbsp;</font>")) --- x(("<font>&nbsp;&nbsp;X&nbsp;&nbsp;</font>"))

  x --- y(("<font>&nbsp;&nbsp;Y&nbsp;&nbsp;</font>"))
  y --- z(("<font>&nbsp;&nbsp;Z&nbsp;&nbsp;</font>"))
  z:::finish --- v(("<font>&nbsp;&nbsp;V&nbsp;&nbsp;</font>"))
  v --- w:::start

  classDef node fill:black,stroke:cyan,stroke-width:4px,color:cyan

  classDef start fill:black,stroke:lime,stroke-width:4px,color:lime

  classDef finish fill:black,stroke:red,stroke-width:4px,color:red
```

### Graph 7 (island count)

6 x 6 grid

&nbsp; &nbsp; 0 &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; 1 &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; 2 &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; 3 &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; 4 &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; 5

```mermaid
block-beta
columns 6

0["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
1["<font class='orange'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>"]
2["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
3["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
4["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
5["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
6["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
7["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
8["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
9["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
10["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
11["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
12["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
13["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
14["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
15["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
16["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
17["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
18["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
19["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
20["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
21["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
22["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
23["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
24["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
25["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
26["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
27["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
28["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
29["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
30["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
31["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
32["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
33["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
34["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
35["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]

style 0 fill:blue,stroke-width:0px
style 1 fill:orange,stroke-width:0px
style 2 fill:blue,stroke-width:0px
style 3 fill:blue,stroke-width:0px
style 4 fill:orange,stroke-width:0px
style 5 fill:blue,stroke-width:0px
style 6 fill:orange,stroke-width:0px
style 7 fill:orange,stroke-width:0px
style 8 fill:blue,stroke-width:0px
style 9 fill:blue,stroke-width:0px
style 10 fill:orange,stroke-width:0px
style 11 fill:blue,stroke-width:0px
style 12 fill:blue,stroke-width:0px
style 13 fill:orange,stroke-width:0px
style 14 fill:blue,stroke-width:0px
style 15 fill:blue,stroke-width:0px
style 16 fill:blue,stroke-width:0px
style 17 fill:blue,stroke-width:0px
style 18 fill:blue,stroke-width:0px
style 19 fill:blue,stroke-width:0px
style 20 fill:blue,stroke-width:0px
style 21 fill:orange,stroke-width:0px
style 22 fill:orange,stroke-width:0px
style 23 fill:blue,stroke-width:0px
style 24 fill:blue,stroke-width:0px
style 25 fill:orange,stroke-width:0px
style 26 fill:blue,stroke-width:0px
style 27 fill:orange,stroke-width:0px
style 28 fill:orange,stroke-width:0px
style 29 fill:blue,stroke-width:0px
style 30 fill:blue,stroke-width:0px
style 31 fill:blue,stroke-width:0px
style 32 fill:blue,stroke-width:0px
style 33 fill:blue,stroke-width:0px
style 34 fill:blue,stroke-width:0px
style 35 fill:blue,stroke-width:0px
```
