from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_model(df) :
    # Prepare the data
    X = df[['SMA_10', 'SMA_50']]
    y = df['signal']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,)

    # Initialize and train the Random Forest Classifier
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Return the trained model
    return model