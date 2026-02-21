1. removed sigmoid from scout output letting it to be unbounded and then apply sigmoid at the loss boundary, Sigmoid should be applied once, at the loss function, not inside the model.
2. adding weighted bce loss
3. reduced model size, because i dont have that much data
4. trying to increase dropout because the model is overfitting
5. adding weight decay in adam
6. I changed the attn_output but changing the normalization from sqrt(N) to actual row_sum that happened in that pass
7. I tried expanding the space of 1X1 Conv but it didnt helped '''
nn.Conv2d(nhead, nhead * 4, kernel_size=1),
nn.GELU(),
nn.Conv2d(nhead * 4, 1, kernel_size=1)
'''
