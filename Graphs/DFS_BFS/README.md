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
