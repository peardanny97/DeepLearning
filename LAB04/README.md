# LAB 04

## Now, We'll handle texts, not images. Is there any differences?

Of course, there are many differences between processing images and texts. One is that text cannot be expressed directly in matrices or tensors. We know an image can be expressed in Tensor(n_channel, width, height). But how about an text sentence? Can word 'Homework' can be expressed in tensor directly? By what laws? With what shapes? Even if it can, which one is closer to the word, 'Burden', or 'Work'? This is called 'Word Embedding Problem' and be considered as one of the most important problem in Natural Language Process(NLP) resarch. Fortunatly, there are some generalized solution in this problem (though not prefect, anyway) and both Tensorflow and Pytorch give basic APIs that solve this problem automatically. You may use those APIs in this homework. 

The other one is that text is sequential data. Generally, when processing images, without batch, input is just one image. However in text, input is mostly some or one paragraphs/sentences, which is sequential data of embedded character or words. So, If we want to generate word 'Homework' with start token 'H', 'o' before 'H' and 'o' before 'Homew' should operate different when it gives to input. This is why we use RNN-based model in deep learning when processing text data.

## Task1: RNN/LSTM/GRU Module

The main task is to create RNN/LSTM/GRU network. You can use any tensorflow/keras api that basically given.

Basically build_model are given, but you can add other functions that help your networks.

## Optional Task: Train & Generate Code

These cells would define functions of training network and generating text function. 

You can change these codes but if then you should annotate where do you make change precisely.
One annotation line should not cover more than 5 lines that you make your changes.  
Also, do not delete original code, just comment out them. (or make another cells of jupyter notebook)

## Execution Code & Credit Creterion
Half Credit (4 points): Generate some ugly text, without any meaningful words.

Q3 Credits (6 points): In SEQ_LENGTH 200, generate 6 or less differet words.

Full Credit (8 points): in SEQ_LENGTH 200, generate 7 or more different words.

## Using Pre-trained Networks: Transformers

Actually, RNN-based sequential model is now regarded as little bit old-fashioned, since 'Transformer' model was announced in paper 'Attention is All You Need'(https://arxiv.org/abs/1706.03762). Now this model is widely used on many state-of-the-art sequential-data-use model, and even in non-sequential-data-use (ex)image) model too. However, model training cost is too heavy(maybe you need multiple million-won GPUs) to train on this homework. Fortunately, there is package called 'transformers' that contains multipe pre-trained transformer-based model that can be used directly. Below is example of text generation using GPT2, which is one of the most popular pre-trained NLP models.

You can install this package with 'pip install transformers'. To download pre-traind model, you may have 2GB or more free disk space.

## Task2: Follow Tutorial of Fine-tuned Networks (2 points.)
There are hundreds of fine-tuned NLP models in 'transformers' package. Try one of these models and follow its tutorial (except language translation model). Results must produce some meaningful, or funny one, and you must write down what model you choose and explain its function (ex) what is input/output, what does it mean etc) with one or two sentences. 

Hint: You can find list of pre-trained models in 'transformers' package on https://huggingface.co/models
