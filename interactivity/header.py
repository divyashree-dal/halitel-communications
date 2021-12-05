import dash_html_components as html

colors = {
    "text": "#FFFFFF"
}

##############################################
"""
    File Usage: Navigation Bar for th dash page
"""
##############################################


def navigation_bar():
    return html.Div(
        id="navigation",
        className="navigation",
        children=[
            html.Div(
                id="navigation-text",
                children=[
                    html.H5("Halitel Communications!", style={'color': 'rgb(145, 223, 210)','font-weight':'bold'}),
                    html.H6("CSCI 6612 : Visual Analytics Project : Team - Absolute Analytics"),
                ],
            ),
        ],
        style={
            'color': colors['text'],
            'display': 'inline-block'
        }
    )
