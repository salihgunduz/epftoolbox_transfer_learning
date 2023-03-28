# epftoolbox transfer learning
#### This is the modified version of the epftoobox for transfer learning applications.

The library has been developed as part of the following article:

- Gunduz Salih, Ugurlu Umut and Oksuz Ilkay. "Transfer learning for electricity price forecasting." [https://doi.org/10.1016/j.segan.2023.100996](https://doi.org/10.1016/j.segan.2023.100996).

At first, we selected the best DNN models from [Lago et. al. (2021)](https://doi.org/10.1016/j.apenergy.2021.116983.) for the Belgium(DNN 4) and France(DNN 3) target markets. 
We applied transfer learning from Belgium to France and France to Belgium. 
Then, we performed transfer learning from Germany to France and Belgium to show contribution changes, when input features are diverse (Belgium and France have similar exogenous features, Germany has diverse features). Overall transfer between France and Belgium is generating better results when compared to using Germany as a source market.

We also selected the French market for detailed analysis on all DNN models suggested in [Lago et. al. (2021)](https://doi.org/10.1016/j.apenergy.2021.116983.). We applied transfer learning to all four models of the French market.Fine-tuning has shown a statistically significant performance increase for all models with the exception of DNN 4. 

Just for now, testing with saved models is available. 
Pre-training and fine-tuning classes are orginizing in a generic way. We will share them in the short term.  


## Getting started
Download the repository and navigate into the folder
```bash
! git clone https://github.com/salihgunduz/epftoolbox_transfer_learning.git
! cd epftoolbox_transfer_learning
```

Install using pip
```bash
! pip install .
```
Navigate to the examples folder and produce predictions by running  testing_finetune_simplified.py” file.

Colab test notebook: [https://colab.research.google.com/drive/1MtaZsqLSjmXLRXfRE15wKSfcwgXVN_Ri?usp=sharing](https://colab.research.google.com/drive/1MtaZsqLSjmXLRXfRE15wKSfcwgXVN_Ri?usp=sharing)


# Namings and forecasts
In "testing_finetune_simplified.py" file, we can set parameters below:

* source
* target
* DNN_id
* experiment_id
* hyperparameter_file_name

 
By running the code below new forecasts can be produced. Forecasts are saved to "examples/experimental_files"

```bash
! python testing_finetune_simplified.py --target="FR" --source="BE"  --DNN_id="3" --experiment_id="1" --hyperparameter_file_name="DNN_hyperparameters_nl2_datFR_YT2_SF_SF_CW4_1"
```

Saved models are in examples/saved_models folder. Saved models' names are formatted as below:

#### "target_source_dnnId_FT_experimentId_testDayIndex.h5"  

where FT means fine-tuned. The pre-treained models will be given as PT. hyperparameter_file_name can be copied from the folder "experimental_files". For example for Belgium DNN 4 is:
#### "DNN_hyperparameters_nl2_datBE_YT2_SF_SF_DA_CW4_1"

For example to forecasting 01.01.2016 in Belgium market with DNN 4,  "BE_FR_4_FT/BE_FR_4_FT_1_1.h5" model is used. There are also random shuffle indexes files for each test day in the same folder  for producing same results. New Forecasts are in "forecasts" folder. They are are named like :

#### "target_source_dnnId_FT_MAE.xlsx"  


