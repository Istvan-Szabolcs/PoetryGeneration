import numpy as np
import tensorflow as tf
import pickle
tf.random.set_seed(42)


models = {"Petőfi Sándor": tf.keras.models.load_model('models/petofi.mdl_wts.hdf5'),
          "Babits Mihály": tf.keras.models.load_model('models/babits.mdl_wts.hdf5'),
          "Karinthy Frigyes": tf.keras.models.load_model('models/karinthy.mdl_wts.hdf5')}


with open('models/tokenizer/tokenizer_magyar.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
max_id = len(tokenizer.word_index)

def complete_text(text, model_name, n_chars=50, temperature=1):
    model = models[model_name]
    def preprocess(texts):
        X = np.array(tokenizer.texts_to_sequences(texts)) - 1
        return tf.one_hot(X, 52)

    def next_char(text, temperature=1):
        X_new = preprocess([text])
        y_proba = model.predict(X_new)[0, -1:, :]
        rescaled_logits = tf.math.log(y_proba) / temperature
        char_id = tf.random.categorical(rescaled_logits, num_samples=1) + 1
        return tokenizer.sequences_to_texts(char_id.numpy())[0]

    for _ in range(n_chars):
        text += next_char(text, temperature)
    return text