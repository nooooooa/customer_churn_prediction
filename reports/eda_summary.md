# Exploratory Data Analysis — Customer Churn

## 1. Customer Churn Distribution
- Total customers: 7043
- Churned customers: 1869
- Churn rate: 26.54%
- Key finding: Sebagian besar pelanggan masih bertahan, tetapi tingkat churn tetap perlu diperhatikan oleh perusahaan.

## 2. Customer Churn by Contract
- Contract with highest churn: Month-to-month
- Key finding: Pelanggan dengan komitmen berlangganan jangka pendek cenderung lebih mudah meninggalkan layanan.

## 3. Customer Tenure Distribution
- Average tenure of churned customers: 17.98 %
- Average tenure of retained customers: 37.57%
- Key finding: Pelanggan yang mengalami churn memiliki rata-rata tenure lebih rendah dibandingkan pelanggan yang masih bertahan. Hal ini mengindikasikan bahwa pelanggan baru mungkin lebih rentan meninggalkan layanan.

## 4. Monthly Charges by Churn
- Average monthly charges of churned customers: 74.44%
- Average monthly charges of retained customers: 61.27%
- Key finding: Pelanggan yang berhenti berlangganan cenderung membayar biaya bulanan yang lebih tinggi dibandingkan pelanggan yang tetap bertahan.

## 5. Numerical Correlation
- Strongest positive correlation: Tenure - TotalChanges, MonthlyCharges - TotalCharges
- Strongest negative correlation: Tenure - SeniorCitizen
- Key finding: pelanggan yang sudah lama berlangganan cenderung memiliki total biaya yang lebih besar, pelanggan dengan biaya bulanan lebih tinggi cenderung memiliki total pengeluaran lebih besar. 

## 6. Business Recommendations
1. Meningkatkan Retensi Pelanggan untuk Kontrak Bulanan

Pelanggan dengan kontrak bulanan memiliki tingkat *churn* tertinggi dibandingkan jenis kontrak lainnya. Perusahaan sebaiknya mempertimbangkan untuk menawarkan insentif, diskon, atau manfaat tambahan guna mendorong pelanggan beralih ke kontrak jangka panjang.

2. Memperkuat Program *Onboarding* dan Retensi Awal Pelanggan

Pelanggan yang berhenti berlangganan memiliki masa berlangganan rata-rata yang lebih singkat (17,98 bulan) dibandingkan pelanggan yang tetap bertahan (37,57 bulan). Perusahaan perlu mengembangkan program *onboarding* yang lebih baik, menyediakan dukungan pelanggan sejak awal, serta melakukan tindak lanjut secara berkala kepada pelanggan baru untuk meningkatkan retensi.

3. Mengevaluasi Penetapan Harga Bulanan dan Paket Layanan

Pelanggan yang berhenti berlangganan memiliki rata-rata biaya bulanan yang lebih tinggi (74,44) dibandingkan pelanggan yang tetap bertahan (61,27). Perusahaan sebaiknya mengevaluasi strategi penetapan harga, meninjau kembali paket layanan, dan menawarkan paket yang lebih fleksibel untuk memastikan pelanggan mendapatkan nilai yang sepadan dengan pengeluaran mereka.

Kesimpulan

Hasil EDA menunjukkan bahwa jenis kontrak, masa berlangganan, dan biaya bulanan merupakan faktor penting yang perlu diteliti lebih lanjut untuk memahami fenomena *churn* pelanggan. Temuan ini dapat membantu perusahaan dalam menyusun strategi retensi pelanggan yang lebih tepat sasaran. Analisis lebih mendalam dan pemodelan prediktif diperlukan untuk mengidentifikasi pelanggan yang memiliki risiko lebih tinggi untuk berhenti berlangganan.