"""
현재 연령대별 인구 수
2020년의 전체 사망자수 대비 연령대별 사망자 비율
신생아수 매년 25만명 고정
으로 인구 피라미드 시뮬레이션
"""

import pandas as pd
df_currentpopulation = pd.read_excel("currentpopulation.xlsx")
print(df_currentpopulation)