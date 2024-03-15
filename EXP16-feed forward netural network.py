import math
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.weights_input_hidden = [[0.1 * (i + j) for j in range(hidden_size)] for i in range(input_size)]
        self.biases_hidden = [0.1 * i for i in range(hidden_size)]
        self.weights_hidden_output = [[0.1 * (i + j) for j in range(output_size)] for i in range(hidden_size)]
        self.biases_output = [0.1 * i for i in range(output_size)]
    def forward(self, inputs):
        hidden_layer_input = [0.0] * self.hidden_size
        hidden_layer_output = [0.0] * self.hidden_size
        output_layer_input = [0.0] * self.output_size
        output_layer_output = [0.0] * self.output_size
        for i in range(self.hidden_size):
            hidden_layer_input[i] = self.biases_hidden[i]
            for j in range(self.input_size):
                hidden_layer_input[i] += inputs[j] * self.weights_input_hidden[j][i]
        for i in range(self.hidden_size):
            hidden_layer_output[i] = 1 / (1 + math.exp(-hidden_layer_input[i]))
        for i in range(self.output_size):
            output_layer_input[i] = self.biases_output[i]
            for j in range(self.hidden_size):
                output_layer_input[i] += hidden_layer_output[j] * self.weights_hidden_output[j][i]
        for i in range(self.output_size):
            output_layer_output[i] = 1 / (1 + math.exp(-output_layer_input[i]))
        return output_layer_output
if __name__ == "__main__":
    input_size = 2
    hidden_size = 3
    output_size = 1
    nn = NeuralNetwork(input_size, hidden_size, output_size)
    inputs = [0.5, 0.3]
    output = nn.forward(inputs)
    print("Output:", output)
