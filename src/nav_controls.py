# Setting up import from parent directories
import sys

sys.path.append("..")

from shiny.types import NavSetArg
from shiny import App, render, ui
from typing import List

# -> : Function returns a list of objects of type NavSetArg
def nav_controls(countries) -> List[NavSetArg]:
    return [
        # 1.) Line Graph -- Nav Controls
        *plot_one_nav_controls(),
        # 2.) Pie Chart -- Nav Controls
        *plot_two_nav_controls(),
        # 3.) Regression -- Nav Controls
        *plot_three_nav_controls(countries)
        # 4.) Choropleth World Sources -- Nav Controls
        #*plot_four_nav_controls()
        ]


def line_graph_info() -> List[NavSetArg]:
    return [
        ui.h5("Range: "),
        ui.output_text(id="elec_pop_year_range"),
        ui.output_plot(id="elec_pop_graph"),
    ]


def plot_one_nav_controls() -> List[NavSetArg]:
    return [
        ui.nav(
            "Line Graph",
            ui.panel_sidebar(
                ui.input_slider(
                    id="elec_pop_range",
                    label="Choose Years",
                    min=1985,
                    max=2020,
                    value=[1990, 2000],
                    step=1,
                    sep="",
                ),
                width=3,
            ),
            ui.panel_main(
                ui.h5("Range: "),
                ui.output_text(id="elec_pop_year_range"),
                ui.output_plot(id="elec_pop_graph"),
            ),
        ),
    ]


def plot_two_nav_controls() -> List[NavSetArg]:
    return [
        ui.nav(
            "Pie Chart",
            ui.panel_sidebar(
                ui.input_slider(
                    id="sawce_year",
                    label="Choose Year",
                    min=2000,
                    max=2020,
                    value=2000,
                    step=1,
                    sep="",
                ),
                width=3,
            ),
            ui.panel_main(
                ui.h5("Distribution: "),
                ui.output_text_verbatim(id="sawce_text"),
                ui.output_plot(id="sawce_graph"),
            ),
        )
    ]


def plot_three_nav_controls(countries) -> List[NavSetArg]:
    return [
        ui.nav(
            "Regression",
            ui.panel_sidebar(
                ui.input_select(id="reg_sawce_select", label="Source: ",choices=["Biofuel","Coal","Gas","Hydro","Nuclear","Oil","Solar","Wind"]),
                ui.input_select(id="reg_country", label="Country: ", choices=countries),
                ui.input_select(id="reg_sawce_degree", label = "Degree: ", choices=[1,2]),
                ui.input_slider(id="reg_year_range",label="Years: ",min=1985,max=2020,value=[1990, 2000],step=1,sep=""),
                width=3,
            ),
            ui.panel_main(
                ui.h5("Linear Regression: "),
                ui.output_text_verbatim(id="reg_sawce_text"),
                ui.output_plot(id="reg_sawce_plot"),
            ),
        )
    ]

def plot_four_nav_controls() -> List[NavSetArg]:
    return [
        ui.nav(
            "World Sources",
            ui.panel_sidebar(
                ui.input_select(
                    id="world_sawce_select",
                    label="Source: ",
                    choices=["Biofuel","Coal","Gas","Hydro","Nuclear","Oil","Solar","Wind"]),
                ui.input_slider(
                    id="world_sawce_year",
                    label="Choose Year",
                    min=1985,
                    max=2020,
                    value=2000,
                    step=1,
                    sep="",
                ),
                width=5,
            ),
            ui.panel_main(
                ui.h5("Plot: "),
            ),
        )
    ]