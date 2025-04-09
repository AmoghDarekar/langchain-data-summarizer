# 🧠 AI-Powered Big Data Summarizer (LangChain + GPT)

This project lets you upload a large CSV dataset and get an **AI-generated summary** using **LangChain + OpenAI**.

---

## 📂 Features
- Summarizes large datasets (like NYC taxi data)
- Uses GPT to explain numeric trends and anomalies
- Easy-to-run Streamlit app

---

## ▶️ How to Run

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/langchain-data-summarizer.git
cd langchain-data-summarizer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
```

Or export it:

```bash
export OPENAI_API_KEY=your_key_here
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🧪 Sample Data

A sample CSV is included in `sample_data/nyc_taxi_sample.csv` for quick testing.

---

## 🧑‍💻 Built With

- [LangChain](https://www.langchain.com/)
- [OpenAI GPT](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)
