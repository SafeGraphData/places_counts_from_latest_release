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
# Keep-alive comment: 2025-05-23 12:23:02.182404
# Keep-alive comment: 2025-05-23 23:23:06.345375
# Keep-alive comment: 2025-05-24 10:23:03.936710
# Keep-alive comment: 2025-05-24 21:23:00.612905
# Keep-alive comment: 2025-05-25 08:23:01.349765
# Keep-alive comment: 2025-05-25 19:23:06.057751
# Keep-alive comment: 2025-05-26 06:22:51.405978
# Keep-alive comment: 2025-05-26 17:22:55.865151
# Keep-alive comment: 2025-05-27 04:23:01.409371
# Keep-alive comment: 2025-05-27 15:23:05.836882
# Keep-alive comment: 2025-05-28 02:23:15.739373
# Keep-alive comment: 2025-05-28 13:23:05.158216
# Keep-alive comment: 2025-05-29 00:22:59.242655
# Keep-alive comment: 2025-05-29 11:22:54.382958
# Keep-alive comment: 2025-05-29 22:23:08.811888
# Keep-alive comment: 2025-05-30 09:22:54.003045
# Keep-alive comment: 2025-05-30 20:22:54.905779
# Keep-alive comment: 2025-05-31 07:23:07.059435
# Keep-alive comment: 2025-05-31 18:23:01.713705
# Keep-alive comment: 2025-06-01 05:22:59.666428
# Keep-alive comment: 2025-06-01 16:23:13.584235
# Keep-alive comment: 2025-06-02 03:23:15.176692
# Keep-alive comment: 2025-06-02 14:23:06.043718
# Keep-alive comment: 2025-06-03 01:22:56.389228
# Keep-alive comment: 2025-06-03 12:23:10.984484
# Keep-alive comment: 2025-06-03 23:23:06.411010
# Keep-alive comment: 2025-06-04 10:23:06.099309
# Keep-alive comment: 2025-06-04 21:22:44.992523
# Keep-alive comment: 2025-06-05 08:23:08.473861
# Keep-alive comment: 2025-06-05 19:22:58.157316
# Keep-alive comment: 2025-06-06 06:22:56.115688
# Keep-alive comment: 2025-06-06 17:22:39.424649
# Keep-alive comment: 2025-06-07 04:22:41.198660
# Keep-alive comment: 2025-06-07 15:22:50.463310
# Keep-alive comment: 2025-06-08 02:22:55.652895
# Keep-alive comment: 2025-06-08 13:22:57.531510
# Keep-alive comment: 2025-06-09 00:22:39.704255
# Keep-alive comment: 2025-06-09 11:22:54.417625
# Keep-alive comment: 2025-06-09 22:23:03.063993
# Keep-alive comment: 2025-06-10 09:23:06.067068
# Keep-alive comment: 2025-06-10 20:22:58.988807
# Keep-alive comment: 2025-06-11 07:23:00.179568
# Keep-alive comment: 2025-06-11 18:24:48.620964
# Keep-alive comment: 2025-06-12 05:22:57.372317
# Keep-alive comment: 2025-06-12 16:23:00.668661
# Keep-alive comment: 2025-06-13 03:23:01.794451
# Keep-alive comment: 2025-06-13 14:22:51.043805
# Keep-alive comment: 2025-06-14 01:23:10.869393
# Keep-alive comment: 2025-06-14 12:22:57.913612
# Keep-alive comment: 2025-06-14 23:22:49.356123
# Keep-alive comment: 2025-06-15 10:22:34.963065
# Keep-alive comment: 2025-06-15 21:23:09.752806
# Keep-alive comment: 2025-06-16 08:23:06.810773
# Keep-alive comment: 2025-06-16 19:22:50.834283
# Keep-alive comment: 2025-06-17 06:23:27.645552
# Keep-alive comment: 2025-06-17 17:22:55.579446
# Keep-alive comment: 2025-06-18 04:23:01.655674
# Keep-alive comment: 2025-06-18 15:23:00.615765
# Keep-alive comment: 2025-06-19 02:22:59.346970
# Keep-alive comment: 2025-06-19 13:22:59.238431
# Keep-alive comment: 2025-06-20 00:22:55.968865
# Keep-alive comment: 2025-06-20 11:23:45.170225
# Keep-alive comment: 2025-06-20 22:23:04.666149
# Keep-alive comment: 2025-06-21 09:22:49.890347
# Keep-alive comment: 2025-06-21 20:23:02.154991
# Keep-alive comment: 2025-06-22 07:22:54.963222
# Keep-alive comment: 2025-06-22 18:22:45.843305
# Keep-alive comment: 2025-06-23 05:23:02.056426
# Keep-alive comment: 2025-06-23 16:22:55.362027
# Keep-alive comment: 2025-06-24 03:23:01.805223
# Keep-alive comment: 2025-06-24 14:22:41.374516
# Keep-alive comment: 2025-06-25 01:22:35.513624
# Keep-alive comment: 2025-06-25 12:22:57.570994
# Keep-alive comment: 2025-06-25 23:22:59.900068
# Keep-alive comment: 2025-06-26 10:23:07.411314
# Keep-alive comment: 2025-06-26 21:24:31.989133
# Keep-alive comment: 2025-06-27 08:23:00.694491
# Keep-alive comment: 2025-06-27 19:22:57.257023
# Keep-alive comment: 2025-06-28 06:23:04.241687
# Keep-alive comment: 2025-06-28 17:22:54.572623
# Keep-alive comment: 2025-06-29 04:22:43.823668
# Keep-alive comment: 2025-06-29 15:22:34.195946
# Keep-alive comment: 2025-06-30 02:22:55.594868
# Keep-alive comment: 2025-06-30 13:22:37.488451
# Keep-alive comment: 2025-07-01 00:24:41.819130
# Keep-alive comment: 2025-07-01 11:22:56.807810
# Keep-alive comment: 2025-07-01 22:23:01.145724
# Keep-alive comment: 2025-07-02 09:22:55.098320
# Keep-alive comment: 2025-07-02 20:24:44.185546
# Keep-alive comment: 2025-07-03 07:23:09.808286
# Keep-alive comment: 2025-07-03 18:22:35.789063
# Keep-alive comment: 2025-07-04 05:22:58.408243
# Keep-alive comment: 2025-07-04 16:22:54.709703
# Keep-alive comment: 2025-07-05 03:22:53.127124
# Keep-alive comment: 2025-07-05 14:22:58.389406
# Keep-alive comment: 2025-07-06 01:22:56.311540
# Keep-alive comment: 2025-07-06 12:22:53.066110
# Keep-alive comment: 2025-07-06 23:22:54.717939
# Keep-alive comment: 2025-07-07 10:22:55.452242
# Keep-alive comment: 2025-07-07 21:22:54.261711
# Keep-alive comment: 2025-07-08 08:22:58.666601
# Keep-alive comment: 2025-07-08 19:22:54.562363
# Keep-alive comment: 2025-07-09 06:23:05.377503
# Keep-alive comment: 2025-07-09 17:23:38.799016
# Keep-alive comment: 2025-07-10 04:22:53.952489
# Keep-alive comment: 2025-07-10 15:23:00.088366
# Keep-alive comment: 2025-07-11 02:22:52.820707
# Keep-alive comment: 2025-07-11 13:22:54.087428
# Keep-alive comment: 2025-07-12 00:22:40.229800
# Keep-alive comment: 2025-07-12 11:22:58.267941
# Keep-alive comment: 2025-07-12 22:22:54.298914
# Keep-alive comment: 2025-07-13 09:22:54.153771
# Keep-alive comment: 2025-07-13 20:22:38.850603
# Keep-alive comment: 2025-07-14 07:22:51.482668
# Keep-alive comment: 2025-07-14 18:23:14.583757
# Keep-alive comment: 2025-07-15 05:23:04.764556
# Keep-alive comment: 2025-07-15 16:22:59.288085
# Keep-alive comment: 2025-07-16 03:22:58.595363
# Keep-alive comment: 2025-07-16 14:22:59.744428
# Keep-alive comment: 2025-07-17 01:22:54.244401
# Keep-alive comment: 2025-07-17 12:23:00.515608
# Keep-alive comment: 2025-07-17 23:22:52.478433
# Keep-alive comment: 2025-07-18 10:23:14.396745
# Keep-alive comment: 2025-07-18 21:22:54.007791
# Keep-alive comment: 2025-07-19 08:23:34.055449
# Keep-alive comment: 2025-07-19 19:22:38.987310
# Keep-alive comment: 2025-07-20 06:23:03.430919
# Keep-alive comment: 2025-07-20 17:23:09.568830
# Keep-alive comment: 2025-07-21 04:23:04.011316
# Keep-alive comment: 2025-07-21 15:22:51.270234
# Keep-alive comment: 2025-07-22 02:23:13.532888
# Keep-alive comment: 2025-07-22 13:23:27.237845
# Keep-alive comment: 2025-07-23 00:23:00.552675
# Keep-alive comment: 2025-07-23 11:22:50.374078
# Keep-alive comment: 2025-07-23 22:22:53.424027
# Keep-alive comment: 2025-07-24 09:23:09.721735
# Keep-alive comment: 2025-07-24 20:22:55.651449
# Keep-alive comment: 2025-07-25 07:22:50.124563
# Keep-alive comment: 2025-07-25 18:22:55.174549
# Keep-alive comment: 2025-07-26 05:22:49.243656
# Keep-alive comment: 2025-07-26 16:22:54.084039
# Keep-alive comment: 2025-07-27 03:22:48.988402
# Keep-alive comment: 2025-07-27 14:22:39.507660
# Keep-alive comment: 2025-07-28 01:23:00.734913
# Keep-alive comment: 2025-07-28 12:22:56.049607
# Keep-alive comment: 2025-07-28 23:22:54.024274
# Keep-alive comment: 2025-07-29 10:22:29.528701
# Keep-alive comment: 2025-07-29 21:22:59.896627
# Keep-alive comment: 2025-07-30 08:22:56.063521
# Keep-alive comment: 2025-07-30 19:23:04.420144
# Keep-alive comment: 2025-07-31 06:23:09.349328
# Keep-alive comment: 2025-07-31 17:22:55.078149
# Keep-alive comment: 2025-08-01 04:22:52.980562
# Keep-alive comment: 2025-08-01 15:23:04.468078
# Keep-alive comment: 2025-08-02 02:22:48.464016
# Keep-alive comment: 2025-08-02 13:22:59.351431
# Keep-alive comment: 2025-08-03 00:22:54.840833
# Keep-alive comment: 2025-08-03 11:23:00.036800
# Keep-alive comment: 2025-08-03 22:22:54.627565
# Keep-alive comment: 2025-08-04 09:22:51.876597
# Keep-alive comment: 2025-08-04 20:22:56.278040
# Keep-alive comment: 2025-08-05 07:22:58.907826
# Keep-alive comment: 2025-08-05 18:23:00.686421
# Keep-alive comment: 2025-08-06 05:22:54.355921
# Keep-alive comment: 2025-08-06 16:24:45.423607
# Keep-alive comment: 2025-08-07 03:22:58.614278
# Keep-alive comment: 2025-08-07 14:23:00.811414
# Keep-alive comment: 2025-08-08 01:22:49.474795
# Keep-alive comment: 2025-08-08 12:23:00.365309
# Keep-alive comment: 2025-08-08 23:23:00.720992
# Keep-alive comment: 2025-08-09 10:22:53.926237
# Keep-alive comment: 2025-08-09 21:23:16.392753
# Keep-alive comment: 2025-08-10 08:23:00.315861
# Keep-alive comment: 2025-08-10 19:23:00.298414
# Keep-alive comment: 2025-08-11 06:22:54.796508
# Keep-alive comment: 2025-08-11 17:23:00.772840
# Keep-alive comment: 2025-08-12 04:22:59.245794
# Keep-alive comment: 2025-08-12 15:22:52.044057
# Keep-alive comment: 2025-08-13 02:23:00.330536
# Keep-alive comment: 2025-08-13 13:22:57.354495
# Keep-alive comment: 2025-08-14 00:22:53.511132
# Keep-alive comment: 2025-08-14 11:23:01.653510
# Keep-alive comment: 2025-08-14 22:22:54.846782
# Keep-alive comment: 2025-08-15 09:22:54.636233
# Keep-alive comment: 2025-08-15 20:22:44.029111
# Keep-alive comment: 2025-08-16 07:23:08.575476
# Keep-alive comment: 2025-08-16 18:22:55.421163
# Keep-alive comment: 2025-08-17 05:22:58.072405
# Keep-alive comment: 2025-08-17 16:22:53.365188
# Keep-alive comment: 2025-08-18 03:22:55.081656
# Keep-alive comment: 2025-08-18 14:22:56.354459
# Keep-alive comment: 2025-08-19 01:22:55.082136
# Keep-alive comment: 2025-08-19 12:23:01.009792
# Keep-alive comment: 2025-08-19 23:23:22.194851
# Keep-alive comment: 2025-08-20 10:22:57.145344
# Keep-alive comment: 2025-08-20 21:23:00.005583
# Keep-alive comment: 2025-08-21 08:22:56.549810
# Keep-alive comment: 2025-08-21 19:23:01.015318
# Keep-alive comment: 2025-08-22 06:23:00.197427
# Keep-alive comment: 2025-08-22 17:22:55.475630
# Keep-alive comment: 2025-08-23 04:23:04.446876
# Keep-alive comment: 2025-08-23 15:22:53.654692
# Keep-alive comment: 2025-08-24 02:22:53.799723
# Keep-alive comment: 2025-08-24 13:22:54.715221
# Keep-alive comment: 2025-08-25 00:23:00.994452
# Keep-alive comment: 2025-08-25 11:23:00.422656
# Keep-alive comment: 2025-08-25 22:22:54.919660
# Keep-alive comment: 2025-08-26 09:22:56.200776
# Keep-alive comment: 2025-08-26 20:23:00.342844
# Keep-alive comment: 2025-08-27 07:23:05.062207
# Keep-alive comment: 2025-08-27 18:22:35.207344
# Keep-alive comment: 2025-08-28 05:23:05.781537
# Keep-alive comment: 2025-08-28 16:22:55.420587
# Keep-alive comment: 2025-08-29 03:22:39.116631
# Keep-alive comment: 2025-08-29 14:22:45.848282
# Keep-alive comment: 2025-08-30 01:22:44.082132
# Keep-alive comment: 2025-08-30 12:22:39.820694
# Keep-alive comment: 2025-08-30 23:22:43.400871
# Keep-alive comment: 2025-08-31 10:22:39.443336
# Keep-alive comment: 2025-08-31 21:22:50.675731
# Keep-alive comment: 2025-09-01 08:22:54.016592
# Keep-alive comment: 2025-09-01 19:22:50.974711
# Keep-alive comment: 2025-09-02 06:22:39.680213
# Keep-alive comment: 2025-09-02 17:22:51.175515
# Keep-alive comment: 2025-09-03 04:22:43.537165
# Keep-alive comment: 2025-09-03 15:22:46.613177
# Keep-alive comment: 2025-09-04 02:22:48.606120
# Keep-alive comment: 2025-09-04 13:22:58.338910
# Keep-alive comment: 2025-09-05 00:22:39.879148
# Keep-alive comment: 2025-09-05 11:22:35.348932
# Keep-alive comment: 2025-09-05 22:22:44.594572
# Keep-alive comment: 2025-09-06 09:22:40.532460
# Keep-alive comment: 2025-09-06 20:22:39.788706
# Keep-alive comment: 2025-09-07 07:22:45.291248
# Keep-alive comment: 2025-09-07 18:22:45.271193
# Keep-alive comment: 2025-09-08 05:22:41.297685
# Keep-alive comment: 2025-09-08 16:22:46.721658
# Keep-alive comment: 2025-09-09 03:23:11.440023
# Keep-alive comment: 2025-09-09 14:22:46.995348
# Keep-alive comment: 2025-09-10 01:22:39.138438
# Keep-alive comment: 2025-09-10 12:22:51.337894
# Keep-alive comment: 2025-09-10 23:22:39.974856
# Keep-alive comment: 2025-09-11 10:22:42.805505
# Keep-alive comment: 2025-09-11 21:22:40.262219
# Keep-alive comment: 2025-09-12 08:22:55.122927
# Keep-alive comment: 2025-09-12 19:22:45.445632
# Keep-alive comment: 2025-09-13 06:22:33.583271
# Keep-alive comment: 2025-09-13 17:22:40.032312
# Keep-alive comment: 2025-09-14 04:22:30.066351
# Keep-alive comment: 2025-09-14 15:22:41.494501
# Keep-alive comment: 2025-09-15 02:22:39.112464
# Keep-alive comment: 2025-09-15 13:22:42.214963
# Keep-alive comment: 2025-09-16 00:22:40.246803
# Keep-alive comment: 2025-09-16 11:22:45.732533
# Keep-alive comment: 2025-09-16 22:22:39.346196
# Keep-alive comment: 2025-09-17 09:22:42.217899
# Keep-alive comment: 2025-09-17 20:22:51.487589
# Keep-alive comment: 2025-09-18 07:22:47.396815
# Keep-alive comment: 2025-09-18 18:22:46.886392
# Keep-alive comment: 2025-09-19 05:22:41.278731
# Keep-alive comment: 2025-09-19 16:23:16.117909
# Keep-alive comment: 2025-09-20 03:22:44.740146
# Keep-alive comment: 2025-09-20 14:22:46.374876
# Keep-alive comment: 2025-09-21 01:22:45.944562
# Keep-alive comment: 2025-09-21 12:22:45.582903
# Keep-alive comment: 2025-09-21 23:22:40.948776
# Keep-alive comment: 2025-09-22 10:22:43.645921
# Keep-alive comment: 2025-09-22 21:22:40.352339
# Keep-alive comment: 2025-09-23 08:22:42.975758
# Keep-alive comment: 2025-09-23 19:22:47.889138
# Keep-alive comment: 2025-09-24 06:22:41.239826
# Keep-alive comment: 2025-09-24 17:22:47.484818
# Keep-alive comment: 2025-09-25 04:24:58.795937
# Keep-alive comment: 2025-09-25 15:22:51.364356
# Keep-alive comment: 2025-09-26 02:22:46.909078
# Keep-alive comment: 2025-09-26 13:22:50.978823
# Keep-alive comment: 2025-09-26 19:31:17.912481
# Keep-alive comment: 2025-09-27 05:31:22.911043
# Keep-alive comment: 2025-09-27 15:31:17.547767
# Keep-alive comment: 2025-09-28 01:31:21.922477
# Keep-alive comment: 2025-09-28 11:31:23.369433
# Keep-alive comment: 2025-09-28 21:31:21.986878
# Keep-alive comment: 2025-09-29 07:31:29.133608
# Keep-alive comment: 2025-09-29 17:31:38.509809
# Keep-alive comment: 2025-09-30 03:31:17.028559
# Keep-alive comment: 2025-09-30 13:31:24.088086
# Keep-alive comment: 2025-09-30 23:31:41.985175
# Keep-alive comment: 2025-10-01 09:31:50.241531
# Keep-alive comment: 2025-10-01 19:31:23.279866
# Keep-alive comment: 2025-10-02 05:31:51.216947
# Keep-alive comment: 2025-10-02 15:31:48.998355
# Keep-alive comment: 2025-10-03 01:31:22.179882
# Keep-alive comment: 2025-10-03 11:31:43.265045
# Keep-alive comment: 2025-10-03 21:31:17.764314
# Keep-alive comment: 2025-10-04 07:31:17.307780
# Keep-alive comment: 2025-10-04 17:31:27.658931
# Keep-alive comment: 2025-10-05 03:31:21.820439
# Keep-alive comment: 2025-10-05 13:31:26.933264
# Keep-alive comment: 2025-10-05 23:31:47.385736
# Keep-alive comment: 2025-10-06 09:31:53.231934
# Keep-alive comment: 2025-10-06 19:31:26.033612
# Keep-alive comment: 2025-10-07 05:31:24.387135
# Keep-alive comment: 2025-10-07 15:31:46.328282
# Keep-alive comment: 2025-10-08 01:31:22.697604
# Keep-alive comment: 2025-10-08 11:31:24.492467
# Keep-alive comment: 2025-10-08 21:31:23.535805
# Keep-alive comment: 2025-10-09 07:31:26.607435
# Keep-alive comment: 2025-10-09 17:31:26.243602
# Keep-alive comment: 2025-10-10 03:31:13.049665
# Keep-alive comment: 2025-10-10 13:31:05.061228
# Keep-alive comment: 2025-10-10 23:31:17.746501
# Keep-alive comment: 2025-10-11 09:31:23.327790
# Keep-alive comment: 2025-10-11 19:31:17.025530
# Keep-alive comment: 2025-10-12 05:31:20.453387
# Keep-alive comment: 2025-10-12 15:31:25.651122
# Keep-alive comment: 2025-10-13 01:31:19.645661
# Keep-alive comment: 2025-10-13 11:31:51.081708
# Keep-alive comment: 2025-10-13 21:31:13.779881
# Keep-alive comment: 2025-10-14 07:31:18.049699
# Keep-alive comment: 2025-10-14 17:31:20.871686
# Keep-alive comment: 2025-10-15 03:31:17.992366
# Keep-alive comment: 2025-10-15 13:31:20.546949
# Keep-alive comment: 2025-10-15 23:31:23.925560
# Keep-alive comment: 2025-10-16 09:31:20.291413
# Keep-alive comment: 2025-10-16 19:31:26.110038
# Keep-alive comment: 2025-10-17 05:31:24.273479
# Keep-alive comment: 2025-10-17 15:31:41.195428
# Keep-alive comment: 2025-10-18 01:31:19.026841
# Keep-alive comment: 2025-10-18 11:31:43.550359
# Keep-alive comment: 2025-10-18 21:31:52.933549
# Keep-alive comment: 2025-10-19 07:31:13.023662
# Keep-alive comment: 2025-10-19 17:31:47.953943
# Keep-alive comment: 2025-10-20 03:31:46.605384
# Keep-alive comment: 2025-10-20 13:31:25.387480
# Keep-alive comment: 2025-10-20 23:31:18.768238
# Keep-alive comment: 2025-10-21 09:31:24.850110
# Keep-alive comment: 2025-10-21 19:33:26.168057
# Keep-alive comment: 2025-10-22 05:31:19.937491
# Keep-alive comment: 2025-10-22 15:32:25.265774
# Keep-alive comment: 2025-10-23 01:31:18.171956
# Keep-alive comment: 2025-10-23 11:31:31.459318
# Keep-alive comment: 2025-10-23 21:31:20.729100
# Keep-alive comment: 2025-10-24 07:32:39.620822
# Keep-alive comment: 2025-10-24 17:31:30.299644
# Keep-alive comment: 2025-10-25 03:31:23.605599
# Keep-alive comment: 2025-10-25 13:31:47.410471
# Keep-alive comment: 2025-10-25 23:31:19.745542
# Keep-alive comment: 2025-10-26 09:31:12.783681
# Keep-alive comment: 2025-10-26 19:31:49.734773
# Keep-alive comment: 2025-10-27 05:31:30.083727
# Keep-alive comment: 2025-10-27 15:31:46.093991
# Keep-alive comment: 2025-10-28 01:31:22.739640
# Keep-alive comment: 2025-10-28 11:31:25.249613
# Keep-alive comment: 2025-10-28 21:31:13.691459
# Keep-alive comment: 2025-10-29 07:31:20.410867
# Keep-alive comment: 2025-10-29 17:31:29.781875
# Keep-alive comment: 2025-10-30 03:31:19.516620
# Keep-alive comment: 2025-10-30 13:31:51.105131
# Keep-alive comment: 2025-10-30 23:31:25.055769
# Keep-alive comment: 2025-10-31 09:32:39.542681
# Keep-alive comment: 2025-10-31 19:31:14.549858
# Keep-alive comment: 2025-11-01 05:31:23.285051
# Keep-alive comment: 2025-11-01 15:31:12.238330
# Keep-alive comment: 2025-11-02 01:31:24.204000