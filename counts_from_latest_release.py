import streamlit as st
from read_data import read_from_gsheets
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import streamlit.components.v1 as components



st.set_page_config(
    page_title="Places Summary Statistics",
    layout="wide"
)
#### Latest Release ####
filter_list = ["US", "Excluding US", "Grand Total"]
latest_release_df = (
    read_from_gsheets("Global Places")
    [["Country", "Total POI with Parking Lots", "Distinct brands", "Branded POI", "Total POI"]]
    .tail(8)
    .query('Country  == @filter_list')
    .assign(
        **{
            "Total POI with Parking Lots": lambda df: df["Total POI with Parking Lots"].str.replace(",", "").astype(float),
            "Total POI": lambda df: df["Total POI"].str.replace(",", "").astype(int),
            "Branded POI": lambda df: df["Branded POI"].str.replace(",", "").astype(int),
            "% Branded": lambda df: (df["Branded POI"] / df["Total POI"]) * 100,
            "Distinct brands": lambda df: df["Distinct brands"].astype(int)
        }
    )
    .drop(["Branded POI", "Total POI"], axis=1)
    .reset_index(drop=True)
)

latest_release_df.loc[latest_release_df.Country == "Excluding US", 'Country'] = 'Rest of World'

latest_release_df_styled = (
    latest_release_df.style
    .apply(lambda x: ['background-color: #D7E8ED' if i%2==0 else '' for i in range(len(x))], axis=0)
    .format({
        "Total POI with Parking Lots": "{:,.0f}",
        "% Branded": "{:.1f}%",
        "Distinct brands": "{:,.0f}"
    })
)

total_poi = latest_release_df.iloc[-1]["Total POI with Parking Lots"]

parking_lots_df = (
    read_from_gsheets("Parking")
    .assign(**{
        "Distinct brands": "NA",
        "% Branded": "NA",
        "Total POI": lambda df: df["Total POI"].str.replace(",", "").astype(int)
    })
    [["Country", "Total POI", "Distinct brands", "% Branded"]]
)

parking_lots_df_styled = (
    parking_lots_df.style
    .apply(lambda x: ['background-color: #D7E8ED' if i % 2 == 0 else '' for i in range(len(x))], axis=0)
    .format({
        "Total POI": "{:,.0f}"
    })
)
st.markdown(f"#### Total POI count across countries, including parking lots POI is <b>{total_poi:,.0f}</b>", unsafe_allow_html=True)
#st.write(, unsafe_allow_html=True)
st.dataframe(latest_release_df_styled, use_container_width=True,hide_index=True)
st.markdown("#### Latest Release - Parking")
#st.write("Latest Release - Parking")
st.dataframe(parking_lots_df_styled, use_container_width=True,hide_index=True)

hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

css = '''
<style>
section.main > div:has(~ footer ) {
    padding-top: 0px;
    padding-bottom: 0px;
}

[data-testid="ScrollToBottomContainer"] {
    overflow: hidden;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)

# Keep-alive comment: 2025-04-25 16:18:30.263502
# Keep-alive comment: 2025-04-26 00:24:05.047136
# Keep-alive comment: 2025-04-26 11:23:59.689392
# Keep-alive comment: 2025-04-26 22:22:58.894545
# Keep-alive comment: 2025-04-27 09:23:29.982949
# Keep-alive comment: 2025-04-27 20:23:24.922313
# Keep-alive comment: 2025-04-28 07:23:55.082107
# Keep-alive comment: 2025-04-28 18:24:15.302326
# Keep-alive comment: 2025-04-29 05:23:44.801714
# Keep-alive comment: 2025-04-29 16:24:29.311745
# Keep-alive comment: 2025-04-30 03:23:19.593796
# Keep-alive comment: 2025-04-30 14:23:47.771993
# Keep-alive comment: 2025-05-01 01:23:59.151332
# Keep-alive comment: 2025-05-01 12:23:30.329057
# Keep-alive comment: 2025-05-01 23:23:03.009603
# Keep-alive comment: 2025-05-02 10:23:49.214335
# Keep-alive comment: 2025-05-02 21:23:00.693267
# Keep-alive comment: 2025-05-03 08:23:25.148713
# Keep-alive comment: 2025-05-03 19:23:43.250472
# Keep-alive comment: 2025-05-04 06:23:48.582256
# Keep-alive comment: 2025-05-04 17:22:57.940387
# Keep-alive comment: 2025-05-05 04:24:08.523461
# Keep-alive comment: 2025-05-05 15:23:27.789856
# Keep-alive comment: 2025-05-06 02:24:19.007447
# Keep-alive comment: 2025-05-06 13:23:20.470412
# Keep-alive comment: 2025-05-07 00:23:19.534203
# Keep-alive comment: 2025-05-07 11:23:20.207381
# Keep-alive comment: 2025-05-07 22:23:30.510835
# Keep-alive comment: 2025-05-08 09:23:23.545478
# Keep-alive comment: 2025-05-08 20:23:30.910728
# Keep-alive comment: 2025-05-09 07:23:38.613812
# Keep-alive comment: 2025-05-09 18:23:52.739151
# Keep-alive comment: 2025-05-10 05:23:33.911187
# Keep-alive comment: 2025-05-10 16:23:22.460313
# Keep-alive comment: 2025-05-11 03:23:22.975182
# Keep-alive comment: 2025-05-11 14:23:14.569083
# Keep-alive comment: 2025-05-12 01:23:19.795852
# Keep-alive comment: 2025-05-12 12:23:50.131497
# Keep-alive comment: 2025-05-12 23:23:23.537930
# Keep-alive comment: 2025-05-13 10:24:23.495728
# Keep-alive comment: 2025-05-13 21:23:24.321243
# Keep-alive comment: 2025-05-14 08:23:50.508332
# Keep-alive comment: 2025-05-14 19:23:49.431533
# Keep-alive comment: 2025-05-15 06:23:50.875007
# Keep-alive comment: 2025-05-15 17:24:14.881673
# Keep-alive comment: 2025-05-16 04:23:36.035106
# Keep-alive comment: 2025-05-16 15:22:38.792264
# Keep-alive comment: 2025-05-17 02:22:57.096923
# Keep-alive comment: 2025-05-17 13:23:30.963451
# Keep-alive comment: 2025-05-18 00:22:55.674494
# Keep-alive comment: 2025-05-18 11:23:23.874400
# Keep-alive comment: 2025-05-18 22:23:21.325077
# Keep-alive comment: 2025-05-19 09:23:57.450712
# Keep-alive comment: 2025-05-19 20:22:56.286400
# Keep-alive comment: 2025-05-20 07:23:12.407968
# Keep-alive comment: 2025-05-20 18:24:24.633464
# Keep-alive comment: 2025-05-21 05:22:56.316022
# Keep-alive comment: 2025-05-21 16:23:05.524721
# Keep-alive comment: 2025-05-22 03:22:59.952729
# Keep-alive comment: 2025-05-22 14:23:03.757230
# Keep-alive comment: 2025-05-23 01:23:02.411075