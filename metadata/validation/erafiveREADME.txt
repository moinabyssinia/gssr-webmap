-------------------------------------------------------------------------------------------------
Folder - surgeReconstructed					                           

contains daily maximum surge (m) time series for 841 tide gauges each "csv" file contains a time 
series that includes the lon/lat of the tide gauge and the 95% prediction interval for the surge    			   
estimation 							   			   
-------------------------------------------------------------------------------------------------
Surge reconstruction period:						   

01/1979 - 12/2019							   
-------------------------------------------------------------------------------------------------
Folder - metaData

contains the model validation results for each tide gauge carried out using the 10-fold cross 
validation technqiue. 						
												
tg         -> name of tide gauge								
lon/lat    -> longitude/latitude of tide gauge							
num_year   -> number of years used to validate models						
num_95_pcs -> principal components (explaining 95% of the variance in the predictors)		
corrn_lr   -> pearson correlation coefficient obtained when using linear regression model (MLR) 
rmse_lr    -> root mean square error (m) obtained when using linear regression model (MLR)	
corrn_rf   -> pearson correlation coefficient obtained when using random forest model (RF)	
rmse_rf    -> root mean sequare error (m) obtained when using random forest model (RF)		
bestModel  -> selected model based on error metrics
MLR        -> multiple linear regression model
RF         -> random forest model						
-------------------------------------------------------------------------------------------------
Model is based on: 						   

[Tadesse, M., Wahl, T., & Cid, A. (2020).Data-driven modeling of global storm surges.Frontiers 
in Marine Science, doi:http://dx.doi.org/10.3389/fmars.2020.00260]			   
-------------------------------------------------------------------------------------------------
Model trained with:						   

ERA5 data on single levels - 10m Uwnd; 10m Vwnd; mean sea-level pressure (slp)

Spatial resolution  -> 0.25°x0.25°		   		
Temporal resolution -> 1 hourly
https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview
-------------------------------------------------------------------------------------------------