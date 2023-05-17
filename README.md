# Algae bloom prediction

## Motivation
This repo is a mini project for the course Data Science in Techno-Socio-Economic Systems (FS2023) at ETH Zurich. The goal is to predict algae blooms in swiss lakes using machine learning.

## Data
All data is from the swiss data-lakes project by EAWAG (https://www.datalakes-eawag.ch). For ease of use, we have included some of the used data in this repo with the corresponding import scripts.

## Predictions and models
The goal was to predict algae blooms ahead of time. Therefore multiple models were trained and tested over different time spans (predicting 7, 14 and 21 days ahead). The models used were:
- Lasso regression
- Ridge regression
- Bayesian ridge regression
- ARD regression
- MLP model
- LSTM model

Input features were a window of the last 7 days with the past algae concentration and in some models temperature, pH and oxygen concentration. 

## Results
Can be found in the ppp presentation or the corresponding jupyter notebooks.
