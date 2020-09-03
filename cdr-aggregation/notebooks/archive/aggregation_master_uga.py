#!/usr/bin/env python
# coding: utf-8

# # Production of indicators for the COVID19 Mobility Task Force
# 
# In this notebook we produce indicators for the [COVID19 Mobility Task Force](https://github.com/worldbank/covid-mobile-data).
# 
# [Flowminder](https://covid19.flowminder.org) indicators are produced to increase the availability of comparable datasets across countries, and have been copied without modification from the [Flowminder COVID-19 github repository](https://github.com/Flowminder/COVID-19) (except for the start and end dates). These have been supplemented by a set of *priority* indicators with data for ingestion into the dashboard in this repository.
# 
# In this notebook we produce indicators in the following four steps:
# 
# - **Import code**: The code for the aggregation is included in the 'custom_aggregation' and 'flowminder_aggregation' scripts
# - **Import data**: 
# To set up the data import we need to place the CDR data files into the `data/new/CC/telco/` folder, where we replace `CC` with the country code and `telco` with the company abbreviation. 
# We also need to place csv files with the tower-region mapping and distance matrices into the `data/support-data/CC/telco/geofiles` folder, and then modify the `data/support_data/config_file.py` to specify:
#     - *geofiles*: the names of the geofiles, 
#     - *country_code*: country code and company abbreviation,
#     - *telecom_alias*: the path to the `data` folder,
#     - *data_paths*: the names to the subfolders in `data/new/CC/telco/` that hold the csv files. Simply change this to `[*]` if you didn't create subfolders and want to load all files.
#     - *dates*: set the start and end date of the data you want to produce the indicators for.
#     
# Find more information about the `config_file.py` settings see the [github page](https://github.com/worldbank/covid-mobile-data/tree/master/cdr-aggregation).
#     
# - **Run aggregations**: By default, we produce all flowminder and priority indicators. We've included 4 re-tries in case of failure, which we have experienced to help on databricks but is probably irrelevant in other settings. Note that before you can re-run these aggregations, you need to move the csv outputs that have been saved in `data/results/CC/telco/` in previous runs to another folder, else these indicators will be skipped. This prevents you from accidentally overwriting previous results. This way you can also delete the files only for the indicators you want to re-produce, and skip any indicatos you don't want to re-produce.
# 
# The outcome of this effort will be used to inform policy making using a [mobility indicator dashboard](https://github.com/worldbank/covid-mobile-data/tree/master/dashboard-dataviz).




# In[2]:


from modules.DataSource import *


# In[3]:


config_file = '../config_file.py'


# In[4]:


exec(open(config_file).read())


# In[5]:


ds = DataSource(datasource_configs)
ds.show_config()


# In[6]:


from modules.setup import *


# # Import data

# ## Load CDR data

# ### Process/standardize raw data, save as parquet, and then load it

# In[7]:


# ds.standardize_csv_files(show=True)
# ds.save_as_parquet()


# # In[ ]:


# ds.load_standardized_parquet_file()


# ### Alternatively, specify and load hive table

# In[ ]:


# # Specify and load hive data
# ds.parquet_df = ds.spark.sql("""SELECT {} AS msisdn, 
#                                        {} AS call_datetime, 
#                                        {} AS location_id FROM {}""".format(ds.hive_vars['msisdn'],
#                                                                            ds.hive_vars['call_datetime'],
#                                                                            ds.hive_vars['location_id'],
#                                                                            ds.hive_vars['calls']))


# ### Or load a sample file

# In[ ]:


## Use this in case you want to sample the data and run the code on the sample

# #ds.sample_and_save(number_of_ids=1000)
# ds.load_sample('sample_feb_mar2020')
# ds.parquet_df = ds.sample_df


# ## Load geo data

# In[ ]:


ds.load_geo_csvs()


# In[ ]:


## Use this in case you want to cluster the towers and create a distance matrix

# ds.create_gpds()
# from modules.tower_clustering import *
# clusterer = tower_clusterer(ds, 'admin2', 'ID_2')
# ds.admin2_tower_map, ds.distances = clusterer.cluster_towers()
# clusterer = tower_clusterer(ds, 'admin3', 'ADM3_PCODE')
# ds.admin3_tower_map, ds.distances  = clusterer.cluster_towers()


# In[ ]:


## Use this in case you want to create a voronoi tesselation

# from modules.voronoi import *
# voronoi = voronoi_maker(ds, 'admin3', 'ADM3_PCODE')
# ds.voronoi = voronoi.make_voronoi()


# # Run aggregations

