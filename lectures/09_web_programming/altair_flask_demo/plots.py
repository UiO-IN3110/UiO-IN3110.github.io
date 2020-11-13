import pandas as pd
import altair as alt


def covids_numbers():
    """ Returns the current covids infections numbers by fylke as a Pandas dictionary """


    data = {'Category': ["Oslo", "Viken", "Vestland", "Rogaland", "Innlandet", "Trøndelag", "Agder", 
			 "Vestfold og Telemark", "Troms og Finnmark",  "Møre og Romsdal", "Nordland"], 
	    'Insidens': [870.5, 410.1, 413.8, 204, 263.3, 182.4, 201.5, 142.1, 204.7, 151.2, 119]}

    return pd.DataFrame.from_dict(data)



def norway_plot():
    # Get covids numbers
    df = covids_numbers()

    # Gets the topojson of norway counties from random gitub
    counties = alt.topo_feature("https://raw.githubusercontent.com/deldersveld/topojson/master/countries/norway/norway-new-counties.json", "Fylker")

    # Define nearest selection (used for the highlighting)
    nearest = alt.selection(type="single", on="mouseover", fields=["properties.navn"], empty="none")

    # Plot the map
    fig = alt.Chart(counties).mark_geoshape().encode(
	# Enable hover efect
	tooltip=[
	    alt.Tooltip("properties.navn:N", title="County"),
	    alt.Tooltip("Insidens:Q", title="Cases per 100k capita"),
	],
	color=alt.Color("Insidens:Q", scale=alt.Scale(scheme="reds"), 
			legend=alt.Legend(title="Cases per 100k capita")),
	stroke=alt.condition(nearest, alt.value("gray"), alt.value(None)),
	opacity=alt.condition(nearest, alt.value(1), alt.value(0.8)),

    # Lookup number of cases from Pandas table and map to counties
    ).transform_lookup(
	lookup="properties.navn",
	from_=alt.LookupData(df, "Category", ["Insidens"])
    ).properties(
	width=500,
	height=600,
	title="Number of cases per 100k in every county",
    ).add_selection(
	nearest
    )

    return fig
