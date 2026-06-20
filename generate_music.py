import pickle
import numpy as np
from tensorflow.keras.models import load_model

# Load notes
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

# Load model
model = load_model("music_model.keras")

unique_notes = sorted(set(notes))

note_to_int = {
    note: number
    for number, note in enumerate(unique_notes)
}

int_to_note = {
    number: note
    for number, note in enumerate(unique_notes)
}

sequence_length = 50

# Pick a random starting point
start = np.random.randint(0, len(notes) - sequence_length)

pattern = notes[start:start + sequence_length]

generated_notes = []

for note_item in pattern:
    generated_notes.append(note_item)

for i in range(100):

    prediction_input = np.array(
        [[note_to_int[n] for n in pattern]]
    )

    prediction_input = prediction_input.reshape(
        (1, sequence_length, 1)
    )

    prediction_input = prediction_input / float(len(unique_notes))

    prediction = model.predict(
        prediction_input,
        verbose=0
    )

    index = np.argmax(prediction)

    result = int_to_note[index]

    generated_notes.append(result)

    pattern.append(result)

    pattern = pattern[1:]

print("Generated Notes:")
print(generated_notes)

# Save notes
with open("generated_notes.pkl", "wb") as f:
    pickle.dump(generated_notes, f)

print("Generated notes saved!")