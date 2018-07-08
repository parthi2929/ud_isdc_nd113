from graphviz import Digraph

#refer: https://graphviz.readthedocs.io/en/stable/manual.html#basic-usage

dot = Digraph(format='png', comment='The Round Table')

dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

print(dot.source)
dot.render('graphviz_output', view=False)  
