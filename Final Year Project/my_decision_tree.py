from sklearn.tree import DecisionTreeClassifier

def run_decission_tree(a, b, X_train, y_train, X_test, y_test, criteria, split_type, max_depth, min_split, min_leaf, return_dict):

    decision_tree = DecisionTreeClassifier(criterion = criteria, splitter = split_type, max_depth = max_depth, 
                                       min_samples_split = min_split , min_samples_leaf = min_leaf)
    decision_tree.fit(X_train, y_train)
    
    y_pred_train       = decision_tree.predict(X_train)
    y_pred_test        = decision_tree.predict(X_test)               
    
    return_dict[a]     = y_pred_train
    return_dict[b]     = y_pred_test