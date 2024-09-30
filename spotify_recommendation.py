import numpy as np
from tqdm import tqdm

class Spotify_Recommendation:
    def __init__(self, dataset):
        self.dataset = dataset

    def recommend(self, song_name, amount=1):
        song = self.dataset[(self.dataset.track_name.str.lower() == song_name.lower())].head(1).values[0]
        
        rec = self.dataset[self.dataset.track_name.str.lower() != song_name.lower()]

        distance = []

        non_numeric_cols = ['artists', 'track_name', 'track_id']

        for songs in tqdm(rec.values):
            d = 0
            for col in np.arange(len(self.dataset.columns)):
                column_name = self.dataset.columns[col]
                if column_name not in non_numeric_cols:
                    try:
                        d += np.absolute(float(song[col]) - float(songs[col]))
                    except ValueError:
                        pass
            distance.append(d)

        rec['distance'] = distance

        rec = rec.sort_values('distance')

        columns = ['artists', 'track_name']
        return rec[columns].head(amount)
