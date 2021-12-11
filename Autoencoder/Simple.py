import keras
def encode(encoding_dim=10 , customized_shape=(1166,),encode_activator='relu')->keras.Model:
    import keras
    input_data = keras.Input(shape=customized_shape)
    encoded = keras.layers.Dense(encoding_dim, activation=encode_activator)(input_data)

    decoded = keras.layers.Dense(24)(encoded)
    autoencoder = keras.Model(input_data,decoded)

    encoder = keras.Model(input_data, encoded)

    encoded_input = keras.Input(shape=(encoding_dim,))
    decoder_layer = autoencoder.layers[-1]

    decoder = keras.Model(encoded_input, decoder_layer(encoded_input))
    autoencoder.compile(optimizer='Adam',loss='mean_squared_error')
    
    return encoder

def decode(neuron=1166,encoder):
    import keras
    decoded = keras.layers.Dense(neuron)(encoder)

def build():
    import keras
    autoencoder.compile
    autoencoder.fit