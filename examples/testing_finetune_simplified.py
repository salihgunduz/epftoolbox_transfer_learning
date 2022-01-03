"""
Simplified example for using the DNN model for forecasting prices with daily recalibration
"""

# Author: Jesus Lago

# License: AGPL-3.0 License

from epftoolbox.models import evaluate_finetune_in_test_dataset
import os
import argparse


# ------------------------------ EXTERNAL PARAMETERS ------------------------------------#

parser = argparse.ArgumentParser()

parser.add_argument("--target", type=str, default='FR', 
                    help='target market we want to predict')

parser.add_argument("--source", type=str, default='BE', 
                    help='source market we pre-trained the model.')

parser.add_argument("--DNN_id", type=str, default='1', 
                    help='DNN model"s index 1 to 4 (Models in the Lago et. al. (2021))')

parser.add_argument("--experiment_id", type=str, default='1', 
                    help='Unique identifier to read the saved models')

parser.add_argument("--hyperparameter_file_name", type=str, default='DNN_hyperparameters_nl2_datFR_YT2_SF_CW4_1', 
                    help='Unique identifier to read the saved models')


args = parser.parse_args()

dataset = args.dataset
years_test = args.years_test
calibration_window = args.calibration_window
begin_test_date = args.begin_test_date

# Market under study. If it not one of the  standard ones, the file name
# has to be provided, where the file has to be a csv file

# target market we want to predict.
target = args.target
# source market we pre-trained the model.
source = args.source
# DNN model's index 1 to 4 (Models in the Lago et. al. (2021))
DNN_id = args.DNN_id
# Unique identifier to read the saved models.
experiment_id = args.experiment_id
hyperparameter_file_name = args.hyperparameter_file_name


######  #  #    # ######  ###
#       #   #  #  #       #  #
####    #    ##   ######  #   #
#       #   #  #  #       #  #
#       #  #    # ######  ###

# Number of years (a year is 364 days) in the test dataset.
years_test = 2
# Number of layers in DNN
nlayers = 2
# Boolean that selects whether the validation and training datasets were shuffled when
# performing the hyperparameter optimization. Note that it does not select whether
# shuffling is used for recalibration as for recalibration the validation and the
# training datasets are always shuffled.
shuffle_train = 1

# Boolean that selects whether a data augmentation technique for DNNs is used
data_augmentation = 1

# Boolean that selects whether we start a new recalibration or we restart an existing one
new_recalibration = 1

# Number of years used in the training dataset for recalibration
calibration_window = 1

# Unique identifier to read the trials file of hyperparameter optimization
experiment_id = 1
# Optional parameters for selecting the test dataset, if either of them is not provided,
# the test dataset is built using the years_test parameter. They should either be one of
# the date formats existing in python or a string with the following format
# "%d/%m/%Y %H:%M"
begin_test_date = '01/01/2016'
end_test_date = '31/12/2016'

# Set up the paths for saving data (this are the defaults for the library)
path_datasets_folder = os.path.join('.', 'datasets')
path_recalibration_folder = os.path.join('.', 'experimental_files')
path_hyperparameter_folder = os.path.join('.', 'experimental_files')


evaluate_finetune_in_test_dataset(experiment_id, path_hyperparameter_folder=path_hyperparameter_folder,
                                  path_datasets_folder=path_datasets_folder, shuffle_train=shuffle_train,
                                  path_recalibration_folder=path_recalibration_folder,
                                  hyperparameter_file_name=hyperparameter_file_name,
                                  DNN_id=DNN_id, target=target, source=source,
                                  nlayers=nlayers, dataset=target, years_test=years_test,
                                  data_augmentation=data_augmentation, calibration_window=calibration_window,
                                  new_recalibration=new_recalibration, begin_test_date=begin_test_date,
                                  end_test_date=end_test_date)
