class DecisionTreeClassifier:
    def __init__(self):
        self.tree = None
    def fit(self, X, y):
        self.tree = self._grow_tree(X, y)
    def _grow_tree(self, X, y):
        # Base case: If all labels are the same, return a leaf node with that label
        if len(set(y)) == 1:
            return {'label': y[0]}

        # Base case: If there are no features left to split on, return a leaf node with the most common label
        if len(X[0]) == 0:
            return {'label': max(set(y), key=y.count)}

        # Find the best split point
        best_split = self._find_best_split(X, y)

        # Split the dataset based on the best split point
        left_indices = [i for i, x in enumerate(X) if x[best_split['feature_index']] <= best_split['threshold']]
        right_indices = [i for i, x in enumerate(X) if x[best_split['feature_index']] > best_split['threshold']]

        # Recursively grow the left and right subtrees
        left_subtree = self._grow_tree([X[i] for i in left_indices], [y[i] for i in left_indices])
        right_subtree = self._grow_tree([X[i] for i in right_indices], [y[i] for i in right_indices])

        # Construct the node representing the best split
        return {
            'feature_index': best_split['feature_index'],
            'threshold': best_split['threshold'],
            'left': left_subtree,
            'right': right_subtree
        }

    def _find_best_split(self, X, y):
        best_split = {'feature_index': None, 'threshold': None, 'gini': float('inf')}
        n_features = len(X[0])

        for feature_index in range(n_features):
            thresholds = sorted(set(x[feature_index] for x in X))
            for threshold in thresholds:
                left_indices = [i for i, x in enumerate(X) if x[feature_index] <= threshold]
                right_indices = [i for i, x in enumerate(X) if x[feature_index] > threshold]

                gini = self._gini_impurity([y[i] for i in left_indices]) + self._gini_impurity([y[i] for i in right_indices])
                if gini < best_split['gini']:
                    best_split = {'feature_index': feature_index, 'threshold': threshold, 'gini': gini}

        return best_split

    def _gini_impurity(self, y):
        counts = {}
        for label in y:
            counts[label] = counts.get(label, 0) + 1
        probabilities = [count / len(y) for count in counts.values()]
        return 1 - sum(p**2 for p in probabilities)

    def predict(self, X):
        return [self._predict_tree(x, self.tree) for x in X]

    def _predict_tree(self, x, node):
        if 'label' in node:
            return node['label']
        if x[node['feature_index']] <= node['threshold']:
            return self._predict_tree(x, node['left'])
        else:
            return self._predict_tree(x, node['right'])

# Sample usage
if __name__ == "__main__":
    # Sample dataset (dummy data)
    X_train = [[2, 4], [5, 1], [3, 3], [7, 2], [8, 9]]
    y_train = [0, 1, 0, 1, 1]

    # Initialize and train the decision tree classifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Make predictions on new data
    X_test = [[4, 5], [6, 3]]
    predictions = clf.predict(X_test)
    print("Predictions:", predictions)
