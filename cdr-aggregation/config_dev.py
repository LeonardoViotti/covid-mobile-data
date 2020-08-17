from pyspark.sql.types import *
schema = StructType([
  StructField("msisdn", IntegerType(), True),
  StructField("call_datetime", StringType(), True), #load as string, will be turned into datetime in standardize_csv_files()
  StructField("location_id", StringType(), True)
])


datasource_configs = {
  "base_path": "/home/jovyan/work/data",
  "country_code": "ZW",
  "telecom_alias": "econet",
  "schema" : schema,
  "data_paths" : ["mar20/*.csv","feb20/*.csv"],
  "filestub":"febmar20",
  "spark_mode":"cluster",
  "geofiles": { "tower_sites":"zw_econet_sites.csv",
                "admin2":"zw_admin2_shapefile.csv",
                "admin3":"zw_admin3_shapefile.csv",
                "voronoi":"zw_voronoi_shapefile.csv",
                "admin2_tower_map":"zw_admin2_tower_map.csv",
                "admin3_tower_map":"zw_admin3_tower_map.csv",
                "voronoi_tower_map":"zw_voronoi_tower_map.csv",
                "voronoi_tower_map_harare":"zw_voronoi_tower_map_harare.csv",
                "voronoi_tower_map_bulawayo":"zw_voronoi_tower_map_bulawayo.csv",
                "distances" : "zw_distances_pd_long.csv",
                "admin2_incidence" : "zw_admin2_covid_incidence_march30.csv",
                "admin2_weight" : "zw_admin2_weight.csv",
                "admin3_weight" : "zw_admin3_weight.csv"},
  "shapefiles": ['admin2','admin3', 'voronoi'],
  "dates": {'start_date' : dt.datetime(2020,2,1),
            'end_date' : dt.datetime(2020,3,31)}}