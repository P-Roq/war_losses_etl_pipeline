from dash import Dash, html
from dashboard.src.components import vehicle_type_dropdown
from dashboard.src.components import line_chart 
from dashboard.src.components import ids

def create_layout(app: Dash, sources: list) -> html.Div():
    agg_losses_ukraine = sources[0]
    agg_losses_russia = sources[1]

    div_ukraine_losses_by_vehicle_type = html.Div(
        className="app-div",
        children=[
            html.H2('Losses Ukraine'),
            html.Div(
                className="dropdown-container",
                children = [
                    vehicle_type_dropdown.render(
                        app,
                        agg_losses_ukraine,
                        dropdown_id=ids.VEHICLE_TYPE_DROPDOWN_UKRAINE,
                        button_id=ids.SELECT_ALL_VEHICLES_BUTTON_UKRAINE,
                        ),
                    ]
                ),
        line_chart.render(
            app,
            agg_losses_ukraine,
            chart_id=ids.AGGREGATE_LOSSES_LINE_CHART_UKRAINE,
            dropdown_id=ids.VEHICLE_TYPE_DROPDOWN_UKRAINE,
            ),
        ],
    )

    div_russian_losses_by_vehicle_type = html.Div(
        className="app-div",
        children=[
            html.H2('Losses Russia'),
            html.Div(
                className="dropdown-container",
                children=[
                    vehicle_type_dropdown.render(
                        app,
                        agg_losses_russia,
                        dropdown_id=ids.VEHICLE_TYPE_DROPDOWN_RUSSIA,
                        button_id=ids.SELECT_ALL_VEHICLES_BUTTON_RUSSIA,
                        ),
                    ]
                ),
            line_chart.render(
                app,
                agg_losses_russia,
                chart_id=ids.AGGREGATE_LOSSES_LINE_CHART_RUSSIA,
                dropdown_id=ids.VEHICLE_TYPE_DROPDOWN_RUSSIA,
                ),
            ]
        )
    
    layout = html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            div_ukraine_losses_by_vehicle_type,
            div_russian_losses_by_vehicle_type,
            html.H4('Note: Verified losses can be readjusted by the Oryx team, therefore decreasing values can occur.'),
            html.H4('IFV - Infantry Fighting Vehicles'),
            html.H4('AFV - Armoured Fighting Vehicles'),
            html.H4('APC - Armoured Personnel Carriers'),
            html.H4('IMV - Infantry Mobility Vehicles'),
        ]
    )

    return  layout
