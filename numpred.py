import keras
from keras.layers import LSTM, Dense
from keras.models import Sequential

# Collect list of numbers from user
numbers = []
while True:
    number = int(input("Enter a number between 1 and 10, or type 'done' to finish: "))
    if number == "done":
        break
    elif 1 <= number <= 10:
        numbers.append(number)
    else:
        print("Invalid input. Please enter a number between 1 and 10.")

# Create and fit LSTM model
model = Sequential()
model.add(LSTM(10, input_shape=(1, 1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(numbers, epochs=1000, batch_size=1, verbose=0)

# Predict next number in the sequence
prediction = model.predict(numbers[-1])
print("Next number in the sequence: ", prediction[0][0])
