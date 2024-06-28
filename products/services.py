from sentence_transformers import SentenceTransformer
from PIL import Image
import pandas as pd
import numpy as np
from scipy import spatial
import copy
import os

def get_df(df_path: str) -> pd.DataFrame:
    '''
    Функция для сохранения датафрейма в json и его корректному импорту.
    '''

    data_df = pd.read_json(df_path)
    data_df['Embedding'] = data_df['Embedding'].apply(lambda x: np.array(x))
    return data_df

def calculate_cos_dist(emb_a: np.array, emb_b: np.array) -> float:
    '''
    Функция для вычисления косинусного расстояния между двумя векторами. 
    '''

    result_distance = spatial.distance.cosine(emb_a, emb_b)
    return result_distance

def found_similar_images(input_vec: str, images_db: pd.DataFrame, n: int=5) -> pd.DataFrame:
    '''
    Функцию для поиска по базе. Она будет возвращать n-самых близких
    изображений из базы по отношению ко входному изображению.
    '''
    
    result_df = copy.deepcopy(images_db)
    result_df['Distance_with_input'] = result_df.apply(lambda x: calculate_cos_dist(input_vec, x['Embedding']), axis=1)
    result_df_sorted = result_df.sort_values('Distance_with_input').reset_index()
    result_df_sorted = result_df_sorted[['Image', 'Distance_with_input']]
    return result_df_sorted.head(n)


model_name = 'clip-ViT-B-16'
st_model = SentenceTransformer(model_name)
images_db = get_df('back_media/data.json')


class ProductSearchService:

    @classmethod
    def searc_simmilar_products(cls, file):
        images = []
        imgfile = Image.open(file.file)
        input_img = st_model.encode(imgfile)
        result_df = found_similar_images(input_img, images_db)
        print(result_df)
        for i in range(len(result_df)):
            images.append({'image': os.path.join('/back_media/images/', result_df.iloc[i].Image)})

        print(images)
        return images
