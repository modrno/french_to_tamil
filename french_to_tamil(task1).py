# -*- coding: utf-8 -*-
"""French_to_tamil(task1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F4Sh9Z1VzXT3yTgGMkTQn6K7NRxxOziS

**Write a python function to implement a  basic toenization algorithm for a given languages**
"""

!pip install gradio

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import gradio as gr

fr_en_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
fr_en_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fr-en")


en_ta_tokenizer = AutoTokenizer.from_pretrained("suriya7/English-to-Tamil")
en_ta_model = AutoModelForSeq2SeqLM.from_pretrained("suriya7/English-to-Tamil")

def translate_fr_to_en(text):
    inputs = fr_en_tokenizer(text, return_tensors="pt", padding=True)
    outputs = fr_en_model.generate(**inputs, max_length=40, num_beams=4, early_stopping=True)
    translated_text = fr_en_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

def translate_en_to_ta(text):
    tokenized = en_ta_tokenizer([text], return_tensors='pt')
    out = en_ta_model.generate(**tokenized, max_length=128)
    translated_text = en_ta_tokenizer.decode(out[0], skip_special_tokens=True)
    return translated_text

def translate_fr_to_ta(text):

    if len(text.split()) == 1 and len(text) == 5:

        translated_to_english = translate_fr_to_en(text)


        translated_to_tamil = translate_en_to_ta(translated_to_english)

        return translated_to_tamil
    else:
        return " "

interface = gr.Interface(
    fn=translate_fr_to_ta,
    inputs="text",
    outputs="text",
    title="French to Tamil Translator",
    description="Enter a single French word with exactly five letters to translate it into Tamil."
)


interface.launch()

