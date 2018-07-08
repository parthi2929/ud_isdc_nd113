from plotly.offline import plot


figure = {'data': [{'x': [0, 1], 'y': [0, 1]}],
          'layout': {'xaxis': {'range': [0, 5], 'autorange': False},
                     'yaxis': {'range': [0, 5], 'autorange': False},
                     'title': 'Start Title',
                     'updatemenus': [{'type': 'buttons',
                                      'buttons': [{'label': 'Play',
                                                   'method': 'animate',
                                                   'args': [None]}]}]
                    },
          'frames': [
            {'data': [{'x': [1, 2], 'y': [1, 2]}]}, #frame1 
            {'data': [{'x': [1, 4], 'y': [1, 4]}]}, #frame2
            {'data': [{'x': [3, 4], 'y': [3, 4]}],  #frame3

                      'layout': {'title': 'End Title'}}]}

plot(figure)