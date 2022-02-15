"""
현재 연령대별 인구 수
2020년의 전체 사망자수 대비 연령대별 사망자 비율
신생아수 매년 25만명 고정
으로 인구 피라미드 시뮬레이션
"""
import pandas as pd
import matplotlib.pyplot as plt

df_curpop = pd.read_excel("currentpopulation.xlsx")
df_deathrate = pd.read_excel("deathrate_2.xlsx")
print(df_curpop)

current_bar = df_curpop.plot.bar(x='age', y='population', rot=0)
plt.show()

"""
1년 지날 때마다 n세의 population에 사망자수 빼고 n+1세의 row로 올린다.
"""
year_count = 21


def pop_counter(age, cnt):
    if cnt == 1:
        now_population = df_curpop.loc[age]['population']
    else:
        now_population = df_curpop.loc[age][f'+{cnt - 1}']
    """
    예를 들어 13세면, 어떤 deathrate를 가져와야 하나? 10-14세, 3번째 인덱스의 deathrate 값을 가져와야 한다.
    구간넓이가 5이므로 5로 나눈 몫 + 1을 해주면된다. 
    
    """
    if age == 85:
        """
        +1 column에 있는 84세로 구한 값에, 기존 85세 이상인구에 사망 고려하여 빼준 인구수를 더해줘야 함
        이때 90세 이상에서 사망률은 대략 100000명 당 18000명
        """
        df_curpop.loc[85][f'+{cnt}'] += int(now_population * (1-(18000/100000)))

    else:
        row = int(age / 5) + 1
        deathrate = df_deathrate.loc[row]['deathrate']
        after_death = int(now_population * (1-(deathrate/100000)))
        df_curpop.loc[age+1][f'+{cnt}'] = after_death

for cnt in range(1, year_count):
    df_curpop[f'+{cnt}'] = 0
    for i in range(len(df_curpop)):
        pop_counter(i, cnt)
    df_curpop.loc[0][f'+{cnt}'] = 250000
    print(df_curpop)

current_bar = df_curpop.plot.bar(x='age', y=f'+{year_count - 1}', rot=0)
plt.show()






