import pandas as pd
from prophet import Prophet
from matplotlib import pyplot

from repositories.abstract_repository import ListParams
from repositories.raziel_repository import RazielRepository


class PredictorManager:
    def __init__(self, raziel_repo: RazielRepository):
        self.raziel_repo = raziel_repo

    def deaths_forecasting(self, params: ListParams, var1: str, var2: str):
        df = self.raziel_repo.prepare_and_gruping_dataframe(params, var1, var2)
        df = df.rename(columns={'DEFU': 'y', 'ANO': 'year'})
        # df['y'][40] = df['y'].mean()

        df2 = df.copy()
        df2['ds'] = pd.to_datetime(df2['year'], format='%Y')
        m = Prophet().fit(df2)
        future = m.make_future_dataframe(periods=50, freq='y', include_history=True)
        fcst = m.predict(future)
        m.plot(fcst)
        pyplot.show()
