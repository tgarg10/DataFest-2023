import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import tensorflow_hub as hub
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define the module URL
module_url = "https://tfhub.dev/google/universal-sentence-encoder/1?tf-hub-format=compressed"

# Import the Universal Sentence Encoder's TF Hub module
embed = hub.Module(module_url)

subcat = "Health Care"

# Sample text
'''
messages = [
    # Smartphones
    "My phone is not good.",
    "Your cellphone looks great.",

    # Weather
    "Will it snow tomorrow?",
    "Recently a lot of hurricanes have hit the US",

    # Food and health
    "An apple a day, keeps the doctors away",
    "Eating strawberries is healthy",
]
'''
df1 = pd.read_csv("newquestionposts.csv", sep = '¬', error_bad_lines=False, encoding='ISO-8859-1')
df2 = pd.read_csv("questions.csv", sep = ',', error_bad_lines=False, encoding='ISO-8859-1')
df = pd.merge(df1,df2, on='QuestionUno')
messages_old = list(df[df.Subcategory == subcat]["PostText"])
messages = []
for msg in messages_old:
    try:
        msg.encode('utf-8')
        messages.append(msg)
    except:
        pass

# Define the input placeholder
similarity_input_placeholder = tf.placeholder(tf.string, shape=(None))

# Encode the messages with the Universal Sentence Encoder
similarity_message_encodings = embed(similarity_input_placeholder)

# Define the function to display a heatmap
def heatmap(x_labels, y_labels, values):
    fig, ax = plt.subplots()
    im = ax.imshow(values)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(x_labels)))
    ax.set_yticks(np.arange(len(y_labels)))

    # ... and label them with the respective list entries
    ax.set_xticklabels(x_labels)
    ax.set_yticklabels(y_labels)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", fontsize=10, rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(y_labels)):
        for j in range(len(x_labels)):
            text = ax.text(j, i, "%.2f"%values[i, j], ha="center", va="center", color="w", fontsize=6)

    fig.tight_layout()
    plt.show()

# Initialize the TensorFlow session
with tf.Session() as session:
    # Run the initializer operations
    session.run(tf.global_variables_initializer())
    session.run(tf.tables_initializer())

    # Compute the message embeddings
    message_embeddings_ = session.run(similarity_message_encodings, feed_dict={similarity_input_placeholder: messages})

    # Compute the correlation matrix
    corr = np.inner(message_embeddings_, message_embeddings_)
    #for msg in messages: print(msg+'\n')
    mask = np.where((corr >  0.86) & (corr <  0.98))
    for row, col in zip(*mask):
        if row == col: continue
        print(f"{messages[row]}\n{messages[col]}\n")#{corr[row, col]}")

    # Display the correlation matrix as a heatmap
    # heatmap(messages, messages, corr)

    