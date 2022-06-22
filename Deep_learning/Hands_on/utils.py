import plotly.graph_objects as go
import numpy as np
import torch


def plot_sin_predictions(training_data, predictions):
    # Create figure
    fig = go.Figure()

    # Add True y values
    fig.add_trace(
        go.Scatter(
            visible=True,
            marker=dict(color="blue", size=3),
            mode='markers',
            name="True y",
            x=training_data['x'],
            y=training_data['y']
        )
    )

    # Add traces, one for each slider step
    for step in np.arange(len(predictions)):
        fig.add_trace(
            go.Scatter(
                visible=False,
                name='Pred y',
                mode='markers',
                marker=dict(color="orange", size=3),
                x=training_data['x'],
                y=predictions[step].flatten()
            )
        )

    # Make 1st trace visible
    fig.data[1].visible = True

    # Create and add slider
    steps = []
    for i in range(1, len(fig.data)):
        visibility = [False] * len(fig.data)
        visibility[0] = True
        visibility[i] = True  # Toggle i'th trace to "visible"
        step = dict(
            method="update",
            label=str(i - 1),
            args=[{"visible": visibility}],  # layout attribute
        )
        steps.append(step)

    sliders = [dict(
        active=0,
        currentvalue={"prefix": "Epoch: "},
        steps=steps
    )]

    min_y = min(predictions[-1].min(), training_data['y'].min()) - 1
    max_y = max(predictions[-1].max(), training_data['y'].max()) + 1

    fig.update_layout(
        sliders=sliders,
        yaxis_range=[min_y, max_y]
    )

    fig.show()


def plot_binary_class_predictions(training_data, predictions, class_to_color=None):
    # Create figure
    fig = go.Figure()
    if class_to_color is None:
        class_to_color = {0: 'blue', 1: 'orange', 2: 'green', 3: 'red'}

    # Add traces, one for each slider step
    for step in np.arange(len(predictions)):
        pred = predictions[step].round().flatten().type(torch.int).numpy()

        fig.add_trace(
            go.Scatter(
                visible=False,
                name='Pred y',
                mode='markers',
                marker_color=np.vectorize(class_to_color.get)(pred),
                marker_size=3,
                x=training_data['x'],
                y=training_data['y']
            )
        )

    # Make 1st trace visible
    fig.data[0].visible = True

    # Create and add slider
    steps = []
    for i in range(len(fig.data)):
        visibility = [False] * len(fig.data)
        visibility[i] = True  # Toggle i'th trace to "visible"
        step = dict(
            method="update",
            label=str(i),
            args=[{"visible": visibility}],  # layout attribute
        )
        steps.append(step)

    sliders = [dict(
        active=1,
        currentvalue={"prefix": "Epoch: "},
        steps=steps
    )]

    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )

    fig.update_layout(
        sliders=sliders,
    )

    fig.show()


def plot_multiple_class_predictions(training_data, predictions, class_to_color=None):
    # Create figure
    fig = go.Figure()
    if class_to_color is None:
        class_to_color = {0: 'blue', 1: 'orange', 2: 'green', 3: 'red'}

    # Add traces, one for each slider step
    for step in np.arange(len(predictions)):
        pred = torch.argmax(predictions[step], dim=1).flatten().type(torch.int).numpy()
        # pred = predictions[step].round().flatten().type(torch.int).numpy()

        fig.add_trace(
            go.Scatter(
                visible=False,
                name='Pred y',
                mode='markers',
                marker_color=np.vectorize(class_to_color.get)(pred),
                marker_size=3,
                x=training_data['x'],
                y=training_data['y']
            )
        )

    # Make 1st trace visible
    fig.data[0].visible = True

    # Create and add slider
    steps = []
    for i in range(len(fig.data)):
        visibility = [False] * len(fig.data)
        visibility[i] = True  # Toggle i'th trace to "visible"
        step = dict(
            method="update",
            label=str(i),
            args=[{"visible": visibility}],  # layout attribute
        )
        steps.append(step)

    sliders = [dict(
        active=1,
        currentvalue={"prefix": "Epoch: "},
        steps=steps
    )]

    fig.add_hline(y=0)
    fig.add_vline(x=0)

    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )

    fig.update_layout(
        sliders=sliders,
    )

    fig.show()
