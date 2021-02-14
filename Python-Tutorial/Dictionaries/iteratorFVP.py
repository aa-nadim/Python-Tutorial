from collections import OrderedDict 
  
statesAndCapitals = OrderedDict([ 
                                 ('Gujarat', 'Gandhinagar'), 
                                 ('Maharashtra', 'Mumbai'), 
                                 ('Rajasthan', 'Jaipur'), 
                                 ('Bihar', 'Patna') 
                                ]) 
                      
print('List Of given states:\n') 
  
# Iterating over keys 
for state in statesAndCapitals: 
    print(state)