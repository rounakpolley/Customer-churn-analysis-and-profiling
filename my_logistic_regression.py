from sklearn.linear_model import LogisticRegression

def run_logistic_regression(X_train, y_train, X_test, y_test): # y_test has no use here

    logreg	= LogisticRegression().fit(X_train,y_train)
    y_pred_train= logreg.predict(X_train)
    y_pred_test = logreg.predict(X_test)               
    
    return y_pred_train, y_pred_test     
