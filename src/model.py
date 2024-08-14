import pickle
import os

def load_model():
    # Correct path without the extra 'src' directory
    model_path = os.path.join("C:\\Users\\pedro\\Downloads\\Faculdade\\9_semestre\\Mlops\\Aula_2\\mlops_api\\models", "model.pkl")
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model

def load_encoder():
    # Correct path without the extra 'src' directory
    encoder_path = os.path.join("C:\\Users\\pedro\\Downloads\\Faculdade\\9_semestre\\Mlops\\Aula_2\\mlops_api\\models", "ohe.pkl")
    with open(encoder_path, "rb") as f:
        encoder = pickle.load(f)
    return encoder
