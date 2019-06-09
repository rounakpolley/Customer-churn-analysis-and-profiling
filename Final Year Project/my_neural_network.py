from sklearn.neural_network import MLPClassifier

def run_nueral_network(a, b, X_train, y_train, X_test, y_test, _solver, _alpha, _layers, _max_iter, _random_state, return_dict):
    
    neural_network = MLPClassifier(solver=_solver, alpha=_alpha, hidden_layer_sizes=_layers, max_iter=_max_iter, verbose=False, 
                          warm_start=False, random_state=_random_state)
    neural_network.fit(X_train, y_train) 
    
    y_pred_train       = neural_network.predict(X_train)
    y_pred_test        = neural_network.predict(X_test)               
    
    return_dict[a]     = y_pred_train
    return_dict[b]     = y_pred_test