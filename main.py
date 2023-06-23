from factories.TriangleFactory import TriangleFactory
import tensorflow as tf
import pandas as pd
triangle_factory = TriangleFactory()

def createDataset():
    triangles = triangle_factory.createTriangles(1_000_000)
    df = pd.DataFrame([triangle.to_dict() for triangle in triangles])
    df.to_csv('triangles.csv', index=False)


def trainNewModel():
    data = pd.read_csv('triangles.csv')

    features = data[['catetoUno', 'catetoDos']]
    labels = data[['hipotenusa']]

    datasetPercentageForTraining = 0.8
    train_size = int(datasetPercentageForTraining * len(features))
    train_features, train_labels = features[:train_size], labels[:train_size]
    test_features, test_labels = features[train_size:], labels[train_size:]

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(2,)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')

    epochsSize = 400
    model.fit(train_features, train_labels, epochs=epochsSize, batch_size=64)

    loss = model.evaluate(test_features, test_labels)
    print('Mean squared Error on test data: ', loss)

    model.save(f'trained_model_{epochsSize}_{loss}')

    new_data = pd.DataFrame({'catetoUno': [10, 20], 'catetoDos': [30, 40]})
    predictions = model.predict(new_data)
    print('Predicted hypotenuse: ', predictions)

if __name__ == '__main__':
    loaded_model = tf.keras.models.load_model('trained_model_400_0.0001872791617643088')

    # Use the loaded model to make predictions
    new_data = pd.DataFrame({'catetoUno': [50, 60], 'catetoDos': [70, 80]})
    predictions = loaded_model.predict(new_data)
    print('Predicted hypotenuse:', predictions)

