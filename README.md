# GATE Exam Helper AI Agent

A smart AI-powered assistant for GATE aspirants — get crisp explanations, key points, code samples, summaries, and interactive doubt-solving for **AI, CSE, EE, ECE, Civil, ME** branches.

---

## 🛠️ Tech Stack

- **Python** (core implementation)
- **CrewAI** (AI workflow and agent orchestration)
- **Gemini 2.5 Flash (via API key)** (LLM for fast, powerful, accurate responses)
- **Streamlit** (for chatbot UI)

---

## 🚦 How It Works

1. **Enter your GATE branch** (AI, CSE, EE, ECE, Civil, ME)
2. **Enter the topic you want to study**
3. **Get output:**
    - **Explanation** of the topic
    - **Code sample** (if available)
    - **Short summary**
    - **Key points/highlights**
    - **Chatbot interface** for instant follow-up doubts

---

## ⚡ Sample Usage

### CLI

```bash
python main.py --branch cse --topic "Dijkstra's Algorithm"
```

### Web UI (Streamlit)

- Run with:  
  ```bash
  streamlit run app.py
  ```
- Open your browser at [http://localhost:8501](http://localhost:8501)  
- Select **Branch** (AI, CSE, EE, ECE, Civil, ME)
- Enter **Topic** (e.g., “Ohm’s Law”)
- Get a full AI-guided output and chat

---

## 🌟 Example Output

> **Branch:** EE  
> **Topic:** Ohm’s Law  
> **Explanation:**  
> Ohm’s Law states that the current through a conductor between two points is directly proportional to the voltage across the two points...
>  
> **Code (if applicable):**
> ```python
> V = I * R
> ```
>
> **Summary:**  
> Voltage = Current × Resistance  
>
> **Key Points:**  
> - Fundamental law in electrical engineering
> - Linear relationship: V = IR
> - Applicable only to ohmic materials  
>
> **Chatbot:**  
> _Type your follow-up question: “Where does Ohm’s Law not apply?”_

---

## 📝 Quickstart

1. **Clone the repo**
    ```bash
    git clone https://github.com/yourusername/gate-exam-helper-ai.git
    cd gate-exam-helper-ai
    ```

2. **Set Google Gemini API Key**
    - [Get API key here](https://aistudio.google.com/app/apikey)
    - Add to `.env`:  
      ```
      GEMINI_API_KEY=your-key-here
      ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit UI**
    ```bash
    streamlit run app.py
    ```

---

## 🤖 Features

- Quick, accurate topic explanations for **AI, CSE, EE, ECE, Civil, ME**
- Code auto-generation (for coding topics)
- Bullet-point summaries & key concepts
- Instantly ask detailed or follow-up exam questions to the chatbot
- Open source and customizable

---

## 🤝 Contributing

1. Fork and clone this repo
2. Create a feature branch
3. Push your changes and open a PR
4. All branches/topics welcome!

---

**Supercharge your GATE prep: Learn, code, revise, and clear every doubt!**
