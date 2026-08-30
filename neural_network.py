# 1. IMPORTS
# we will use tokenizer.py 's  vocabulary .
import tokenizer

# NumPy for mathematical operations
import numpy as np

import training_data
"""
# ============================================================
# 2. BASIC MODEL SETTINGS
# ============================================================
"""
# how many tokens are existing on Vocabulary?↓
vocab_size = len(tokenizer.vocabulary)

# how many numbers will stay for each token's vector ?↓
embedding_size = 8

"""
# ============================================================
# 3. EMBEDDING MATRIX
# ============================================================
"""
#  8-dimensional vector for each vocabulary token
#
# Shape:
# (vocab_size, embedding_size)
# = (20, 8)
#
# এখন values random।
# Training-এর সময় এগুলো শিখবে।
embedding = np.random.randn(vocab_size, embedding_size)

"""
# ============================================================
# 4. MODEL PARAMETERS
# ============================================================
"""
# Hidden vector-এর 8টি value থেকে vocabulary-এর
# 20টি token-এর score তৈরি করার জন্য weights।
#
# Shape:
# (embedding_size, vocab_size)
# = (8, 20)
weights = np.random.randn(embedding_size, vocab_size)


# প্রতিটি vocabulary token-এর জন্য একটি bias।
#
# Shape:
# (20,)
bias = np.zeros(vocab_size)


# ============================================================
# 5. SOFTMAX FUNCTION
# ============================================================

# Raw scores-কে probabilities-এ convert করবে।
#
# Input:
#     scores → (20,)
#
# Output:
#     probabilities → (20,)
#
# সব probability-এর যোগফল প্রায় 1 হবে।
def softmax(scores):

    # প্রতিটি score-এর exponential বের করি।
    exp_scores = np.exp(scores)

    # সব exponential value যোগ করি।
    total = np.sum(exp_scores)

    # প্রত্যেকটি exponential-কে total দিয়ে ভাগ করি।
    probabilities = exp_scores / total

    # Probability distribution ফেরত দিই।
    return probabilities


# ============================================================
# 6. FORWARD PASS
# ============================================================

# এই function একটি input sequence নিয়ে
# model-এর prediction তৈরি করবে।
#
# এখন আর কোনো fixed:
#     [1, 6, 5, 1]
#
# নেই।
#
# যে input_sequence পাঠাব,
# সেটার ওপরেই calculation হবে।
def forward(input_sequence):

    # --------------------------------------------------------
    # Step 1: Embedding lookup
    # --------------------------------------------------------
    #
    # Token IDs দিয়ে embedding matrix থেকে
    # corresponding vectors বের করি।
    #
    # Example:
    # input_sequence = [1, 6, 5, 1]
    #
    # Output shape:
    # (4, 8)
    embedded_input = embedding[input_sequence]


    # --------------------------------------------------------
    # Step 2: Mean pooling
    # --------------------------------------------------------
    #
    # চারটি 8-dimensional vector-এর average নিই।
    #
    # (4, 8)
    #    ↓
    # (8,)
    #
    # ফলে পুরো input sequence-এর একটি
    # 8-dimensional hidden representation পাই।
    hidden = embedded_input.mean(axis=0)


    # --------------------------------------------------------
    # Step 3: Linear layer
    # --------------------------------------------------------
    #
    # Hidden vector:
    # (8,)
    #
    # Weights:
    # (8, 20)
    #
    # তাই:
    #
    # (8,) @ (8, 20)
    #        ↓
    #      (20,)
    #
    # তারপর bias যোগ করি।
    scores = hidden @ weights + bias


    # --------------------------------------------------------
    # Step 4: Softmax
    # --------------------------------------------------------
    #
    # Raw scores-কে probability distribution-এ
    # convert করি।
    probabilities = softmax(scores)


    # --------------------------------------------------------
    # Step 5: Prediction return
    # --------------------------------------------------------
    #
    # 20টি vocabulary token-এর probability ফেরত যাবে।
    return probabilities

def cross_entropy(probability):
    loss = -np.log(probability)
    return loss

for input_sequence, target in zip(training_data.inputs, training_data.targets):
    probabilities = forward(input_sequence)
    target_probability = probabilities[target]
    loss = cross_entropy(target_probability)
    


def calculate_loss(input_sequence, target):
    # এখানে forward()
    probabilities = forward(input_sequence)
    # target probability
    target_probability = probabilities[target]
    # cross entropy
    loss = cross_entropy(target_probability)
    # return loss
    return loss
print(calculate_loss(training_data.inputs[0], training_data.targets[0]))


epsilon = 0.0001
original = weights[0, 0]

weights[0, 0] = original - epsilon

loss_minus = calculate_loss(
    training_data.inputs[0],
    training_data.targets[0]
)

weights[0, 0] = original + epsilon

loss_plus = calculate_loss(
    training_data.inputs[0],
    training_data.targets[0]
)

gradient = (loss_plus - loss_minus) / (2 * epsilon)

weights[0, 0] = original

#=============

# ==============================
# LOSS BEFORE UPDATE
# ==============================

loss_before = calculate_loss(
    training_data.inputs[0],
    training_data.targets[0]
)


# ==============================
# WEIGHT UPDATE
# ==============================

learning_rate = 0.1

old_weight = weights[0, 0]

new_weight = old_weight - learning_rate * gradient

weights[0, 0] = new_weight

print("Old weight:", old_weight)
print("New weight:", new_weight)


# ==============================
# LOSS AFTER UPDATE
# ==============================

loss_after = calculate_loss(
    training_data.inputs[0],
    training_data.targets[0]
)

#///////////////////////////////
epsilon = 0.0001

grad_weights = np.zeros_like(weights)

for i in range(weights.shape[0]):
    for j in range(weights.shape[1]):

        original = weights[i, j]

       # weiget decreasing
        weights[i, j] = original - epsilon
        # loss_minus বের করো
        loss_minus = calculate_loss(
    training_data.inputs[0],
    training_data.targets[0]
)

        # weight একটু বাড়াও
        weights[i,j] = original + epsilon

        # loss_plus বের করো
        loss_plus = calculate_loss(
    training_data.inputs[0],
    training_data.targets[0]
)

        # gradient বের করো
        gradient = (loss_plus - loss_minus)/(2 * epsilon)

        # gradient matrix-এ রাখো
        grad_weights[i, j] = gradient
        weights[i, j] = original
learning_rate = 0.1

# পুরো weights matrix update
weights = weights - learning_rate * grad_weights

#//////////////////////////////////
epochs = 100

for epoch in range(epochs):

    # প্রতিটি training example-এর জন্য
    for input_sequence, target in zip(
        training_data.inputs,
        training_data.targets
    ):

        # ------------------------------------------------
        # 1. বর্তমান input-এর prediction এবং loss
        # ------------------------------------------------
        prediction_on_loop = forward(input_sequence)
        loss_on_loop = calculate_loss(input_sequence, target)


        # ------------------------------------------------
        # 2. সব weights-এর gradient রাখার জন্য matrix
        # ------------------------------------------------
        grad_weights = np.zeros_like(weights)


        # ------------------------------------------------
        # 3. প্রতিটি weight-এর gradient বের করা
        # ------------------------------------------------
        epsilon = 0.0001

        for i in range(weights.shape[0]):
            for j in range(weights.shape[1]):

                # বর্তমান weight সংরক্ষণ
                original = weights[i, j]


                # ----------------------------------------
                # weight একটু কমাই
                # ----------------------------------------
                weights[i, j] = original - epsilon

                loss_minus = calculate_loss(
                    input_sequence,
                    target
                )


                # ----------------------------------------
                # weight একটু বাড়াই
                # ----------------------------------------
                weights[i, j] = original + epsilon

                loss_plus = calculate_loss(
                    input_sequence,
                    target
                )


                # ----------------------------------------
                # Numerical gradient
                # ----------------------------------------
                gradient = (
                    loss_plus - loss_minus
                ) / (2 * epsilon)


                # gradient matrix-এ রাখি
                grad_weights[i, j] = gradient


                # ----------------------------------------
                # আসল weight ফিরিয়ে আনি
                # ----------------------------------------
                weights[i, j] = original


        # ------------------------------------------------
        # 4. Gradient descent দিয়ে weights update
        # ------------------------------------------------
        learning_rate = 0.1

        weights = weights - learning_rate * grad_weights


    # ----------------------------------------------------
    # 5. প্রতি epoch শেষে loss দেখাই
    # ----------------------------------------------------
    print("Epoch:", epoch + 1, "Loss:", loss_on_loop)

# ============================================================
# MODEL SAVE
# ============================================================

# Training-এর পরে model-এর learned parameters save করছি।
np.savez(
    "sunnygpt_model.npz",
    embedding=embedding,
    weights=weights,
    bias=bias
)

print("Model saved successfully! 😎")

def predict_next(input_sequence):
    # 1. forward() দিয়ে probabilities বের করো
    predict_nexts_forward = forward(input_sequence)
    # 2. সবচেয়ে বড় probability-এর index বের করো
    index_of_high_probability = np.argmax(predict_nexts_forward)
    # Hint: np.argmax(...)
    # 3. index return করো
    return index_of_high_probability


predicted_id = predict_next(input_sequence)

a = tokenizer.decoder([predicted_id])

print(a)

# ============================================================
# USER INPUT → TOKENIZER → MODEL → NEXT WORD
# ============================================================

# ব্যবহারকারীর কাছ থেকে একটি sentence নেব।
user_text = input("Enter text: ")

# ------------------------------------------------------------
# Step 1: Text → Token IDs
# ------------------------------------------------------------
input_ids = tokenizer.encoder(user_text)

print("Input IDs:", input_ids)


# ------------------------------------------------------------
# Step 2: Token IDs → Model
# ------------------------------------------------------------
# Model probability distribution তৈরি করবে।
probabilities = forward(input_ids)


# ------------------------------------------------------------
# Step 3: সবচেয়ে সম্ভাবনাময় token খুঁজে বের করি
# ------------------------------------------------------------
predicted_id = np.argmax(probabilities)

print("Predicted ID:", predicted_id)


# ------------------------------------------------------------
# Step 4: Token ID → Word
# ------------------------------------------------------------
predicted_word = tokenizer.decoder([predicted_id])

print("Predicted word:", predicted_word)

#end
