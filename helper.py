def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby('Team').sum()[['Bronze', 'Gold', 'Silver']].sort_values('Gold', ascending=False).reset_index()
    medal_tally['total'] = medal_tally['Bronze'] + medal_tally['Gold'] + medal_tally['Silver']

    medal_tally['Bronze'] = medal_tally['Bronze'].astype(int)
    medal_tally['Gold'] = medal_tally['Gold'].astype(int)
    medal_tally['Silver'] = medal_tally['Silver'].astype(int)
    medal_tally['total'] = medal_tally['total'].astype(int)
    return medal_tally

def country_year_list(df):
    year = df['Year'].unique().tolist()
    year.sort()
    year.insert(0, 'overall')

    team = df['Team'].unique().tolist()
    team.sort()
    team.pop(0)
    team.insert(0, 'overall')

    return year , team


def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == "overall" and country == "overall":
        temp_df = medal_df
    if year == "overall" and country != "overall":
        flag = 1
        temp_df = medal_df[medal_df['Team'] == country]
    if year != "overall" and country == "overall":
        temp_df = medal_df[medal_df['Year'] == year]
    if year != "overall" and country != "overall":
        temp_df = medal_df[(medal_df['Team'] == country) & (medal_df['Year'] == year)]

    if flag == 1:
        temp_df = temp_df.groupby('Year').sum()[['Bronze', 'Gold', 'Silver']].sort_values('Year').reset_index()
    else:
        temp_df = temp_df.groupby('Team').sum()[['Bronze', 'Gold', 'Silver']].sort_values('Gold',
                                                                                          ascending=False).reset_index()

    temp_df['total'] = temp_df['Bronze'] + temp_df['Gold'] + temp_df['Silver']
    temp_df['Bronze'] = temp_df['Bronze'].astype(int)
    temp_df['Gold'] = temp_df['Gold'].astype(int)
    temp_df['Silver'] = temp_df['Silver'].astype(int)
    temp_df['total'] = temp_df['total'].astype(int)
    return temp_df

def overtime(df):
    nation_overtime = df.drop_duplicates(['Year', 'region'])['Year'].value_counts().reset_index().sort_values('index')
    nation_overtime = nation_overtime.rename(columns={'index': 'edition', 'Year': 'total_country'})
    return nation_overtime
def overtime_event(df):
    nation_overtime = df.drop_duplicates(['Year', 'Event'])['Year'].value_counts().reset_index().sort_values('index')
    nation_overtime = nation_overtime.rename(columns={'index': 'edition', 'Year': 'total_event'})
    return nation_overtime

def most_successful(df,sport):
    sdf = df.dropna(subset = ['Medal'])
    if sport != 'overall':
        ss = sdf[sdf['Sport']== sport]
        ss['total'] = ss['Bronze']+ss['Gold']+ss['Silver']
        e = ss.groupby('Name').sum()['total'].reset_index()
        e = e.sort_values(['total'],ascending = False).reset_index()
    return  e

def sport_find(df):
    sport = df['Sport'].unique().tolist()
    sport.sort()
    sport.insert(0, 'overall')
    return sport

def most_successful_overall(df):
    ll = df.dropna(subset=['Medal']).reset_index()
    ll = ll['Name'].value_counts().reset_index().merge(df, left_on='index', right_on='Name', how='left')[
        ['index', 'Sport','Name_x']]
    ll = ll.drop_duplicates(subset=['index'])
    return ll



