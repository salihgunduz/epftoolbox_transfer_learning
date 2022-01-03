# epftoolbox transfer learning


The epftoolbox is the first open-access library for driving research in electricity price forecasting. Its main goal is to make available a set of tools that ensure reproducibility and establish research standards in electricity price forecasting research.

The library has been developed as part of the following article:

- Jesus Lago, Grzegorz Marcjasz, Bart De Schutter, Rafał Weron. "Forecasting day-ahead electricity prices: A review of state-of-the-art algorithms, best practices and an open-access benchmark". *Applied Energy* 2021; 293:116983. [https://doi.org/10.1016/j.apenergy.2021.116983](https://doi.org/10.1016/j.apenergy.2021.116983).

The library is distributed under the AGPL-3.0 License and it is built on top of scikit-learn, tensorflow, keras, hyperopt, statsmodels, numpy, and pandas. 

Website: [https://epftoolbox.readthedocs.io/en/latest/](https://epftoolbox.readthedocs.io/en/latest/) 

#### This is the modified version of the epftoobox for transfer learning applications.


First, we select the best DNN models for the Belgium(DNN 4) and France(DNN 3) target markets. 
We applied transfer learning from Belgium to France and France to Belgium. 
Then, we perform transfer learning from Germany to France and Belgium to show contribution changes, when input features are diverse (Belgium and France have similar exogenous features, Germany has diverse features). Overall transfer between France and Belgium is generating better results when compared to using Germany as a source market.

We also selected the French market for detailed analysis on all DNN models suggested in [Lago et. al. (2021)](https://doi.org/10.1016/j.apenergy.2021.116983.) We applied transfer learning to all four models of the French market.Fine-tuning has shown a statistically significant performance increase for all models with the exception of DNN 4. 

# Namings and testing
Anyone can test and produce predictions by running  “transfer_learning_test.py” file.  In this file, we can set source, target, DNN_id and hyperparameter_file_name parameters. Saved models are in examples/saved_models folder. Saved models' names are formatted as below:

"target_source_dnnId_FT_experimentId_testDay.h5"  

where FT means fine-tuned. The pre-treained models will be given as PT. hyperparameter_file_name can be copied from the folder "experimental_files". For example for Belgium DNN 4 is "DNN_hyperparameters_nl2_datBE_YT2_SF_SF_DA_CW4_1"

For example to forecasting 01.01.2016 in Belgium market with DNN 4,  "BE_FR_4_FT/BE_FR_4_FT_1_1.h5" model is used. There are also random shuffle indexes files for each test day in the same folder  for producing same results. New Forecasts are in "forecasts" folder. They are are named like :

"target_source_dnnId_FT_MAE.xlsx"  

Just for now, testing with saved models is available. 
Pre-training and fine-tuning classes are orginising in a genereric way. We will share them in the short term.  

