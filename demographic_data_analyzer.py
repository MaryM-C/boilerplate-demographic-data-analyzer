import pandas as pd

def percentage(num1, num2):
    return round((num1 / num2) * 100, 1)

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('./adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men_data = df.loc[df['sex'] == 'Male']
    average_age_men = round(men_data['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = len(df.loc[df['education'] == 'Bachelors'])
    percentage_bachelors = percentage(bachelors, len(df))

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    degree = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df.loc[df['education'].isin(degree)]
    lower_education = df.loc[~df['education'].isin(degree)]
    
    #People with high salary
    rich_with_degree = len(higher_education.loc[higher_education['salary'] == '>50K'])
    rich_without_degree = len(lower_education.loc[lower_education['salary'] == '>50K'])

    # percentage with salary >50K
    higher_education_rich = percentage(rich_with_degree, len(higher_education))
    lower_education_rich = percentage(rich_without_degree, len(lower_education))

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]
    num_min_workers_rich = len(num_min_workers.loc[num_min_workers['salary'] == '>50K'])

    rich_percentage = percentage(num_min_workers_rich, len(num_min_workers))

    # What country has the highest percentage of people that earn >50K?
    ppl_with_high_salary = df.loc[df['salary'] == '>50K']
    freq_countries_with_high_salary = ppl_with_high_salary['native-country'].value_counts()
    freq_countries = df['native-country'].value_counts()
    countries_by_percentage = (freq_countries_with_high_salary / freq_countries) * 100 

    highest_earning_country =  countries_by_percentage.idxmax()
    highest_earning_country_percentage = round(countries_by_percentage.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_with_high_salary = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    freq_occupation = india_with_high_salary['occupation'].value_counts()
    top_IN_occupation = freq_occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
