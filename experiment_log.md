1. Was using MSE , but I think BCE would be a better choice
2. Gonna split my data in validation set and training set and train the model based on that instead of when loss decreases
3. I can see the model was stopping learning after 10-15 epochs so adding a scheduler in learning rate so that my learning rate changes when the model starts stagnating