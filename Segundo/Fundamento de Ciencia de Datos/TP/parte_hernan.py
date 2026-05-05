import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def autos():
    # print(help(pd.read_csv))
    au = pd.read_csv('autos.csv', encoding='latin1', sep=';')
    # print(au.info())
    print(len(au['respondent_id'].unique()))

def punto3():
    au = pd.read_csv('autos.csv', encoding='latin1', sep=';')
    enc = pd.read_excel('encuestados.xlsx')
    data = pd.merge(au, enc, on='respondent_id')

    sexos = data.value_counts('sexo', normalize=True) * 100
    print(sexos)
    
    sns.set_style('whitegrid')
    sns.barplot(sexos)
    plt.title('Proporciones de sexos entre los encuestados')
    plt.xlabel('Sexo')
    plt.ylabel('Porcentaje (%)')
    plt.legend()
    plt.show()

    ingresos = data.value_counts('ingreso_hogar', normalize=True) * 100
    print(ingresos)

    sns.set_style('whitegrid')
    sns.barplot(data=ingresos)
    plt.title('Porcentajes de categorias de ingresos')
    plt.xlabel('Ingreso mensual (ARS)')
    plt.ylabel('Porcentaje (%)')
    plt.show()

    # Segun lo que se puede ver en ambos graficos, la proporcion de hombres entre los 
    # encuestados es ligeramente superior a la de mujeres. Y la cantidad de encuestados 
    # para cada categoria de ingreso decrece a medida que los ingresos aumentan, siendo 
    # la categoria con mas encuestados la respectiva a ingresos menores a 500k.

def punto5():
    au = pd.read_csv('autos.csv', encoding='latin1', sep=';')
    enc = pd.read_excel('encuestados.xlsx')
    data = pd.merge(au, enc, on='respondent_id')

    sns.set_style("whitegrid")
    # sns.kdeplot(data['precio_compra_N'], hue='ingreso_hogar', label='TMIN', fill=True, color='blue')
    # sns.kdeplot(
    #         data=data, 
    #         x='precio_compra_N', 
    #         hue='ingreso_hogar', 
    #         # label='ingreso_hogar',
    #         fill=True, 
    #         palette="magma", 
    #         common_norm=False
    #     )

    # rangos_ing = data['ingreso_hogar'].unique().tolist()
    rangos_ing = ['<500k', '500k-1M', '1M-2M', '2M-4M', '>4M']
    for ing in rangos_ing:
        sns.kdeplot(
                data=data[data['ingreso_hogar'] == ing], 
                x='precio_compra_N', 
                # hue='ingreso_hogar', 
                label=ing,
                fill=True, 
                # palette="magma", 
                common_norm=False
            )
    
    plt.title('Distribuciones de precios de compra por categoria de ingresos')
    plt.xlabel('Precio de compra (ARS)')
    plt.ylabel('Densidad')
    plt.legend()
    plt.show()


    sns.violinplot(data=data, x='precio_compra_N', y='ingreso_hogar', split=False)
    plt.xlabel('Precio de compra (ARS)')
    plt.ylabel('Densidad')
    plt.show()

if __name__ == '__main__':
    punto5()