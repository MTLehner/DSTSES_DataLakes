import torch
from torch import nn


class LSTM_model(nn.Module):

    def __init__(self,input_size,hidden_size,num_layers,device='cuda'):
        super().__init__()

        self.lstm = nn.LSTM(input_size,hidden_size,num_layers)
        self._hidden_size = hidden_size
        self._input_size = input_size
        self._num_layers = num_layers

        self._linear = nn.Linear(self._hidden_size,1)
        self._device = device
    
    def forward(self,input):

        h_0 = torch.zeros(self._num_layers,input.size(1),self._hidden_size,device=self._device)
        c_0 = torch.zeros(self._num_layers,input.size(1),self._hidden_size,device=self._device)
        output, (hn, cn) = self.lstm(input, (h_0,c_0))
        output = self._linear(output[-1, :, :])
        return output, (hn, cn)


class LSTM_model_sig(nn.Module):

    def __init__(self,input_size,hidden_size,num_layers,device='cuda'):
        super().__init__()

        self.lstm = nn.LSTM(input_size,hidden_size,num_layers)
        self._hidden_size = hidden_size
        self._input_size = input_size
        self._num_layers = num_layers

        self._linear = nn.Linear(self._hidden_size,1)
        self._device = device
        self.silu = nn.SiLU()
        self.sigmoid = nn.Sigmoid()
    
    def forward(self,input):

        h_0 = torch.zeros(self._num_layers,input.size(1),self._hidden_size,device=self._device)
        c_0 = torch.zeros(self._num_layers,input.size(1),self._hidden_size,device=self._device)
        output, (hn, cn) = self.lstm(input, (h_0,c_0))
        output = self._linear(output[-1, :, :])
        output = self.sigmoid(output)*4
        return output, (hn, cn)