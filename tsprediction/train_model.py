"""
train_model module trains a LSTM model and saves the model in models folder.
pylint bug: https://github.com/pytorch/pytorch/issues/701
"""
import torch
from tsprediction.lstm_class import LSTM


def train_model(train_dataset_tuple, sequence_length, save_model=None, epochs=1000):
    """
    Parameters
    ----------
    train_dataset_tuple : tuple
        train_dataset_tuple[0]: input sequence : a tensor array
        train_dataset_tuple[1]: output sequence also we call it label sometimes : a tensor array
    sequence_length : int
        sequence length for input and output sequence
    save_model : boolean, optional
        The default is None. If true, saves model in models folder
    epochs : int, optional
        The default is 1000. Number of epochs we want to train the model

    Returns
    -------
    LSTM model and the loss

    """
    params = {}
    params["learning_rate"] = 0.01
    params["input_size"] = 1
    params["num_layers"] = 2
    params["hidden_size"] = sequence_length
    params["num_classes"] = sequence_length
    train_x, train_y = train_dataset_tuple

    lstm = LSTM(
        params["num_classes"],
        params["input_size"],
        params["hidden_size"],
        params["num_layers"],
    )

    dev = torch.device("cpu")
    if torch.cuda.is_available():
        dev = torch.device("cuda")
        print("GPU mode on :)")

    lstm = lstm.to(dev)
    criterion = torch.nn.MSELoss()  # mean-squared error for regression
    optimizer = torch.optim.Adam(lstm.parameters(), lr=params["learning_rate"])

    for epoch in range(epochs):
        train_x, train_y = train_x.to(dev), train_y.to(dev)
        outputs = lstm(train_x)
        optimizer.zero_grad()
        # obtain the loss function
        # print(outputs.shape)
        loss = criterion(outputs, train_y.view(train_y.shape[0], -1))

        loss.backward()

        optimizer.step()

        if epoch % 20 == 0:
            # print(outputs)
            # print(train_y.view(train_y.shape[0], -1))
            print("Epoch: %d, loss: %1.5f" % (epoch, loss.item()))
    if save_model:
        torch.save(lstm.state_dict(), "models/" + save_model)
    return lstm, loss.item()
