from sentence_transformers import SentenceTransformer
from scipy import spatial
from PIL import Image
import pandas as pd
import numpy as np
import copy
import os

model_name = 'clip-ViT-B-16'
st_model = SentenceTransformer(model_name)

def vectorize_img(img_path: str, model: SentenceTransformer=st_model) -> np.array:
    img = Image.open(img_path)
    return st_model.encode(img)

def create_images_db(images_folder: str, model: SentenceTransformer=st_model) -> pd.DataFrame:
    '''
    Функция которая получает папку с изображениями и векторизирует их
    по модели, в итоге выдыет датафрейм, каждая строка которого содержит
    информацию о названии изображения и его векторном представлении.
    '''

    data_dict = dict()
    for file_name in os.listdir(images_folder):
        if os.path.isfile(images_folder + file_name):
            image_path = images_folder + file_name
            emb = vectorize_img(image_path)
            data_dict[file_name] = emb
        pd.DataFrame(data_dict.items(), columns=['Image', 'Embedding']).to_json("back_media/data.json")
    # return pd.DataFrame(data_dict.items(), columns=['Image', 'Embedding'])

def calculate_cos_dist(emb_a: np.array, emb_b: np.array) -> float:
    '''
    Функция для вычисления косинусного расстояния между двумя векторами. 
    '''

    result_distance = spatial.distance.cosine(emb_a, emb_b)
    return result_distance


images_folder = 'back_media/images/'
create_images_db(images_folder)
