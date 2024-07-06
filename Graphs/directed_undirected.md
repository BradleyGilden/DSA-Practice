<h1 align="center">Graphs</h1>

## What is a Graph?
graph = $\color{cyan}{nodes}$ + $\color{yellow}{edges}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  (collection of nodes and edges)

<br/>

### $\color{cyan}{directed\ graph}$ 

```mermaid
  block-beta
  columns 3
  A(("<font color='cyan'>&nbsp;&nbsp;A&nbsp;&nbsp;</font>")) space C(("<font color='cyan'>&nbsp;&nbsp;C&nbsp;&nbsp;</font>"))
  space space space
  B(("<font color='cyan'>&nbsp;&nbsp;B&nbsp;&nbsp;</font>")) space E(("<font color='cyan'>&nbsp;&nbsp;E&nbsp;&nbsp;</font>"))
  space space space
  D(("<font color='cyan'>&nbsp;&nbsp;D&nbsp;&nbsp;</font>")) space F(("<font color='cyan'>&nbsp;&nbsp;F&nbsp;&nbsp;</font>"))
  A--"edge"-->C
  C-->E
  E-->B
  A-->B
  F-->D
  B-->D
```

### $\color{cyan}{adjacency\ List}$

```
{
  a: [b, c],
  b: [d],
  c: [e],
  d: [],
  e: [b],
  f: [d],
}
```
<br/>

### $\color{orange}{undirected\ graph}$ 

```mermaid
  flowchart LR
  A((<font color='orange'>&nbsp;&nbsp;A&nbsp;&nbsp;</font>)) --- C((<font color='orange'>&nbsp;&nbsp;C&nbsp;&nbsp;</font>))
  C--- E((<font color='orange'>&nbsp;&nbsp;E&nbsp;&nbsp;</font>))
  E--- B((<font color='orange'>&nbsp;&nbsp;B&nbsp;&nbsp;</font>))
  A--- B
  F--- D((<font color='orange'>&nbsp;&nbsp;D&nbsp;&nbsp;</font>))
  B--- D
  F((<font color='orange'>&nbsp;&nbsp;F&nbsp;&nbsp;</font>)) --- A


```
