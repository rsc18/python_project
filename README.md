# Sequence to Sequence Stock Time Series Data Prediction Model using PyTorch 

#### -- Project Status: [Active, On-Hold, Completed]
Active

## Project Intro/Objective
This repo contains the code base for predicting time series stock data. We will be using live stock data and feed them to the NN to train ehich will predict future stock values of given equity. We will be using LSTM for training. 

## Project Description
* Alpha- vantage: We will collect stock time series data using Alpha-vantage Time Series Stock API. 
* PyTorch: We will be using PyTorch library for building the Neural Network model with LSTM cells.
* LSTM: Long Short Term Memory (LSTM) is an artificial recurrent neural network architecture which is capable of learning order dependence in sequence prediction problem.
* Sequnce to Sequence Model: We will be building a sequence to sequence model with the LSTM cells. Here the input sequence would be a sequence of stock data of a specified equity and the output will be prediction of a future sequence of the same equity or some other equity. 

## Installability    
 * git clone https://github.com/rsc18/tsprediction.git
 * Run poetry install from root directory
 
## Usage

```
    Predict Stock CLI

    Usage:
        predict_stock.py alphavantage <companySymbol> <predictSequenceLength> [options]
        predict_stock.py custom <csvFileLocation> <predictSequenceLength> [options]
        predict_stock.py --help
        predict_stock.py --listcompanies -k <keywords>
 
    Options:
        -h --help                   help with predict_stock useage
        --plot= True/False          plot flag if true saves the plots in plot folder
        --saveModel= model-name     save_model flag if given saves the trained model with given model-name for future use
        -k <keywords>               search companies names using keyword
        --epochs = no-of-epochs     no of epochs

```
## Example
To list companies symbol that match keyword "micro" :
``` python predict_stock.py --listcompanies -k micro  ```       
To train a stock model with TSLA(Tesla) data.     
``` python predict_stock.py alphavantage TSLA 64 --saveModel=teslaModel --epochs=2000   ```      
To train a model with custom datasets.  
``` python predict_stock.py custom file.csv 9   ```       


### Technologies
* Python
* Pandas
* Spyder
* PyTorch
 

## Project Description
* Alpha- vantage: We will collect stock time series data using Alpha-vantage Time Series Stock API. 
* PyTorch: We will be using PyTorch library for building the Neural Network model with LSTM cells.
* LSTM: Long Short Term Memory (LSTM) is an artificial recurrent neural network architecture which is capable of learning order dependence in sequence prediction problem.
* Sequnce to Sequence Model: We will be building a sequence to sequence model with the LSTM cells. Here the input sequence would be a sequence of stock data of a specified equity and the output will be prediction of a future sequence of the same equity or some other equity. 


## Needs of this project

- data collection from stock API
- data processing/cleaning
- Deep learning library PyTorch with gpu support
- writeup/reporting



=======
### Partner
|Name     |  FSUID   |  FSU e-mail  |
|---------|-----------------|-------|
| Ram Sharan Chaulagain | RSC18 | rsc18@my.fsu.edu |
| Chashi Mahiul Islam | CI20L | ci20l@my.fsu.edu |

#### Project Supervisor:

|Name     |  github id   | 
|---------|-----------------|
|Piyush Kumar | pkfl |


