# Undersampling acak: buang sebagian kelas "no" sampai jumlahnya sama dengan kelas "yes".
# Dipakai di widget Python Script pada Orange (variabel in_data / out_data disediakan Orange).
# Sambungkan ke output "Data Sample" dari Data Sampler, JANGAN ke data uji.

import numpy as np

rng = np.random.default_rng(42)
y = in_data.Y
yes = in_data.domain.class_var.values.index("yes")
idx_yes = np.where(y == yes)[0]
idx_no = np.where(y != yes)[0]
keep_no = rng.choice(idx_no, size=len(idx_yes), replace=False)
keep = np.sort(np.concatenate([idx_yes, keep_no]))

out_data = in_data[keep]
print("yes:", len(idx_yes), "no sebelum:", len(idx_no), "total sesudah:", len(out_data))
