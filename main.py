from datetime import datetime, timedelta

import pandas as pd
import streamlit as st

# from mitosheet.streamlit.v1 import spreadsheet
# from mitosheet.streamlit.v1.spreadsheet import _get_mito_backend

st.set_page_config(layout="wide")

@st.cache_data
def get_collection_data():
    df = pd.read_csv('https://raw.githubusercontent.com/juststampit/bos-dao-airdrop/main/data/final/collections.csv')
    df = df.drop('count_all_nft_holders.collection_count.csv', axis=1)
    # df['volume'] = df['volume'].astype(float)
    return df

@st.cache_data
def get_token_data():
    df = pd.read_csv('https://raw.githubusercontent.com/juststampit/bos-dao-airdrop/main/data/final/tokens.csv')
    df = df.drop('eligible', axis=1)
    # df['volume'] = df['volume'].astype(float)
    return df

@st.cache_data
def get_alloc_data():
    df = pd.read_csv('https://raw.githubusercontent.com/juststampit/bos-dao-airdrop/main/data/final/BOS.draft.csv')
    df = df[['address', 'Eligible Tokens Held', 'SPAD_Bonus', 'ALLOC_1', 'BOOK OF STAMPS', 'ALLOC_2', 'stamp_count_unique', 'ALLOC_3', 'TOTAL ALLOC']]
    # df['volume'] = df['volume'].astype(float)
    return df

@st.cache_data
def get_merged_data():
    df = pd.read_csv('https://raw.githubusercontent.com/juststampit/bos-dao-airdrop/main/data/final/merged.csv')
    #df = df[['address', 'Eligible Tokens Held', 'SPAD_Bonus', 'ALLOC_1', 'BOOK OF STAMPS', 'ALLOC_2', 'stamp_count_unique', 'ALLOC_3', 'TOTAL ALLOC']]
    # df['volume'] = df['volume'].astype(float)
    # pr = df.profile_report()

    return df

collection_data = get_collection_data()
token_data = get_token_data()
alloc_data = get_alloc_data()
merged_data = get_merged_data()

# new_dfs, code = spreadsheet(collection_data)
st.subheader('STAMP Collection Data', divider='red')

st.dataframe(collection_data, use_container_width=True)

st.subheader('SRC20 Collection Data', divider='red')

st.dataframe(token_data, use_container_width=True)

st.subheader('BOS Allocations Calculated', divider='red')

st.dataframe(alloc_data, use_container_width=True)

with st.expander("See explanation"):
    st.dataframe(merged_data, use_container_width=True)

# code = code if code else "# STAMP Collection Data"
# st.code(code)

#def clear_mito_backend_cache():
#    _get_mito_backend.clear()

# Function to cache the last execution time - so we can clear periodically
# @st.cache_resource
# def get_cached_time():
#     # Initialize with a dictionary to store the last execution time
#     return {"last_executed_time": None}

# def try_clear_cache():

#     # How often to clear the cache
#     CLEAR_DELTA = timedelta(hours=12)

#     current_time = datetime.now()
#     cached_time = get_cached_time()

#     # Check if the current time is different from the cached last execution time
#     if cached_time["last_executed_time"] is None or cached_time["last_executed_time"] + CLEAR_DELTA < current_time:
#         clear_mito_backend_cache()
#         cached_time["last_executed_time"] = current_time

# try_clear_cache()
