import pandas as pd
import numpy as np
import os





def extrapolarTabua(fa, df, w, f_x):
    feature_list = ['x', 'q_x', 'd_x','l_x','L_x','T_x', 'e_x', 'u_x', 'm_x','p_x']

    df = pd.DataFrame(0, index= np.arange(start=0, stop=w+1), columns=feature_list)

    l = 100000
    df['x']=np.arange(start=0, stop=w+1)
    df.at[0, 'l_x'] = l

    df['q_x'][0:80] = data_original['q_x'][0:80]/1000

    df_aux = df[:80]

    i = 1
    w_aux = len(df_aux)
    while i < w_aux+1:
        df_aux.at[i-1, 'd_x'] = df_aux.at[i-1, 'l_x']*df_aux.at[i-1, 'q_x']
        df_aux.at[i, 'l_x'] = df_aux.at[i-1, 'l_x'] - df_aux.at[i-1, 'd_x']
        i += 1

    df_aux['p_x'] = 1 - df_aux['q_x']

    df[:81] = df_aux[:81]

    i = 80
    while i < w:
        df.at[i+1, 'l_x'] = (df.at[i, 'l_x']*df.at[i, 'l_x'])/(df.at[i-1, 'l_x']+fa)
        i+=1

    i = 80
    while i < w:
        df.at[i,'d_x'] = df.at[i, 'l_x']-df.at[i+1, 'l_x']
        i+=1

    i = 80
    while i < w:
        df.at[i,'q_x'] = df.at[i, 'd_x']/df.at[i, 'l_x']
        i+=1

    df['p_x'] = 1 - df['q_x']

    f_x = 0.5
    i = 0
    while i < w:
        df.at[i, 'L_x'] = f_x*df.at[i, 'l_x'] + (1-f_x)*df.at[i+1, 'l_x'] 
        #df.at[i, 'L_x'] = (df.at[i, 'l_x']+df.at[i+1, 'l_x'])/2
        i+=1

    pd.set_option('display.float_format', lambda x: '%.5f' % x)

    df['T_x'] = df['T_x'].apply(lambda x: float(x))
    i = 0
    while i < w:
        df.at[i, 'T_x'] = df.loc[i:w, 'L_x'].sum() # w = index of the last row
        i += 1

    df['e_x'] = df['T_x']/df['l_x']

    return df


cwd = os.getcwd()
print(cwd)
data_original = pd.read_excel(cwd+"./Planilhas/q_xe_x2.xlsx")

w = 115
fa = 100



def calcular(data_original, fa, w, f_x):
    df = extrapolarTabua(data_original, w, fa, f_x)

    print(f"e_x data extrapolada: {df.at[80, 'e_x']}")
    print(f"e_x data original: {data_original.at[80, 'e_x']}")
    diferenca = df.at[80, 'e_x'] - data_original.at[80, 'e_x']
    print(diferenca)
    achou = False
    while achou == False:
        print(f"FA -> {fa}")
        if diferenca > 0:
            fa += 1
            df_aux = extrapolarTabua(fa, data_original, w, f_x)
            diff = df_aux.at[80, 'e_x'] - data_original.at[80, 'e_x']
            if abs(diff) < abs(diferenca):
                diferenca = diff
                df = df_aux
            elif abs(diff) > abs(diferenca):
                achou = True
                fa -= 1
        elif diferenca < 0:
            fa -= 1
            df_aux = extrapolarTabua(fa, data_original, w, f_x)
            diff = df_aux.at[80, 'e_x'] - data_original.at[80, 'e_x']
            if abs(diff) < abs(diferenca):
                diferenca = diff
                df = df_aux
            elif abs(diff) > abs(diferenca):
                achou = True
                fa += 1

    i = 0
    while i < w:
        x = df.at[i, 'q_x'].round(6)
        # if i == 109:
        #     print(x)
        #     print(x >= 1)
        if x == 1:
            print(df[107:115])
            print(x)
            print(i)
            #print(df[:i])
            break
        i += 1
    print(fa)
    df = df[0:i+1]
    print(df)
    arquivo = "output2.xlsx"
    with pd.ExcelWriter(arquivo) as writer:
        data_original.to_excel(writer, sheet_name='Planilha')
        df.to_excel(writer, sheet_name='Planilha Extrapolada')
    os.system(f'cmd /c {arquivo}')
    pd.reset_option('display.float_format')

