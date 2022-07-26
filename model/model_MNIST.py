import tensorflow as tf


def create_model_MNIST():
    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(28, 28, 1)),
            # tf.keras.layers.Rescaling(scale=1.0 / 255), Rescaling already done in the Preprocessing part
            tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )
    loss = tf.keras.losses.SparseCategoricalCrossentropy()
    optimizer = tf.keras.optimizers.Adam()
    metrics = [tf.keras.metrics.SparseCategoricalAccuracy()]
    return model, loss, optimizer, metrics


if __name__ == "__main__":
  model, _, _ , _ = create_model_MNIST()
  model.summary()
