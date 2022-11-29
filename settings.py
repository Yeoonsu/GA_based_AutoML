## BPIC2012
caseid = 'Case ID'
activity = 'Activity'
ts = 'Complete Timestamp'
label = {'Activity' : 'O_ACCEPTED-COMPLETE'}
other_features = ['Resource', 'Variant index', '(case) AMOUNT_REQ']

## BPIC2017
# caseid = 'Case ID'
# activity = 'Activity'
# ts = 'Complete Timestamp'
# label = {'column' : 'Accepted'}
# other_features = ['Resource', 'CreditScore', 'FirstWithdrawalAmount', 'MonthlyCost', 'NumberOfTerms','OfferedAmount']

## BPIC2015
# caseid = 'Case ID'
# activity = 'Activity'
# ts = 'Complete Timestamp'
# label = {'column' : 'Label'}
# other_features = ['Resource', 'monitoringResource', '(case) Includes_subCases','(case) Responsible_actor','(case) caseProcedure','(case) caseStatus','(case) last_phase','(case) parts',
#                 '(case) requestComplete','(case) termName', '(case) SUMleges']

combi = ['bucketing', 'encoding', 'drop_act', 'params']

options = {
    'bucketing' : (1,40), # a number of partitions
    
    'encoding' : ['index', 'aggregate'],
    
    'drop_act' : [2,4,6,8], # a number of activities to drop
    
    'models' : ['Decision Tree','Random Forest','LightGBM','Xgboost'],

    'params' : {'Decision Tree':{'max_depth': (2,20),
                           'min_samples_leaf': (5,100),
                           'criterion': ["gini", "entropy"]
            }, 
            'Random Forest':{"n_estimators": (10,1000), 
                           "max_depth": (2,20),
                           "max_features": ["auto", "log2"], 
                           "bootstrap": [True, False],
                           "criterion": ["gini", "entropy"]
            },
            'LightGBM':{'max_depth': (2,20),
                      'num_leaves' : (10,500),
                      'min_child_samples' : (2,10)
            },
            'Xgboost':{"max_depth": (2,20),
                     "n_estimators": (10,1000),
                     "learning_rate": [0.01, 0.05, 0.1]
                     
            }
            }
}