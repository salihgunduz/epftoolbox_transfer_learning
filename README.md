# epftoolbox transfer learning

This toolbox is the modified version of the epftoobox for transfer learning applications. 

First, we select the best DNN models for the Belgium(DNN 4) and France(DNN 3) target markets. We applied transfer learning from Belgium to France and France to Belgium. Then, we perform transfer learning from Germany to France and Belgium to show contribution changes, when input features are diverse (Belgium and France have similar exogenous features, Germany has diverse features). Overall transfer between France and Belgium is generating better results when compared to using Germany as a source market.

We also selected the French market for detailed analysis on all DNN models suggested in Lago et al. (2021). We applied transfer learning to all four models of the French market.Fine-tuning has shown a statistically significant performance increase for all models with the exception of DNN 4. 

# Namings and testing
Anyone can test and produce predictions by running  “transfer_learning_test.py” file.  In this file, we can set source, target, DNN_id and hyperparameter_file_name parameters. Saved models are in examples/saved_models folder. Saved models' names are formatted as below:

"target_source_DNNid_FT_experimentid_testday.h5" 

For example to forecasting 01.01.2016 in Belgium market with DNN 4,  "BE_FR_4_FT_1_1.h5" model is used. There are also random shuffle indexes files for each test day in the same folder  for producing same results. 






Just for now, testing with saved models is available. 
Pre-training and fine-tuning classes are orginising in a genereric way. We will share them in the short term.  

