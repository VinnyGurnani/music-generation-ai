import pickle
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load notes
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

# Convert notes to numbers
unique_notes = sorted(set(notes))

note_to_int = {
    note: number
    for number, note in enumerate(unique_notes)
}

sequence_length = 50

network_input = []
network_output = []

for i in range(len(notes) - sequence_length):

    sequence_in = notes[i:i + sequence_length]
    sequence_out = notes[i + sequence_length]

    network_input.append(
        [note_to_int[note] for note in sequence_in]
    )

    network_output.append(
        note_to_int[sequence_out]
    )

n_patterns = len(network_input)

network_input = np.reshape(
    network_input,
    (n_patterns, sequence_length, 1)
)

network_input = network_input / float(len(unique_notes))

network_output = np.array(network_output)

print("Training Patterns:", n_patterns)

# Build Model

model = Sequential()

model.add(
    LSTM(
        128,
        input_shape=(network_input.shape[1], network_input.shape[2])
    )
)

model.add(Dense(len(unique_notes), activation="softmax"))

model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam"
)

model.fit(
    network_input,
    network_output,
    epochs=10,
    batch_size=64
)

model.save("music_model.keras")

print("Model saved successfully!")