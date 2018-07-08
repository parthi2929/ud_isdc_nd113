**This is a sample markdown page**  

This is just a text  

This is a formula  
$\displaystyle p(X_{i}^{t})=\sum\limits_{{k=1}}^{n}{{p(X_{k}^{{t-1}})p(X_{i}^{t}|X_{k}^{{t-1}})}}$

```dot
digraph G {
    node [shape=circle width=0.4 style=filled];
    ranksep = 0.1;
    nodesep=0.8;
    2 [fillcolor=yellow];
    1 -> 2;
    1 -> 3;
    2 -> 3;
    2 -> 4;
    2 -> 5;
    3 -> 5;
    4 -> 6;
    5 -> 6;
}
```

**A table**
|<span style="font-weight:normal">Visited</span>|<span style="font-weight:normal">0</span>|
|:---------------------------------------------:|----|
|              Queue                 |0