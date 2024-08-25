from dyca import dyca
#from app.dyca.src.dyca import dyca, reconstruction
import numpy as np

dummy_data = np.random.rand(1000, 20)
result = dyca(dummy_data, 2, 3)