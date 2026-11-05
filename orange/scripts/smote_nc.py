# SMOTE-NC: buat sampel sintetis kelas "yes" (untuk data campuran numerik + kategorikal).
# Dipakai di widget Python Script pada Orange (variabel in_data / out_data disediakan Orange).
# Sambungkan ke output "Data Sample" dari Data Sampler, JANGAN ke data uji.

import numpy as np
from Orange.data import Table
from imblearn.over_sampling import SMOTENC

X = in_data.X
y = in_data.Y.astype(int)
cat_idx = [i for i, a in enumerate(in_data.domain.attributes) if a.is_discrete]

X_res, y_res = SMOTENC(categorical_features=cat_idx, random_state=42).fit_resample(X, y)

out_data = Table.from_numpy(in_data.domain, X_res, y_res.astype(float))
print("kolom kategorikal:", cat_idx)
print("sebelum:", np.bincount(y), "sesudah:", np.bincount(y_res))
