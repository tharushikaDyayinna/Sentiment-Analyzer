{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dec3a4dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\dell\\anaconda\\lib\\site-packages (1.33.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (5.3.0)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (1.8.0)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (1.24.3)\n",
      "Requirement already satisfied: packaging<25,>=16.8 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (2.0.3)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (9.4.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (4.25.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (4.7.1)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (0.9.0b1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (6.3.2)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\dell\\anaconda\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\dell\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: toolz in c:\\users\\dell\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\dell\\anaconda\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\dell\\anaconda\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\dell\\anaconda\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\dell\\anaconda\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\dell\\anaconda\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\dell\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\dell\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\dell\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\dell\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2023.7.22)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\dell\\anaconda\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (22.1.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\dell\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\dell\\anaconda\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\dell\\anaconda\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "03f66cbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "23e0c426",
   "metadata": {},
   "outputs": [],
   "source": [
    "import altair as alt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7b1c67d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d28f0153",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-04-28 12:58:14.264 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\DELL\\anaconda\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "pipe_lr = joblib.load(open(\"model/text_emotion2.pkl\", \"rb\"))\n",
    "\n",
    "emotions_emoji_dict = {\"anger\": \"😠\", \"disgust\": \"🤮\", \"fear\": \"😨😱\", \"happy\": \"🤗\", \"joy\": \"😂\", \"neutral\": \"😐\", \"sad\": \"😔\",\n",
    "                       \"sadness\": \"😔\", \"shame\": \"😳\", \"surprise\": \"😮\"}\n",
    "\n",
    "\n",
    "def predict_emotions(docx):\n",
    "    results = pipe_lr.predict([docx])\n",
    "    return results[0]\n",
    "\n",
    "\n",
    "def get_prediction_proba(docx):\n",
    "    results = pipe_lr.predict_proba([docx])\n",
    "    return results\n",
    "\n",
    "\n",
    "def main():\n",
    "    st.title(\"Text Emotion Detection\")\n",
    "    st.subheader(\"Detect Emotions In Text\")\n",
    "\n",
    "    with st.form(key='my_form'):\n",
    "        raw_text = st.text_area(\"Type Here\")\n",
    "        submit_text = st.form_submit_button(label='Submit')\n",
    "\n",
    "    if submit_text:\n",
    "        col1, col2 = st.columns(2)\n",
    "\n",
    "        prediction = predict_emotions(raw_text)\n",
    "        probability = get_prediction_proba(raw_text)\n",
    "\n",
    "        with col1:\n",
    "            st.success(\"Original Text\")\n",
    "            st.write(raw_text)\n",
    "\n",
    "            st.success(\"Prediction\")\n",
    "            emoji_icon = emotions_emoji_dict[prediction]\n",
    "            st.write(\"{}:{}\".format(prediction, emoji_icon))\n",
    "            st.write(\"Confidence:{}\".format(np.max(probability)))\n",
    "\n",
    "        with col2:\n",
    "            st.success(\"Prediction Probability\")\n",
    "            #st.write(probability)\n",
    "            proba_df = pd.DataFrame(probability, columns=pipe_lr.classes_)\n",
    "            #st.write(proba_df.T)\n",
    "            proba_df_clean = proba_df.T.reset_index()\n",
    "            proba_df_clean.columns = [\"emotions\", \"probability\"]\n",
    "\n",
    "            fig = alt.Chart(proba_df_clean).mark_bar().encode(x='emotions', y='probability', color='emotions')\n",
    "            st.altair_chart(fig, use_container_width=True)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
