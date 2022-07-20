from pyalgotrading.strategy.strategy_base import StrategyBase
from pyalgotrading.constants import *


print(get_historical_data())
# class StrategyEMARegularOrder(StrategyBase):
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.timeperiod1 = self.strategy_parameters['timeperiod1']
#         self.timeperiod2 = self.strategy_parameters['timeperiod2']

#         self.main_order = None

#     def initialize(self):
#         self.main_order = {}
    
#     @staticmethod
#     def name():
#         return 'EMA Regular Order Strategy'

#     @staticmethod    
#     def versions_supported():
#         return AlgoBullsEngineVersion.VERSION_3_2_0

#         def get_crossover_value(self, instrument):
#         hist_data = self.get_historical_data(instrument)
        ema_x = talib.EMA(hist_data['close'], timeperiod=self.timeperiod1)
        ema_y = talib.EMA(hist_data['close'], timeperiod=self.timeperiod2)
#         crossover_value = self.utils.crossover(ema_x, ema_y)
#         return crossover_value

#     def strategy_select_instruments_for_entry(self, candle, instruments_bucket):

#         selected_instruments_bucket = []
#         sideband_info_bucket = []

#         for instrument in instruments_bucket:
#             crossover_value = self.get_crossover_value(instrument)
#             if crossover_value == 1:
#                 selected_instruments_bucket.append(instrument)
#                 sideband_info_bucket.append({'action': 'BUY'})
#             elif crossover_value == -1:
#                 if self.strategy_mode is StrategyMode.INTRADAY:
#                     selected_instruments_bucket.append(instrument)
#                     sideband_info_bucket.append({'action': 'SELL'})
                    
#         return selected_instruments_bucket, sideband_info_bucket