#%% Pipeline 


ml_pipe = Pipeline([
    ('col selector', ColumnSelectorTransformer(columns=cols_to_keep)),
    ('bins', BinningTransformer(bins=bins)),
    ('woe', WOETransformer(columns=cols_to_keep)),
    # ('logistic regression', LogisticRegression(random_state=seed))
    ('gdbt', GradientBoostingClassifier(random_state=seed))
])

#%% Target Variable

y_train_nd = [1 if val==0 else 0 for val in y_train.values]
ml_pipe.fit(x_train, y_train_nd)

ml_pipe.score(x_train, y_train_nd)

ml_pipe.predict_proba(x_train)

y_pred = ml_pipe.predict(x_train)

fpr, tpr, threshold = roc_curve(y_train_nd, ml_pipe.predict_proba(x_train)[:, 1])
roc_auc = auc(fpr, tpr)
f1 = f1_score(y_train_nd, y_pred)
print(f"ROC AUC: {roc_auc}")
print(f"F1: {f1}")