import pandas as pd

df = pd.read_csv('D:\\USUARIO\\Documents\\Santiago\\FreeCodeCamp\\ProyectosCv\Analizador\\adult.data.csv')

def demographics_analizer():

    print('¿Cuántas personas de cada raza están representadas en este conjunto de datos?')
    print('')
    race_count = df['race'].value_counts()
    print(race_count)
    print('')
    print('/////////////////////////////////////////////////////////////')
    print('')
    print('Cuál es la edad media de los hombres')
    print('')
    male_age_mean = df[df['sex'] == 'Male']['age'].mean()
    print(male_age_mean)
    print('')
    print('/////////////////////////////////////')
    print('')
    print('¿Cuál es el porcentaje de personas que tienen una licenciatura?')
    print('')
    education_count = df['education'].value_counts()
    print(education_count)
    print('')
    print('/////////////////////////////////////////////////////////////')
    print('')
    print('¿Qué porcentaje de personas con educación avanzada ( Bachelors, Masters, o Doctorate) ganan más de 50 000 dólares?')
    education_count = df['education'].value_counts()
    advanced_education_count = education_count[['Bachelors', 'Masters', 'Doctorate']].sum()
    advanced_education_percentage = advanced_education_count / education_count.sum() * 100
    print(advanced_education_percentage)
    print('')
    print('//////////////////////////////////////////////////////////////')
    print('')
    print('Qué porcentaje de personas sin educación avanzada ganan más de 50.000 dólares')
    education_count = df['education'].value_counts()
    no_advanced_education_count = education_count[['Some-college', '11th', '12th', 'HS-grad']].sum()
    no_advanced_education_percentage = no_advanced_education_count / education_count.sum() * 100
    print(no_advanced_education_percentage)
    print('')
    print('/////////////////////////////////////////////////////////////')
    print('')
    print('Cuál es el número mínimo de horas que trabaja una persona por semana')
    print('')
    min_hours_per_week = df['hours-per-week'].min()
    print(min_hours_per_week)
    print('')
    print('/////////////////////////////////////////////////////////////')
    print('')
    print('Qué porcentaje de las personas que trabajan el mínimo de horas semanales tienen un salario de más de 50 mil')
    min_hours_salary_percentage = (df[df['hours-per-week'] == min_hours_per_week]['salary'] == '>50K').mean() * 100
    print(min_hours_salary_percentage)
    print('')
    print('/////////////////////////////////////////////////////////////')
    print('')
    print('Qué país tiene el mayor porcentaje de personas que ganan >50 000 dólares y cuál es ese porcentaje')
    max_salary_country = df[df['salary'] == '>50K']['native-country'].value_counts().idxmax()
    max_salary_percentage = (df[df['salary'] == '>50K']['native-country'] == max_salary_country).mean() * 100
    print(f'El país con el mayor porcentaje de personas que ganan más de 50 000 dólares es {max_salary_country} con un {max_salary_percentage:.2f}%')
    print('')
    print('/////////////////////////////////////////////////////////////')
    print('')
    print('Identifique la ocupación más popular para quienes ganan >50 000 en la India')
    india_df = df[df['native-country'] == 'India']
    india_salary_df = india_df[india_df['salary'] == '>50K']
    india_job_counts = india_salary_df['occupation'].value_counts()
    print(f'La ocupación más popular para quienes ganan >50 000 en la India es {india_job_counts.idxmax()} con {india_job_counts.max()} personas')




