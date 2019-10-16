import plotly.graph_objects as go

def PrintTable(match):
    campi = ["NUM","NOME","TLR","TLT","T2R","T2T","T3R","T3T","RD","RO","PR","PP","FC","FS","ST","AST","MIN"]
    match.pop("INFO")
    data = {}
    for field in campi:
        data[field] = []
    for giocatore in match:
        data["NOME"].append(giocatore)
        stats = match[giocatore]
        for field in campi:
            if (field != "NOME"):
                data[field].append(stats[field])
    table = list(data.values())


    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'
    fig = go.Figure(data=[go.Table(
    header=dict(
        values=campi,
        line_color='darkslategray',
        fill_color=headerColor,
        align=['left','center','right'],
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=table,
        line_color='darkslategray',
        # 2-D list of colors for alternating rows
        fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
        align = ['left', 'center'],
        font = dict(color = 'darkslategray', size = 11)
        ))
    ])
    fig.show()
    return