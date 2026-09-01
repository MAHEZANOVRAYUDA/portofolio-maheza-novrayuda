# Content Strategy — Isi Ulang Konten Portofolio

Tujuan: mengganti semua placeholder generik dengan narasi yang jujur, spesifik, dan mencerminkan Maheza Novrayuda sebagai mahasiswa Informatika yang fokus AI/Data. Rekruter dan Google sama-sama menyukai konten yang **spesifik**, bukan buzzword kosong.

## 1. Instruksi untuk Antigravity

Buat **Django data migration** atau **management command** (`portfolio/management/commands/seed_profile.py`) yang mengisi/update model `Profile`, `Skill`, `Achievement` dengan draf di bawah — **bukan hardcode ke template**, karena semua field ini sudah ada di model dan dikelola lewat Django Admin. Tujuannya supaya Maheza cukup edit lewat `/admin/` tanpa sentuh kode lagi ke depannya.

## 2. Draf `Profile` (edit sebelum publish)

```
name: Maheza Novrayuda
hero_title: AI & Data Engineering Enthusiast
bio: >
  Mahasiswa Teknik Informatika di Universitas Putra Indonesia YPTK Padang yang fokus
  membangun solusi data end-to-end — mulai dari data pipeline, analisis statistik,
  hingga model AI/Machine Learning siap produksi. Tertarik pada Generative AI (RAG),
  NLP, dan arsitektur data yang scalable.
about_long: >
  Saya mulai serius menekuni AI dan Data Science sejak semester awal kuliah, belajar
  lewat kombinasi kelas kampus, bootcamp (Dicoding Academy, CodePolitan), dan
  eksperimen mandiri di GitHub. Fokus saya ada di tiga area yang saling terkait:
  Data Engineering (pipeline & data cleaning), Data Science (analisis statistik &
  machine learning klasik), dan AI Engineering (deep learning & Generative AI/RAG).
  Saat ini saya sedang memperdalam sistem RAG (Retrieval-Augmented Generation) dan
  arsitektur data yang efisien untuk kasus dunia nyata.
location: Padang, Sumatera Barat, Indonesia
email: mahezanovrayuda@gmail.com   # pastikan email ini masih aktif & benar
github_url: https://github.com/MAHEZANOVRAYUDA
linkedin_url: https://www.linkedin.com/in/mahezanovrayuda
```

> ⚠️ **Wajib dikoreksi manual oleh Maheza**: nomor telepon, Instagram (jika mau ditampilkan), dan link resume/CV (upload PDF CV ke `/admin/` lalu isi `resume_link`).

## 3. Draf Skill (kategori sudah sesuai `Skill.Category` di model)

| Kategori | Skill |
|---|---|
| Languages | Python, SQL |
| Frameworks | Django, Streamlit, Flask, Pandas, NumPy, Scikit-learn, TensorFlow, Keras |
| ML/AI Tools | XGBoost, RAG Pipelines, LLM Integration, NLP, Matplotlib, Seaborn |
| Cloud/DevOps | PostgreSQL, MySQL, Git & GitHub, Vercel |

Setiap skill butuh file icon (SVG/PNG) — bisa ambil dari [Simple Icons](https://simpleicons.org/) (bebas pakai, tinggal unduh SVG resmi tiap tools).

## 4. Draf `Project` (isi dari repo GitHub publik kamu — sinkronkan deskripsi & link)

Untuk tiap project, isi field `github_link` dengan URL asli, `demo_link` jika ada demo Streamlit/live, dan `metrics` dengan angka nyata (akurasi, F1-score, dsb — ambil dari README masing-masing repo).

1. **RAG-BCA** — *featured=True*
   `Sistem Retrieval-Augmented Generation (RAG) yang menggabungkan Large Language Model dengan vector embedding untuk pencarian semantik dan question-answering berbasis dokumen.`
   github: `https://github.com/MAHEZANOVRAYUDA/RAG-BCA`

2. **CNN Cat vs Dog Classifier** — *featured=True*
   `Convolutional Neural Network untuk klasifikasi gambar kucing vs anjing, dengan optimisasi bobot model untuk mengurangi overfitting.`
   github: `https://github.com/MAHEZANOVRAYUDA/CNN_CatvDog`

3. **Real-time Sentiment Analysis**
   `Aplikasi NLP untuk mengklasifikasikan sentimen pengguna, dilengkapi antarmuka web interaktif.`
   github: `https://github.com/MAHEZANOVRAYUDA/SentimentAnalysis`

4. **Credit Risk Modeling** — *featured=True*
   `Pipeline machine learning untuk memprediksi probabilitas gagal bayar pinjaman, membantu keputusan kredit berbasis data.`
   github: `https://github.com/MAHEZANOVRAYUDA/Credit_Risk_Analysis`

5. **Home Pricing Regression (Streamlit)**
   `Proyek data science end-to-end memprediksi harga properti menggunakan regresi multivariat, dengan dashboard Streamlit interaktif.`
   github: `https://github.com/MAHEZANOVRAYUDA/Regression_HomePricingStreamlit`

6. **AI/ML Multi-Case Portfolio**
   `Kumpulan studi kasus AI/ML dunia nyata: exploratory data analysis, feature engineering, dan benchmarking model.`
   github: `https://github.com/MAHEZANOVRAYUDA/AI-ML_DL-Project-Portofolio`

> Tambahkan project lain (`DSF-dibimbing`, `data_wragling`, `End-to-end-machine-learning`) sebagai non-featured jika ingin portofolio terlihat lebih lengkap — tapi **kualitas > kuantitas**: lebih baik 6 project rapi dengan deskripsi jelas daripada 16 project tanpa konteks.

## 5. Prinsip copywriting untuk seluruh isi situs

- **Hindari klaim tanpa bukti** ("expert", "master") — pakai kata yang jujur untuk level mahasiswa: "fokus", "sedang mendalami", "membangun".
- Setiap project **wajib** punya: masalah yang diselesaikan → pendekatan teknis → hasil/metrik (walau sederhana).
- Judul halaman (`<title>`) dan meta description harus selalu memuat "Maheza Novrayuda" secara eksplisit (lihat `09-seo-strategy.md`).
- Bahasa konsisten: pilih satu — Bahasa Indonesia penuh, atau Inggris penuh, atau toggle language. Campur-aduk (seperti saat ini: judul "AI Engineer" bahasa Inggris tapi form Indonesia) membingungkan rekruter internasional maupun lokal.
