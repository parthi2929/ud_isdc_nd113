## STACK/QUEUE: Navigation example without closed loops
```dot
digraph structs {
    
    node [shape=record width=0.4];
    rankdir=LR;
    
    current [label="B" style=filled fillcolor=green];
    stack [label="{ <f0> C |<f1> P |<f2> M   }" style=filled fillcolor=yellow];
    
    stack:f2 -> current;

}
```

## TREE: Navigation example without closed loops...
```dot
digraph G1 {
    
    node [shape=circle width=0.4 style=filled fixedsize=true];

    A -> S;
    A -> T;
    A -> Z;
    S -> F;
    S -> RV;
    T -> LU;
    Z -> O;
    F -> B;
    RV -> C,P;
    LU -> M;

    M -> D;
    B -> G, U;
    U -> V -> LA -> N;
    U -> H -> E;
}
```


## MAP: Navigation example without closed loops

```dot {engine="neato"} 
graph G {

    overlap=compress;
    sep=4;

    edge [ fontsize=9 color="#92CCBF" fontcolor="#7c7c7c" ];

    node [shape=box width=0.1 height=0.1 style=filled fontname="Arial" fontsize=10 fixedsize=true color="#179E9C" ];

    A [xlabel=Arad, label="" pos="-3.25,0.15!" color=red];
    S [xlabel=Sibiu label=""  pos="-1.75,-0.05!"];
    Z [xlabel=Zerind label="" pos="-2.95,0.75!"];
    T [xlabel=Timisoara label="" pos="-3.30,-0.8!"];

    O [xlabel=Oradea label="" pos="-2.45,1.35!"];
    LU [xlabel=Lugoj label="" pos="-2.25,-1.25!"];
    M [xlabel=Mehadia label="" pos="-2.15,-2!"];
    D [xlabel=Drobeta label="" pos="-2.3,-2.75!"];
    C [xlabel=Craiova label="" pos="-1,-2.75!"];

    RV [xlabel="Rimnicu Vilcea" label="" pos="-1.25,-0.8!"];
    P [xlabel=Pitesti label="" pos="0.0,-1.45!"];
    F [xlabel=Fagaras label=""  pos="-0.25,-0.15!"];
    B [xlabel=Bucharest label="" pos="1.5,-2.1!" color=red];

    G [xlabel=Giurgiu label="" pos="1.3,-2.85!"];
    U [xlabel=Urziceni label="" pos="3,-1.85!"];
    H [xlabel=Hirsova label="" pos="4,-2!"];
    E [xlabel=Eforie label="" pos="3.8,-3!"];

    V [xlabel=Vaslui label="" pos="3.5,-0.05!"];
    LA [xlabel=lasi label="" pos="2.75,0.75!"];
    N [xlabel=Neamt label="" pos="2,1.25!"];

    A -- Z [label=75];
    A -- S [label=140];
    A -- T [label=118];


    S -- F [label=99];
    S -- RV [label=80];

    Z -- O [label=71];
    T -- LU [label=111];
    LU -- M [label=70]; 
    M -- D [label=75]; 


    RV  -- C [label=146];
    RV  -- P [label=97];

    F -- B [label=211];

    G -- B [label=90];
    B -- U [label=85];
    U -- H [label=98];
    H -- E [label=86];
    U -- V [label=142];
    V -- LA [label=92];
    LA -- N [label=87];
}
```

**Simpler Smaller View**
```dot {engine="neato"}
graph G {

    overlap=compress;
    sep=3;
    edge [ fontsize=9 color=grey fontcolor="#7c7c7c" ];
    node [shape=box width=0.1 height=0.1 style=filled fontname="Arial" fontsize=10 fixedsize=true color="#666666" ];

    A [xlabel=A, label="" pos="-3.25,0.15!" color=red];
    S [xlabel=S label=""  pos="-1.75,-0.05!"];
    Z [xlabel=Z label="" pos="-2.95,0.75!"];
    T [xlabel=T label="" pos="-3.30,-0.8!"];

    O [xlabel=O label="" pos="-2.45,1.35!"];
    LU [xlabel=LU label="" pos="-2.25,-1.25!"];
    M [xlabel=M label="" pos="-2.15,-2!"];
    D [xlabel=D label="" pos="-2.3,-2.75!"];
    C [xlabel=C label="" pos="-1,-2.75!"];

    RV [xlabel=RV label="" pos="-1.25,-0.8!"];
    P [xlabel=P label="" pos="0.0,-1.45!"];
    F [xlabel=F label=""  pos="-0.25,-0.15!"];
    B [xlabel=B label="" pos="1.5,-2.1!" color=red];

    G [xlabel=G label="" pos="1.3,-2.85!"];
    U [xlabel=U label="" pos="3,-1.85!"];
    H [xlabel=H label="" pos="4,-2!"];
    E [xlabel=E label="" pos="3.8,-3!"];

    V [xlabel=V label="" pos="3.5,-0.05!"];
    LA [xlabel=LA label="" pos="2.75,0.75!"];
    N [xlabel=N label="" pos="2,1.25!"];

    A -- Z [label=75];
    A -- S [label=140];
    A -- T [label=118];


    S -- F [label=99];
    S -- RV [label=80];

    Z -- O [label=71];
    T -- LU [label=111];
    LU -- M [label=70]; 
    M -- D [label=75]; 


    RV  -- C [label=146];
    RV  -- P [label=97];

    F -- B [label=211];

    G -- B [label=90];
    B -- U [label=85];
    U -- H [label=98];
    H -- E [label=86];
    U -- V [label=142];
    V -- LA [label=92];
    LA -- N [label=87];

    A [color=black fillcolor=green];
    S,T,Z [color=black fillcolor=orange];
}
```

## MAP: Navigation example with closed loops
```dot {engine="neato"}
graph G {

    overlap=compress;
    sep=4;

    edge [ fontsize=9 color="#92CCBF" fontcolor="#7c7c7c" ];

    node [shape=box width=0.1 height=0.1 style=filled fontname="Arial" fontsize=10 fixedsize=true color="#179E9C" ];

    A [xlabel=Arad, label="" pos="-3.25,0.15!" color=red];
    S [xlabel=Sibiu label=""  pos="-1.75,-0.05!"];
    Z [xlabel=Zerind label="" pos="-2.95,0.75!"];
    T [xlabel=Timisoara label="" pos="-3.30,-0.8!"];

    O [xlabel=Oradea label="" pos="-2.45,1.35!"];
    LU [xlabel=Lugoj label="" pos="-2.25,-1.25!"];
    M [xlabel=Mehadia label="" pos="-2.15,-2!"];
    D [xlabel=Drobeta label="" pos="-2.3,-2.75!"];
    C [xlabel=Craiova label="" pos="-1,-2.75!"];

    RV [xlabel="Rimnicu Vilcea" label="" pos="-1.25,-0.8!"];
    P [xlabel=Pitesti label="" pos="0.0,-1.45!"];
    F [xlabel=Fagaras label=""  pos="-0.25,-0.15!"];
    B [xlabel=Bucharest label="" pos="1.5,-2.1!" color=red];

    G [xlabel=Giurgiu label="" pos="1.3,-2.85!"];
    U [xlabel=Urziceni label="" pos="3,-1.85!"];
    H [xlabel=Hirsova label="" pos="4,-2!"];
    E [xlabel=Eforie label="" pos="3.8,-3!"];

    V [xlabel=Vaslui label="" pos="3.5,-0.05!"];
    LA [xlabel=lasi label="" pos="2.75,0.75!"];
    N [xlabel=Neamt label="" pos="2,1.25!"];

    A -- Z [label=75];
    A -- S [label=140];
    A -- T [label=118];

    S -- O [label=151];
    S -- F [label=99];
    S -- RV [label=80];

    Z -- O [label=71];
    T -- LU [label=111];
    LU -- M [label=70]; 
    M -- D [label=75]; 
    D -- C [label=120];

    RV  -- C [label=146];
    RV  -- P [label=97];
    C -- P [label=138];
    F -- B [label=211];
    P -- B [label=101];
    G -- B [label=90];
    B -- U [label=85];
    U -- H [label=98];
    H -- E [label=86];
    U -- V [label=142];
    V -- LA [label=92];
    LA -- N [label=87];
}
```
```dot
digraph G1 {
    node [width=0.2 style=filled];
    Arad [fillcolor=green];
    Arad -> Zerind;
    Arad -> Sibiu;
    Arad -> Timisoara;
}
```