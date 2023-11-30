import charts
import read_csv

if __name__ == '__main__':
    labels, values = read_csv.obtain_porcentage_world('PROYECTO DE GRAFICA DE TORTAS/world_population.csv')
    charts.generate_charts_pie(labels, values)