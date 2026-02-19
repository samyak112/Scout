1. removed sigmoid from scout output letting it to be unbounded and then apply sigmoid at the loss boundary, Sigmoid should be applied once, at the loss function, not inside the model.
2. adding weighted bce loss
3. reduced model size, because i dont have that much data
4. trying to increase dropout because the model is overfitting
5. adding weight decay in adam
