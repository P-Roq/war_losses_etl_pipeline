from dash import Dash, html
from dashboard.src.components import vehicle_type_dropdown
from dashboard.src.components import vehicle_type_dropdown_2
from dashboard.src.components import loss_type_dropdown
from dashboard.src.components import date_range_slider
from dashboard.src.components import line_chart_losses_by_country 
from dashboard.src.components import line_chart_country_comparison
from dashboard.src.components import ids

def create_layout(app: Dash, sources: list) -> html.Div():
    agg_losses_ukraine = sources[0]
    agg_losses_russia = sources[1]

    #-------------------------------------------------------------------------------

    div_ukraine_losses_by_vehicle_type = html.Div(
        className="app-div",
        children=[
            html.H2('Losses Ukraine'),
            html.Div(
                className="dropdown-container",
                children = [
                    loss_type_dropdown.render(
                        app,
                        agg_losses_ukraine,
                        dropdown_id=ids.DROPDOWN_LOSS_TYPE_UKRAINE,
                        ),
                    vehicle_type_dropdown.render(
                        app,
                        agg_losses_ukraine,
                        dropdown_id=ids.DROPDOWN_VEHICLE_TYPE_UKRAINE,
                        button_id=ids.BUTTON_SELECT_ALL_VEHICLES_UKRAINE,
                        ),
                    ]
                ),
        line_chart_losses_by_country.render(
            app,
            agg_losses_ukraine,
            chart_id=ids.LINE_CHART_AGGREGATE_LOSSES_UKRAINE,
            dropdown_loss_type_id=ids.DROPDOWN_LOSS_TYPE_UKRAINE,
            dropdown_vehicle_type_id=ids.DROPDOWN_VEHICLE_TYPE_UKRAINE,
            date_range_slider_id=ids.DATE_RANGE_SLIDER_AGGREGATE_LOSSES_UKRAINE
            ),
        html.Div(
                className="date_range_slider_container",
                children=[
                    date_range_slider.render(
                        app,
                        agg_losses_ukraine,
                        date_range_slider_id=ids.DATE_RANGE_SLIDER_AGGREGATE_LOSSES_UKRAINE,
                        ),
                    ],
                ),
            ],
        )

    #-------------------------------------------------------------------------------

    div_russian_losses_by_vehicle_type = html.Div(
        className="app-div",
        children=[
            html.H2('Losses Russia'),
            html.Div(
                className="dropdown-container",
                children=[
                    loss_type_dropdown.render(
                        app,
                        agg_losses_russia,
                        dropdown_id=ids.DROPDOWN_LOSS_TYPE_RUSSIA,
                        ),
                    vehicle_type_dropdown.render(
                        app,
                        agg_losses_russia,
                        dropdown_id=ids.DROPDOWN_VEHICLE_TYPE_RUSSIA,
                        button_id=ids.BUTTON_SELECT_ALL_VEHICLES_RUSSIA,
                        ),
                    ]
                ),
            line_chart_losses_by_country.render(
                app,
                agg_losses_russia,
                chart_id=ids.LINE_CHART_AGGREGATE_LOSSES_RUSSIA,
                dropdown_loss_type_id=ids.DROPDOWN_LOSS_TYPE_RUSSIA,
                dropdown_vehicle_type_id=ids.DROPDOWN_VEHICLE_TYPE_RUSSIA,
                date_range_slider_id=ids.DATE_RANGE_SLIDER_AGGREGATE_LOSSES_RUSSIA
                ),
            html.Div(
                className="date_range_slider_container",
                children=[
                    date_range_slider.render(
                        app,
                        agg_losses_russia,
                        date_range_slider_id=ids.DATE_RANGE_SLIDER_AGGREGATE_LOSSES_RUSSIA,
                        ),
                    ],
                ),
            ]
        )
    
    #-------------------------------------------------------------------------------

    div_losses_comparison_by_country = html.Div(
        className="app-div",
        children=[
            html.H2('Country Comparison'),
            html.Div(
                className="dropdown-container",
                children=[
                    loss_type_dropdown.render(
                        app,
                        agg_losses_russia, # doesn't matter which country is used
                        dropdown_id=ids.DROPDOWN_LOSS_TYPE_COUNTRY_COMPARISON, 
                        ),
                    vehicle_type_dropdown_2.render(
                        app,
                        agg_losses_russia, # doesn't matter which country is used
                        dropdown_id=ids.DROPDOWN_VEHICLE_TYPE_COUNTRY_COMPARISON, 
                        ),
                    ]
                ),
            line_chart_country_comparison.render(
                app,
                agg_losses_ukraine,
                agg_losses_russia,
                chart_id=ids.LINE_CHART_AGGREGATE_LOSSES_COMPARISON,
                dropdown_loss_type_id=ids.DROPDOWN_LOSS_TYPE_COUNTRY_COMPARISON,
                dropdown_vehicle_type_id=ids.DROPDOWN_VEHICLE_TYPE_COUNTRY_COMPARISON,
                date_range_slider_id=ids.DATE_RANGE_SLIDER_AGGREGATE_LOSSES_COMPARISON,
                ),
            html.Div(
                className="date_range_slider_container",
                children=[
                    date_range_slider.render(
                        app,
                        agg_losses_russia, # doesn't matter which country is used
                        date_range_slider_id=ids.DATE_RANGE_SLIDER_AGGREGATE_LOSSES_COMPARISON,
                        ),
                    ],
                ),
            ],
        )

    #-------------------------------------------------------------------------------

    layout = html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            div_ukraine_losses_by_vehicle_type,
            div_russian_losses_by_vehicle_type,
            div_losses_comparison_by_country,
            html.H4('Note: Verified losses can be readjusted by the Oryx team, therefore decreasing values can occur.'),
            html.H4('IFV - Infantry Fighting Vehicles'),
            html.H4('AFV - Armoured Fighting Vehicles'),
            html.H4('APC - Armoured Personnel Carriers'),
            html.H4('IMV - Infantry Mobility Vehicles'),
        ]
    )

    return  layout
